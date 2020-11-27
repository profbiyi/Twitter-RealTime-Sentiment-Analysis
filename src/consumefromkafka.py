from kafka import KafkaConsumer
from datetime import datetime
import json
import requests
import re
import apiConfig
from textblob import TextBlob
import preprocessor as p
import psycopg2
from psycopg2.extras import execute_values
from psycopg2.extensions import register_adapter
import time
from cleantext import clean

register_adapter(dict, json)


connection = psycopg2.connect(user = apiConfig.user,
    password = apiConfig.password,
    host = apiConfig.host,
    port = apiConfig.port,
    database = apiConfig.database)

cursor = connection.cursor()


consumer = KafkaConsumer('test', bootstrap_servers=['157.245.210.30:9092'],value_deserializer=lambda m: json.loads(m.decode('utf-8')))



def getTextSubjectivity(txt):
    return TextBlob(txt).sentiment.subjectivity

def getTextPolarity(txt):
    return TextBlob(txt).sentiment.polarity


for message in consumer:
    tweet = message.value

    p.set_options(p.OPT.URL, p.OPT.EMOJI) #fully customise preprocessor to clean text

    clean_tweet =  clean((tweet['text']))
    tweet_polarity = getTextPolarity(clean_tweet)
    tweet_subjectivity = getTextSubjectivity(clean_tweet)

    tweets = [{
                    'created_at': datetime.strftime(datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S'),
                    'id' : str(tweet['id_str']),
                    'text' : str(tweet['text'].encode('utf-8')),
                    'clean_text' : clean_tweet,
                    'tweet_polarity' : tweet_polarity,
                    'tweet_subjectivity': tweet_subjectivity,
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


    ##send live data to powerbi
    REST_API_URL = "https://api.powerbi.com/beta/983fd5a7-4101-47a8-9e55-46815a6ed49d/datasets/47ccc959-38c0-4e4f-8669-8b178a15b74b/rows?key=83mUyYnPePd7ggyFUH%2Fqk2U9Zy87o1Oqf4eu9hLH1j1Wz1nZwh%2FtHfHAhQsEbyeDZdP%2B708onQVJAldGiSwKSg%3D%3D"
    req = requests.post(REST_API_URL, data_json)
    print(req)