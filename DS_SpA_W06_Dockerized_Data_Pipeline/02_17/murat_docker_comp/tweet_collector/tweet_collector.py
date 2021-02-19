import os
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import json
import logging
import pymongo

API_KEY =  os.getenv('TWT_API_KEY')            
API_SECRET =  os.getenv('TWT_API_SECRET')          
ACCESS_TOKEN =  os.getenv('TWT_ACCESS_TOKEN')        
ACCESS_TOKEN_SECRET =  os.getenv('TWT_ACCESS_TOKEN_SECRET')

client = pymongo.MongoClient("mongodb", port=27017)
db = client.tweets
collection = db.tweet_data

def authenticate():
    """
    """
    auth = OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return auth

class TwitterListener(StreamListener):

    def on_data(self, data):

        t = json.loads(data) #t is just a regular python dictionary.

        if 'extended_tweet' in t:
            text = t['extended_tweet']['full_text']
        else:
            text = t['text']

        tweet = {
        'text': t['text'],
        'username': t['user']['screen_name'],
        #'followers_count': t['user']['followers_count']
        }

        logging.critical(f'\n\n\nTWEET INCOMING: {tweet["text"]}\n\n\n')


    def on_error(self, status):

        if status == 420:
            print(status)
            return False

if __name__ == '__main__':

    auth = authenticate()
    listener = TwitterListener()
    stream = Stream(auth, listener)
    stream.filter(track=['politics'], languages=['en'])
