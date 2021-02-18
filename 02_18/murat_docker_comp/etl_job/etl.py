
import pymongo
from sqlalchemy import create_engine
import time

time.sleep(10)  #

client = pymongo.MongoClient(host="mongodb", port=27017)
db = client.tweets
collection = db.tweet_data
entries = collection.find()


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
s  = SentimentIntensityAnalyzer()


pg = create_engine('postgres://postgres:postgres@postgresdb:5432/twitter_stream', echo=True)

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

for e in entries:
    print(e)
    text = e['text']
    sentiment = s.polarity_scores(e['text'])
    score = sentiment['compound']
    query = "INSERT INTO tweets VALUES (%s, %s);"
    pg.execute(query, (text, score))


# psql -U postgres -h 0.0.0.0 -p 5555 twitter_stream
# SELECT text FROM tweets LIMIT 20;
# SELECT sentiment FROM tweets LIMIT 20;
