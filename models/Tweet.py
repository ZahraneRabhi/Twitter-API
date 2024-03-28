#from datetime import strftime


class Tweet:
    def __init__(self, tweet_data):
        self.platform = "twitter"
        self.review_text = tweet_data.get('text', '')
        self.comment_id = tweet_data.get('id', '')
        #self.tweet_date = strptime(tweet_data.get('created_at', ''), '%a %b %d %H:%M:%S %z %Y').strftime('%d/%m/%Y')
        self.tweet_author = tweet_data.get('author_id', '')

    def __str__(self):
        return f'''Platform: {self.platform}\n
                    Review Text: {self.review_text}\n
                    Comment ID: {self.comment_id}\n
                    Tweet Date: {self.tweet_date}\n
                    Tweet Author: {self.tweet_author}'''


