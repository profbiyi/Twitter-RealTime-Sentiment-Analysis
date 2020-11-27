import tweepy
import json
import sqlite3
import apiConfig
import requests
from datetime import datetime
import pandas as pd
import os

from kafka import KafkaProducer

# Twitter authentication stuff
global api
# API keys are stored in a separate file
access_token = apiConfig.access_token
access_token_secret = apiConfig.access_token_secret
consumer_key = apiConfig.consumer_key
consumer_secret = apiConfig.consumer_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#api = tweepy.API(auth)
#api = tweepy.API(auth, wait_on_rate_limit=True)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


#local system
#producer = KafkaProducer(bootstrap_servers='192.168.99.100:9092')   
producer = KafkaProducer(bootstrap_servers='157.245.210.30:9092')
topic_name = 'test'



# Stream Listener class
class TweetStreamListener(tweepy.StreamListener):

    # When data is received
    def on_data(self, data):

        # Error handling because teachers say to do this
        try:

            # Make it JSON
            tweet = json.loads(data)
            # producer.send(topic_name, str.encode(data))
            # print(data)
        

            # # filter out retweets
            if not tweet['retweeted'] and 'RT @' not in tweet['text']:

                producer.send(topic_name, str.encode(data))
                print(data)

        # Let me know if something bad happens            
        except Exception as e:
            print(e)
            pass
        
        producer.flush()
        # return True

def twitter_keywords(keywords: list):
    listener = TweetStreamListener()
    stream = tweepy.Stream(auth, listener)
    # # Filter the stream for these keywords. Add whatever you want here! 
    # stream.filter(languages=["en"], track=['EndSarsNow',], is_async=True)

    try:
        print('Start streaming... ')
        stream.filter(languages=["en"], track=keywords, is_async=True)
    except KeyboardInterrupt as e :
        print("Stopped.")
    return stream 


# Driver
if __name__ == '__main__':
   import sys
   keywords = sys.argv[1:] # grab keywords from cmd

    # keywords not passed
   if len(keywords) < 1:
       raise SystemExit('Error: No keyword was passed!')
   twitter_keywords(keywords)
