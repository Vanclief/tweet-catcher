# tweet-catcher
A python utility for saving tweets in a time stamp database.


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


topics:
  bitcoin:
    - 'btc'
    - '$btc'
    - '#btc'
    - 'bitcoin'
    - '$bitcoin'
    - '#bitcoin'
  ethereum:
    - 'eth'
    - '$eth'
    - '#eth'
    - 'ethereum'
    - '$ethereum'
    - '#ethereum'
```

