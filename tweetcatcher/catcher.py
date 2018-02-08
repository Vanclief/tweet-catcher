import yaml
from influxdb import InfluxDBClient
from tweetcatcher.client import Client
from tweepy import OAuthHandler


class Catcher(object):

    def __init__(self):
        with open("config.yml", 'r') as config_file:
            config = yaml.load(config_file)

        self.db_client = self._create_db_client(config)
        self.twitter_auth = self._create_twitter_auth(config)

    def _create_db_client(self, config):
        """ Init a new InfluxDB client """

        host = config['database']['host']
        port = config['database']['port']
        user = config['database']['user']
        password = config['database']['password']
        db_name = config['database']['name']

        return InfluxDBClient(host, port, user, password, db_name)

    def _create_twitter_auth(self, config):
        """ Create a new Auth for Twitter """
        # Get twitter api configuration
        consumer_key = config['twitter_api']['consumer_key']
        consumer_secret = config['twitter_api']['consumer_secret']
        access_token = config['twitter_api']['access_token']
        access_token_secret = config['twitter_api']['access_token_secret']

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        return auth

    def run(self):
        """ Start Catching tweets"""
        client = Client(self.twitter_auth, self.db_client)
        client.run()


if __name__ == '__main__':

    CATCHER = Catcher()
    CATCHER.run()
