# tweet-catcher
A python utility for saving tweets for a certain topic using Influxdb.

## Instalation

TODO

## Usage

1. Create a config.yml file in your project directory
Example config:
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
  - 'eth'
  - 'ethereum'
  - '#eth'
  - '#ethereum'
  - 'xrp'
  - 'ripple'
  - '#xrp'
  - '#ripple'
  - 'ltc'
  - 'litecoin'
  - '#ltc'
  - '#litecoin'
```

2. Run `catcher.py`

