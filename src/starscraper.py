import csv
import html
import os
import tweepy

consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

results = api.search(q="astronomy", lang="en", count=100)

with open("sample.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "handle", "name", "text"])
    for tweet in results:
        writer.writerow([tweet.created_at, tweet.user.screen_name, tweet.user.name, html.unescape(tweet.text)])
