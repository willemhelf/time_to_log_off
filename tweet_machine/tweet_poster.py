import tweepy
import config

auth = tweepy.OAuthHandler(config.client_id, config.client_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

# Create API object
api = tweepy.API(auth)

# Send a tweet

api.update_status("hi")