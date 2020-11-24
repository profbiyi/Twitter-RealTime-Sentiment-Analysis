from kafka import KafkaConsumer
from datetime import datetime
import json
import requests
import re
from textblob import TextBlob
import preprocessor as p
import psycopg2


connection = psycopg2.connect(user = "postgres",
    password = "2591",
    host = "localhost",
    port = "5432",
    database =  "test")

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

    data_json = json.dumps(tweets, indent = 4)   
    print(data_json)
    print()
    #print(type(data_json)


    #REST_API_URL = "https://api.powerbi.com/beta/983fd5a7-4101-47a8-9e55-46815a6ed49d/datasets/c3d5b1af-95ba-4625-881c-0cf77776981f/rows?key=Airq7p9FdX%2FazL5FcOs5UYsQ4V8P%2FM50LzaS7Zioa4CjamvEbAE5Uh2q%2FJuwYCLhwZ1E0qqiS%2FENIMyqJOaLaQ%3D%3D"
    #req = requests.post(REST_API_URL, data_json)
    #print(req)

