import yaml
from influxdb import InfluxDBClient
from multiprocessing.dummy import Pool as ThreadPool
from tweetcatcher.client import Client


class Catcher(object):

    def __init__(self):
        with open("config.yml", 'r') as config_file:
            config = yaml.load(config_file)

        self.topics = config['topics']
        self.twitter_auth = self._create_twitter_auth(config)
        self.db_client = self._create_db_client(config)

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

        return None

    def _catch_tweets(self, topic):
        client = Client(self.db_client, topic)
        client.run()

    def run(self):
        pool = ThreadPool(len(self.topics))
        pool.map(self._catch_tweets, self.topics)
        pool.close()
        pool.join()


if __name__ == '__main__':

    catcher = Catcher()
    catcher.run()

#
    # CONSUMER_KEY = CONFIG['twitter_api']['consumer_key']
    # CONSUMER_SECRET = CONFIG['twitter_api']['consumer_secret']
    # ACCESS_TOKEN = CONFIG['twitter_api']['access_token']
    # ACCESS_TOKEN_SECRET = CONFIG['twitter_api']['access_token_secret']

    # HOST = CONFIG['database']['host']
    # PORT = CONFIG['database']['port']
    # USER = CONFIG['database']['user']
    # PASSWORD = CONFIG['database']['password']
    # DBNAME = CONFIG['database']['name']

    # DBCLIENT = InfluxDBClient(HOST, PORT, USER, PASSWORD, DBNAME)

    # LISTERNER = StdOutListener()
    # AUTH = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # TOPICS = (CONFIG['topics']['bitcoin'])
    # LANGUAGES = (CONFIG['languages'])

    # for topic in CONFIG['topics']:
        # print(topic)

    # STREAM = Stream(AUTH, LISTERNER)
    # STREAM.filter(track=TOPICS, languages=LANGUAGES)
