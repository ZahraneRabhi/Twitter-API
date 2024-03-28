from os import getenv
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Database Credentials
SERVER_NAME = getenv("SERVER_NAME")
DATABASE_NAME = getenv("DATABASE_NAME")

# Twitter Credentials
TWITTER_API_KEY = getenv("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = getenv("TWITTER_API_SECRET_KEY")
TWITTER_ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = getenv("TWITTER_ACCESS_TOKEN_SECRET")
TWITTER_USERNAME = getenv("TWITTER_USERNAME")
TWITTER_BEARER_TOKEN = getenv("TWITTER_BEARER_TOKEN")

# Tweet Criterias
TWITTER_HASHTAG = '#'
TWITTER_KEYWORD = 'Playboi Carti'





