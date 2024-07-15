import os
import tweepy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys and tokens from environment variables
api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authentication
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("API:::",api)
# Fetch tweets
# tweets = api.search_tweets(q="keyword", lang="en", count=100, tweet_mode="extended")

# # Store tweets in a list
# tweet_list = [tweet.full_text for tweet in tweets]

# Upload media
def upload_media(file_path):
    media = api.media_upload(file_path)
    return media.media_id

# Post a tweet with media
def post_tweet_with_media(status, file_path):
    # media_id = upload_media(file_path)
    api.update_status(status=status, media_ids="testing")

# Example usage
post_tweet_with_media("Hello, World! This is a tweet with media.", "path_to_image.jpg")