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

        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    with open("config.yml", 'r') as config_file:
        CONFIG = yaml.load(config_file)

    CONSUMER_KEY = CONFIG['twitter_api']['consumer_key']
    CONSUMER_SECRET = CONFIG['twitter_api']['consumer_secret']
    ACCESS_TOKEN = CONFIG['twitter_api']['access_token']
    ACCESS_TOKEN_SECRET = CONFIG['twitter_api']['access_token_secret']

    LISTERNER = StdOutListener()
    AUTH = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    TOPICS = (CONFIG['topics']['bitcoin'])
    LANGUAGES = (CONFIG['languages'])

    STREAM = Stream(AUTH, LISTERNER)
    STREAM.filter(track=TOPICS, languages=LANGUAGES)
