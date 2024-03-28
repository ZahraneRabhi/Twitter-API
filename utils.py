from requests import get
from models.Tweet import Tweet


def fetch_tweets(bearer_token, keyword):
    """
    fetching tweets from a given twitter account (must be adminsitered by you ) .
    Args:
        bearer_token (str): your Twitter Private API bearer toke (must be kept secret).
        keyword (str): your keyword criteria to fetch tweets
    """
    tweet_fields = "tweet.fields=lang,author_id,created_at"
    query = f"query={keyword}"
    url = f"https://api.twitter.com/2/tweets/search/recent?{query}&{tweet_fields}"

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "User-Agent": "v2TweetLookupPython"
    }

    response = get(url, headers=headers)
    if response.status_code == 200:
        twitter_data = response.json()

        if 'data' in twitter_data:
            tweets_data = []
            data = twitter_data['data']

            for tweet_data in data:
                tweet = Tweet(tweet_data)
                print(tweet)

                tweets_data.append({
                    'comment_id': tweet.comment_id, 
                    'comment_text': tweet.review_text,
                    'comment_date': tweet.tweet_date,
                    'tweet_author': tweet.tweet_author,
                    'platform': tweet.platform
                    })
                
    return tweets_data
