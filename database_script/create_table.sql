CREATE TABLE twitter_data
(
created_at TIMESTAMP,
id VARCHAR ( 50 ),
text VARCHAR ( 500 ),
clean_text VARCHAR ( 500 ),
tweet_polarity INT,
cordinates VARCHAR(20), 
user_created TIMESTAMP,
description VARCHAR ( 500 ),
name VARCHAR ( 500 ),
location VARCHAR ( 100 ),
followers_count INT,
retweet_count INT,
background_color VARCHAR(50)
)
;

ALTER TABLE twitter_data OWNER to twitter_user;