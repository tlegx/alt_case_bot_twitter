# alt_case_bot_twitter
<p>
  <img alt="AppVeyor" src="https://img.shields.io/badge/Status-Unstable-informational?color=orange">
  <img alt="AppVeyor" src="https://img.shields.io/badge/Language-Python-informational?color=blue">
  <img alt="AppVeyor" src="https://img.shields.io/badge/Version-v0.0.0 alpha-informational?color=orange">
</p>

A Twitter bot that creates an alternative case version of the tweet you're replying to
## How it works
Every 20 seconds, check for mentions in mentions_timeline. If found, reply to the user who mentioned the bot with an alternative case version of the tweet they are replying to
## Using the bot
***WARNING: THIS PROGRAM IS IN AN ALPHA STATE AND IS NOT INTENDED FOR PUBLIC USE YET. ONLY USE THIS PROGRAM IF YOU KNOW WHAT YOU ARE DOING. YOU HAVE BEEN WARNED***

**Make sure you have installed the *Python interpreter* and had a [Twitter developer account](https://developers.twitter.com) before continuing**

***Do this first:*** Open [config.py](https://github.com/tlegx/alt_case_bot_twitter/blob/master/config.py) and replace the "consumer_key", "consumer_secret", "access_token" and "access_token_secret" string data to your own.
Navigate to the directory you downloaded this and simply type:
```
python main.py
```
into your terminal. The bot will automatically authenticates to Twitter using the "consumer_key", "consumer_secret", "access_token" and "access_token_secret" that you given earlier.
## Feedbacks and Contributions
As mentioned above, this program is very unstable so any feedback and contributions is welcomed.
## Acknowledgements
[The Tweepy Project](https://github.com/tweepy/tweepy)
## License
MIT License</br>
Copyright (c) 2021 tlegx</br>
For more information, please see [LICENSE](https://github.com/tlegx/alt_case_bot_twitter/blob/master/LICENSE)
