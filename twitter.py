import tweepy

auth = tweepy.OAuthHandler('sB0dfM83HfCfMVbzbInx3Iu79', 'fZE1XGHxwyUxth3K5uRoUwqifoE9uV1iuRzzvg6e8mXrK1xc9H')
auth.set_access_token('1288503502390669313-pj7gmFcv3savN1GleWtv4vnds8kEXU', 'NCi4yYTgluQPRZLE1AXYAZZyCAlYSxvEPKGL53IZkL4yG')

api = tweepy.API(auth,  wait_on_rate_limit=True)
