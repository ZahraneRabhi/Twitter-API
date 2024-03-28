from utils import fetch_tweets
from config import TWITTER_BEARER_TOKEN, TWITTER_KEYWORD


fetch_tweets(TWITTER_BEARER_TOKEN, keyword=TWITTER_KEYWORD)
