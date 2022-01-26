import tweepy
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

# Create API object
api = tweepy.API(auth)

# Send a tweet

#test 
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print(":(")

api.update_status("write tweet here :)")