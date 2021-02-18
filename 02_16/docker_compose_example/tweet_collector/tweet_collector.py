import time
import os
from datetime import datetime
import logging
import random

import pymongo
from faker import Faker

# Create a connection to the MongoDB database server
client = pymongo.MongoClient(host='mongodb') # hostname = servicename for docker-compose pipeline

# Create/use a database
db = client.tweets
#equivalent of CREATE DATABASE tweets;

# Define the collection
collection = db.tweet_data
#equivalent of CREATE TABLE tweet_data;

fake = Faker()
while True:
    # What we actually want to do is to insert the tweet into MongoDB
    text = fake.text()
    tweet = {'username': fake.name(), 'text': text, 'data': random.randint(0, 10)}
    # Insert the tweet into the collection

    logging.critical('-----Tweet written into MongoDB-----')
    collection.insert(tweet) #equivalent of INSERT INTO tweet_data VALUES (....);
    logging.critical(str(datetime.now()))
    logging.critical('----------\n')

    time.sleep(3)