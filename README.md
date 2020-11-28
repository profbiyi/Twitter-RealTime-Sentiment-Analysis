# Twitter Sentiment Analysis for Brand Improvement
This project is designed to pull real data from twitter and perform sentiment analysis on the same, also it is expected to store the tweets and do a batch analysis.

This project is designed for brand improvement. It affords a firm/company etc to track mentions and trends on the twitter space, and use the details to get an idea of the general public's view of their company, business and/or firm. It is also designed to 


Sentiment analysis will be performed on realtime tweets, the tweet and results visualised.  At the same time, the same tweets are stored in batches and then analysed.



 ## Project Structure

 ```

├───.circleci
├           └─── config.yml
├───src
├     └─── appy.py
├     └─── test.py
├     └─── README.md
├     └─── images
├               └─── post.PNG
├               └─── post2.PNG
├               └─── get_1.PNG
├               └─── get_all.PNG
├
├───docker_docker_compose
├                        └─── Dockerfile
├                        └─── docker-compose.yml
├
├───k8s
├    └─── flask_k8_service.yml
├    └─── flask-api-deployment.yml
├    └─── minikube_start.PNG
├    └─── minikube_status.PNG
├
├───istio
├
├───gitignore
├───gitattributes
├───Procfile
├───README.md
├───requirements.txt
└───runtime

 ```
 
 
## Tools, Technology and Architecture


<img width="900" alt="architecture" src="https://user-images.githubusercontent.com/21452793/91578421-0d641e80-e942-11ea-948e-d3f1de54dc52.PNG">


### 1. Tweepy
Tweepy is the official python api for twitter. It allows for streams and batch harvesting of tweets. A twitter developer account is needed to use this awesome API. To have acces to the necessary keys for twitter api, a user is expected to apply for an account [here](https://developer.twitter.com/en/apply-for-access).

Tweey [documentation](http://docs.tweepy.org/en/latest/)


### 2. Apache Kakfa
Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications. Read more about Kafka (here)[https://kafka.apache.org]



### 3. PostgreSQL
Stores the processed data and allow for other form of batch usage.



### 4. PowerBI
Displays and visualise the data from apache spark in real time. Also, does same for the data in postgreSQL, but this time as a batch display and visualization.



## Usage
- clone the repository
- cd to the containerisation directory and run `docker-compose up` or 'docker-compose up -d` to run in silent mode. This will set up Kafka and Kafdrop.
- goto `localhost:9000` to launch kafdrop web UI. create a broker using the UI
- create a virtual environment 
- run `pip install -r requirements.txt`
- connect to the your postgres database and create the table using the script in `create_table.sql
- then run `python app.py` to start the flask application.
- navigate to `localhost:5000` and start streaming and view results from the dashboards.



## TODO:
- change the technology/tools for the consumer to apache spark
- send realtime email to alert users
- combine ML model with the result of Textblob
- add login page to the flask application
- containerise the whole application, as some services are set up with docker compose while the others are hosted on ec2.
- ....

