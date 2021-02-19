import time
from datetime import datetime
import logging

import pymongo
from faker import Faker

# Create a connection to the MongoDB database server
client = pymongo.MongoClient('mongodb') # hostname = service name for docker-compose pipeline

# Create/use a database


# Define the collection


fake = Faker()
while True:
    # What we actually want to do is to insert the tweet into MongoDB
    text = fake.text()
    tweet = {'username': fake.name(), 'text': text}
    # Insert the tweet into the collection

    logging.critical('-----Tweet written into MongoDB-----')
    logging.critical(text)
    logging.critical(str(datetime.now()))
    logging.critical('----------\n')

    time.sleep(3)