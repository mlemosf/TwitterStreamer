from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from time import sleep
from json import loads
import twitter_credentials

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
        counter = 0
        try:
            d = loads(data)
            formated = "+"+d['user']['name'] +"+ says '"+d['text']+"'"
            print(formated)
            sleep(10)
        except Exception as err:
            print(str(err))
        return True

    def on_error(self, status):
        print(status)



if __name__ == '__main__':
    hashtag_list = ['Elon Musk','SpaceX', 'Blockchain','Bitcoin', 'Ethereum','Iota']
    fetched_tweets_filename = "tweets.json"
    twiterStreamer = TwitterStreamer()
    twiterStreamer.stream_tweets(fetched_tweets_filename, hashtag_list)
