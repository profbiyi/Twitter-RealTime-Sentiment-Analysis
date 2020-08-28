# DSTI Python Project 


## Realtme Sentiment and Batch Analysis of Tweets
This project is designed to pull real data from twitter and perform sentiment analysis on the same, also it is expected to store the tweets and do a batch analysis. 


Sentiment analysis will be performed on realtime tweets, the tweet and results visualised.  At the same time, the same tweets are stored in batches and then analysed.


## Tools, Technology and Architecture
#### 1. Tweepy
        For this project, tweepy streams data in realtime from twitter and send to Apache Kakfa.
        
#### 2. Apache Kakfa
        Apache Kafka is an open source software which provides a framework for storing, reading and 
        analysing streaming data. Kafka accepts the streaming tweets (using KafkaPRoducer) from tweepy, 
        and also send them out through the KakfaConsumer
        
#### 3. Apache Spark (Pyspark)
        Apache Spark, wih its streaming capability consumes the data from Kafka using the KafkaConsumer (in realtime), 
        cleanse, process, analyse and send to power BI in realtime, and also batch-stores in a database for other 
        forms of batch analysis. Here the sentiment analysis is carried out
        
#### 4. PostgreSQL
        Stores the processed data and allow for other form of batch usage.

#### 5. PowerBI
        Displays and visualise the data from apache spark in real time. Also, does same for the data in postgreSQL, 
        but this time as a batch display and visualization.
      


