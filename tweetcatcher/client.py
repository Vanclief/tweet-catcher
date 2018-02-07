import json
import yaml
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):

        t = json.loads(data)

        tweet = {
                'id': t['id_str'],
                'username': t['user']['screen_name'],
                'followers_count': t['user']['followers_count'],
                'text': t['text'],
                'hashtags': t['entities']['hashtags'],
                'created_at': t['created_at'],
                'language': t['lang']
                }

        print(tweet['text'])
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    with open("config.yml", 'r') as config_file:
        config = yaml.load(config_file)

    consumer_key = config['twitter_api']['consumer_key']
    consumer_secret = config['twitter_api']['consumer_secret']
    access_token = config['twitter_api']['access_token']
    access_token_secret = config['twitter_api']['access_token_secret']

    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    topics = (config['topics']['bitcoin'])
    languages = (config['languages'])

    stream = Stream(auth, listener)
    stream.filter(track=topics, languages=languages)
