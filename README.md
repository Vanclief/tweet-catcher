# tweet-catcher
Tweet Catcher allows you to define a set of keywords, and automatically start a
Twitter stream and save tweets that match any of the keywords in a time series
database.

## Requirements

* Python 3.3+

* InfluxDB

* Pip

## Instalation

### Pip

_COOMING SOON_

### From source

Clone the repo
```
git clone https://github.com/Vanclief/tweet-catcher.git
```

Run setup
```
python setup.py install
```

## Usage

1. Create a config.yml file in your project directory.
```
database:
  host: 'localhost'
  port: 8086
  user: root
  password: root
  name: cryptotweets

twitter_api:
  consumer_key: ""
  consumer_secret: ""
  access_token: ""
  access_token_secret: ""

languages:
  - en

keywords:
  - 'btc'
  - 'bitcoin'
  - '#btc'
  - '#bitcoin'
```

2. Run `python catcher.py`


## Contribution

1. Discuss changes by creating a issue.
2. Fork the project.
3. Create a branch with fix, or feature with it's proper tests.
4. Create a PR

