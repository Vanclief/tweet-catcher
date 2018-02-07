import json
import yaml

from tweepy.streaming import StreamListener
from tweepy import Stream


class Client(object):

    def __init__(self, auth, db_client, topic):

        self.auth = auth
        self.db_client = db_client
        self.topic = topic

        with open("config.yml", 'r') as config_file:
            config = yaml.load(config_file)

        # Get query parameters
        self.languages = config['languages']
        self.keywords = config['topics'][topic]

    def run(self):
        listener = StdOutListener(self.db_client, self.topic)

        stream = Stream(self.auth, listener)
        stream.filter(track=self.keywords, languages=self.languages)


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, db_client, topic):
        self.db_client = db_client
        self.topic = topic

    def on_data(self, data):

        t = json.loads(data)

        tweet = [{
            "measurement": self.topic,
            "tags": {
                'username': t['user']['screen_name'],
            },
            "fields": {
                'id': t['id_str'],
                'followers_count': t['user']['followers_count'],
                'text': t['text'],
                'hashtags': str(t['entities']['hashtags']),
                'created_at': t['created_at'],
                'language': t['lang']
            }
            }]

        self.db_client.write_points(tweet)

        return True

    def on_error(self, status):
        print(status)
