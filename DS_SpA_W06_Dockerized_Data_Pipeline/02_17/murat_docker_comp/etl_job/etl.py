
import pymongo
from sqlalchemy import create_engine
import time

time.sleep(10)  #

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb")

# Select the database you want to use withing the MongoDB server
db = client.tweets_db

# Select the collection of documents you want to use withing the MongoDB database
collection = db.tweets

entries = collection.find()
for e in entries:
    print(e)

# Apply sentiment analysis

# Send it to postgres

pg = create_engine('postgres://postgres:postgres@postgresdb:5432/twitter_stream', echo=True)


pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

for e in entries:
    text = e['text']
    score = 1.0  # placeholder value
    query = "INSERT INTO tweets VALUES (%s, %s);"
    pg.execute(query, (text, score))