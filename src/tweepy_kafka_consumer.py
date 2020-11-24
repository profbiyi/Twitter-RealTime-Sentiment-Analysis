from kafka import KafkaConsumer
from datetime import datetime
import json
import requests
import re
from textblob import TextBlob
import preprocessor as p
import psycopg2
from psycopg2.extras import execute_values
from psycopg2.extensions import register_adapter

register_adapter(dict, json)


connection = psycopg2.connect(user = "twitter_user",
    password = "user123",
    host = "localhost",
    port = "1234",
    database =  "tweet_db")

cursor = connection.cursor()


consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'],value_deserializer=lambda m: json.loads(m.decode('utf-8')))


for message in consumer:
    tweet = message.value

    p.set_options(p.OPT.URL, p.OPT.EMOJI) #fully customise preprocessor to clean text

    clean_tweet =  p.clean(str(tweet['text'].encode('utf-8')))
    tweet_polarity = TextBlob(clean_tweet).sentiment.polarity



    tweets = [{
                    'created_at': datetime.strftime(datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S'),
                    'id' : str(tweet['id_str']),
                    'text' : str(tweet['text'].encode('utf-8')),
                    'clean_text' : clean_tweet,
                    'tweet_polarity' : tweet_polarity,
                    'cordinates':  tweet['coordinates'],
                    'user_created' : datetime.strftime(datetime.strptime(tweet['user']['created_at'],'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S'),
                    'description' : str(tweet['user']['description']),
                    'name' : str(tweet['user']['screen_name']),
                    'location' : str(tweet['user']['location']),
                    'followers_count' : tweet['user']['followers_count'],
                    'retweet_count': tweet['retweet_count'],
                    'background_color' : str(tweet['user']['profile_background_color'])
                    }]

    

    columns = tweets[0].keys()
    query = "INSERT INTO twitter_data ({}) VALUES %s".format(','.join(columns))

    # convert projects values to sequence of seqeences
    values = [[value for value in tweet.values()] for tweet in tweets]
    execute_values(cursor, query, values)
    connection.commit()
    
    
    
    
    
    data_json = json.dumps(tweets, indent = 4) 
    print(data_json)
    print()
