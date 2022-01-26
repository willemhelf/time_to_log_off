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

api.update_status("made a janky little thing to post tweets via code editor/terminal... coding/API knowledge very much required lol... have fun https://github.com/sophiehelf/time_to_log_off")