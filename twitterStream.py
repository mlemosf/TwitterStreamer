from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from time import sleep
from json import loads
import twitter_credentials
import sys

class TwitterStreamer():
    def stream_tweets(self, fetched_tweets_filename,hashtag_list):
        # isso conecta ao serviço de stream do Twitter e salva os tweets em arquivo
        listener = StdoutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)
        stream.filter(track=hashtag_list)



class StdoutListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        color_bold = '\033[1m'
        color_end = '\033[0m'
        counter = 0
        try:
            data = loads(data)
            formated = color_bold+data['user']['name'] +color_end+" says '"+data['text']+"'"
            print(formated)
            sleep(5)
            data = ""
        except Exception as err:
            print(str(err))
        return True

    def on_error(self, status):
        print(status)



if __name__ == '__main__':
    hashtag_list = sys.argv[1:]
    print(hashtag_list)
    fetched_tweets_filename = "tweets.json"
    twiterStreamer = TwitterStreamer()
    twiterStreamer.stream_tweets(fetched_tweets_filename, hashtag_list)
