from TwitterAPI import TwitterAPI
from configparser import ConfigParser

config = ConfigParser()
config.read("old_place.config")

CONSUMER_KEY = config['twitter']['CONSUMER_KEY']
CONSUMER_SECRET = config['twitter']['CONSUMER_SECRET']
ACCESS_TOKEN_KEY = config['twitter']['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = config['twitter']['ACCESS_TOKEN_SECRET']

def send(status_msg):
    TWEET_TEXT = "@koonktech " + status_msg

    api = TwitterAPI(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN_KEY,
        ACCESS_TOKEN_SECRET
    )
    api.request('statuses/update', {'status': TWEET_TEXT})