# Copyright (c) tlegx 2021
# This software has no warranty, use at your own risk!

# Imports
import tweepy
from config import create_api
import logging
import time

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions, please wait...")
    new_since_id = since_id
    # Retrieve tweets in mentions_timeline
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        # If the user mentioned the bot in a tweet (not a reply) the bot responds with an error
        if tweet.in_reply_to_status_id is None:
            api.update_status(
                status="@" + tweet.user.screen_name + " Tweet ID: " + str(tweet.id) + ". Alternative Case Bot Error 01: This bot does not support mentioning straight from a tweet. For more information, visit: https://tlegx.rf.gd",
                in_reply_to_status_id=tweet.id)
        # If the user mentioned the bot in a reply, convert og_tweet_content to alternative case, then reply to the user who mentioned the bot earlier
        else:
            if any(keyword in tweet.text.lower() for keyword in keywords):
                og_tweet_id = tweet.in_reply_to_status_id
                og_tweet_meta = api.get_status(og_tweet_id)
                og_tweet_content = str(og_tweet_meta.text)
                # If og_tweet_content is longer than 260 characters then truncate to prevent from exceeding Twitter's character limit
                if len(str(og_tweet_content)) > 260:
                    og_tweet_content = truncate(og_tweet_content)
		# If the user attempts to 'alt_case' the author, the bot responds with an error (optional)
                if str(tweet.in_reply_to_screen_name) == "tlegx_" or "alt_case":
                    api.update_status(status="Tweet ID: " + str(tweet.id) + ". Alternative Case Bot Error 02: You cannot make the author of this bot feel the pain. + tweet.in_reply_to_screen_name,
                                      in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                else:
                    altcase_tweet_content = altcase(og_tweet_content)
                    logger.info(f"Original content: {og_tweet_content}, AltCase content: {altcase_tweet_content}")
                    logger.info(f"Answering to {tweet.user.name}, username {tweet.user.screen_name}")
                    api.update_status(status=altcase_tweet_content + "-@/" + tweet.in_reply_to_screen_name,
                                  in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                    logger.info(
                        f"Replied to {tweet.user.name}, username {tweet.user.screen_name}, original tweet id " + str(
                            tweet.id))
    return new_since_id


def main():
    # Authenticates to Twitter and check for replies containing "test" and "testing" every 20 seconds
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["test", "testing"], since_id)
        countdown(int(20))


def countdown(t):
    # Countdown
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}'.format(secs)
        print("Waiting to fetch, " + timer + " seconds remaining...", end="\r")
        time.sleep(1)
        t -= 1


def altcase(string):
    # Method to convert og_tweet_content to alternative case
    res = ''
    for idx in range(len(string)):
        if not idx % 2:
            res += string[idx].upper()
        else:
            res += string[idx].lower()
    return res

def truncate(string):
    # Limit og_tweet_content to 260 characters
    shortstring = string[:260] + '...'
    return shortstring

if __name__ == "__main__":
    main()
