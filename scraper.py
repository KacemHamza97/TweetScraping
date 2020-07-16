# from pprint import pprint
import tweepy
from tweepy import OAuthHandler
from time import sleep
from notify_run import Notify
from googletrans import Translator


class Tweet:
    def __init__(self, id, text):
        self.id = id
        self.text = text


translator = Translator()
notify = Notify()
a = notify.register()
print(a)
ACCESS_TOKEN = "241949174-J7mlaEePXSl59Ee7SUSWxJ7UX1pIunz6dTck9IaK"
ACCESS_TOKEN_SECRET = "KPGs3ZZBcSXRzwxNNOu1vSs0wxdTXPYmjb80O06AwhTmv"
CONSUMER_KEY = "SSip5qurDw27uvKcDbUZlp7Ub"
CONSUMER_SECRET = "gis20uRU4KJ4fpCHZrwYVSxl16DWsppC9dlMgLATYzOE0HYJBC"
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)  # wait_on_rate_limit=True
tweets = set()
while 1:
    for status in tweepy.Cursor(api.home_timeline, include_entities=True).items(50):
        tweet = Tweet(status._json["id"], status._json["text"])
        if tweet.text not in tweets:
            tweets.add(tweet.text)
            translation = translator.translate(tweet.text, dest='en')
            print(translation.text)
            # notify.send(tweet.text)
        sleep(60)
