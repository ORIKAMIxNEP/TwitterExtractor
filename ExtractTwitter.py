import os
import random

import tweepy
from dotenv import load_dotenv

load_dotenv()


def ExtractTwitter(text):
    BEARER_TOKEN = os.getenv("BEARER_TOKEN")
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
    client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET,
                           ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    searchText = text
    next_token = ""
    allTweetsCount = 0
    extractedTweetsCount = 0
    TweetsData = {"tweets": []}
    for i in range(5):
        if i == 0:
            tweets = client.search_recent_tweets(
                query=searchText, max_results=100, tweet_fields=["entities", "lang", "public_metrics"])
        else:
            tweets = client.search_recent_tweets(
                query=searchText, max_results=100, next_token=next_token, tweet_fields=["entities", "lang", "public_metrics"])
        for tweet in tweets.data:
            if tweet.lang == "ja" and (tweet.entities is None or ("mentions" not in tweet.entities and "urls" not in tweet.entities)):
                print("-------------------------------------------")
                print(tweet.text)
                print("favorite:" + str(tweet.public_metrics["like_count"]))
                TweetsData["tweets"].append(
                    dict({"tweet": tweet.text, "favorite": tweet.public_metrics["like_count"]}))
                extractedTweetsCount += 1
            allTweetsCount += 1
        if "next_token" not in tweets.meta:
            break
        else:
            next_token = tweets.meta["next_token"]

    # for i in range(100):
    #     TweetsData["tweets"].append(
    #         dict({"tweet": "テストツイート"+str(i+1), "favorite": random.randint(0, 1000)}))

    print("----------------------------------------")
    print("AllTweet:" + str(allTweetsCount))
    print("ExtractedTweet:" + str(extractedTweetsCount))
    print(TweetsData)
    return TweetsData
