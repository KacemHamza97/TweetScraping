import tweepy
from tweepy import OAuthHandler
from time import sleep
from notify_run import Notify
import json


class Tweet:
    def __init__(self, id, text):
        self.id = id
        self.text = text


notify = Notify()
ACCESS_TOKEN = "241949174-J7mlaEePXSl59Ee7SUSWxJ7UX1pIunz6dTck9IaK"
ACCESS_TOKEN_SECRET = "KPGs3ZZBcSXRzwxNNOu1vSs0wxdTXPYmjb80O06AwhTmv"
CONSUMER_KEY = "SSip5qurDw27uvKcDbUZlp7Ub"
CONSUMER_SECRET = "gis20uRU4KJ4fpCHZrwYVSxl16DWsppC9dlMgLATYzOE0HYJBC"
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
print("waiting")
api = tweepy.API(auth, wait_on_rate_limit=True) #wait_on_rate_limit=True
print("done")
tweets = set()
while 1:
    print("looking")
    for status in tweepy.Cursor(api.home_timeline).items(5):
        tweet = Tweet(status._json["id"], status._json["text"])
        print(tweet.text)
        if tweet.text not in tweets:
            tweets.add(tweet.text)


    #         notify.send(tweet.text)
    sleep(300)
