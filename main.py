import tweepy
from config import create_api
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions, please wait...")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is None:
            api.update_status(status="@" + tweet.user.screen_name + " Tweet ID: " + tweet.id + " Alternative Case Bot Error 01: This bot does not support mentioning straight from a tweet. For more information, visit: https://tlegx.rf.gd", in_reply_to_status_id=tweet.id)
        else:
            if any(keyword in tweet.text.lower() for keyword in keywords):
                og_tweet_id = tweet.in_reply_to_status_id
                og_tweet_content = api.get_status(og_tweet_id)
                altcase_tweet_content = altcase(str(og_tweet_content.text))
                logger.info(f"Original content: {og_tweet_content.text}, AltCase content: {altcase_tweet_content}")
                logger.info(f"Answering to {tweet.user.name}, username {tweet.user.screen_name}")
                api.update_status(status=altcase_tweet_content + "---@/" + tweet.in_reply_to_screen_name, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                logger.info(f"Replied to {tweet.user.name}, username {tweet.user.screen_name}, original tweet id " + str(tweet.id))
    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["test", "testing"], since_id)
        countdown(int(20))

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}'.format(secs)
        print("Waiting to fetch, " + timer + " seconds remaining...", end="\r")
        time.sleep(1)
        t -= 1

def altcase(string):
    res = ''
    for idx in range(len(string)):
        if not idx % 2:
            res += string[idx].upper()
        else:
            res += string[idx].lower()
    return res

if __name__ == "__main__":
    main()