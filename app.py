from threading import Thread
from time import sleep

from db_utils import add_comment_to_sql_server
from tweet_utils import fetch_tweets
from config import *

#
def background_task():
    """
    Continuously fetches tweets from Twitter and adds them to an SQL Server database.
    """
    latest_twitter_comments = fetch_tweets(TWITTER_BEARER_TOKEN, keyword=TWITTER_KEYWORD)

    while(True):
        new_twitter_comments = fetch_tweets(TWITTER_BEARER_TOKEN, keyword=TWITTER_KEYWORD)
        verify_new_twitter = (new_twitter_comments and new_twitter_comments != latest_twitter_comments)

        
        if (verify_new_twitter):
            print("New Tweet Reviews Detected!")

            difference = [comment for comment in new_twitter_comments if comment not in latest_twitter_comments]

            for new_comment in difference:
                print(f"New review: {new_comment}") # you can delete it, usefull to monitor the tweet fetching flow tho
                add_comment_to_sql_server(SERVER_NAME, DATABASE_NAME, new_comment)
            latest_twitter_comments = new_twitter_comments
        sleep(10)


if __name__ == "__main__":
    initial_twitter_comments = fetch_tweets(TWITTER_BEARER_TOKEN, keyword=TWITTER_KEYWORD)   

    for twitter_comments in initial_twitter_comments:
        print(twitter_comments)
        add_comment_to_sql_server(SERVER_NAME, DATABASE_NAME, twitter_comments )
        print()
        
    bg_thread = Thread(target = background_task)
    bg_thread.start()