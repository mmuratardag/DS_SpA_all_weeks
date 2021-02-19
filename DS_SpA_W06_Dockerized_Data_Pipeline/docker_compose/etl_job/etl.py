
import pymongo
from sqlalchemy import create_engine
import time

time.sleep(10)  #

while True:

    client = pymongo.MongoClient(host="mongodb", port=27017)
    db = client.tweets
    collection = db.tweet_data
    entries = collection.find()


    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    s  = SentimentIntensityAnalyzer()


    pg = create_engine('postgres://postgres:postgres@postgresdb:5432/twitter_stream', echo=True)

    pg.execute('''
        CREATE TABLE IF NOT EXISTS tweets (
        id VARCHAR(100),
        text VARCHAR(1000),
        sentiment NUMERIC
    );
    ''')


    for e in entries:
        print(e)
        id = e['id']
        #moment = e['tweet_created_at']
        text = e['text']
        sentiment = s.polarity_scores(e['text'])
        score = sentiment['compound']
        query = "INSERT INTO tweets VALUES (%s, %s, %s);"
        pg.execute(query, (id, text, score))

    time.sleep(10)

