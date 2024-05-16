from tweet_utils import fetch_tweets
from config import TWITTER_BEARER_TOKEN, TWITTER_KEYWORD

# Use this to fetch tweets based on a specified keyword(hashtag, name, trend...)
fetch_tweets(TWITTER_BEARER_TOKEN, keyword=TWITTER_KEYWORD)
