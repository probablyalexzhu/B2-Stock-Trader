import tweepy
from configparser import ConfigParser 
import os
import pandas as pd


config = ConfigParser()

#read configs API key with configparser
config.read('Twitter Scraper\config.ini')
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#authentication
auth = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret = api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


choice = input("enter the hashtag: ")

tweets = tweepy.Cursor(api.search_tweets, q = choice).items(100)

for tweet in tweets:
    print(tweet.text)
    print("\n")