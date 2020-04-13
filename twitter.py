from dotenv import load_dotenv
# loads environment variables from a .gitignore'd .env file
load_dotenv()

import os
import requests
from requests_oauthlib import OAuth1
import json

key = os.getenv('TWITTER_KEY')
key_secret = os.getenv('TWITTER_KEY_SECRET')
token = os.getenv('TWITTER_TOKEN')
token_secret = os.getenv('TWITTER_TOKEN_SECRET')

class Twitter:

    def tweet(msg):
        base_uri = 'https://api.twitter.com/1.1/'
        tweet_url = base_uri + 'statuses/update.json'

        auth = OAuth1(key, key_secret, token, token_secret)

        data = {'status': msg}

        resp = requests.post(tweet_url, data=data, auth=auth)
        print(resp.text)


