import os
import time
import slack
from sqlalchemy import create_engine
import logging
import requests
import pandas as pd


WEBHOOK_URL =  os.getenv('WEBHOOK_URL')

time.sleep(15)

pg = create_engine('postgres://postgres:postgres@postgresdb:5432/twitter_stream', echo=True)

query = """SELECT DISTINCT ON (id) id, text, sentiment FROM tweets WHERE id = (SELECT MAX(id) FROM TWEETS) ORDER BY id DESC"""

time.sleep(15)

while True:

    tweet = pd.read_sql_query(query, con=pg)
    logging.warning('Pandas makes the PG, query =  \n {}'.format(tweet))
    
    text = tweet['text'].iloc[0]

    sentiment =  tweet['sentiment'].iloc[0]
    
    output = f'Here is a random anonymous bullshit tweet about politics ::: {text}; \n\n\nThe sentiment score for this tweet is: {sentiment}'
    data = {'text': output}
    requests.post(url=WEBHOOK_URL, json=data)

    time.sleep(120)