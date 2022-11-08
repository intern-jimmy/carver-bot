import tweepy

def sendTweet(apiKey, apiSecret, accessToken, tokenSecret, message):
  client = tweepy.Client(consumer_key=apiKey, consumer_secret=apiSecret, access_token=accessToken, access_token_secret=tokenSecret)
  tweet = client.create_tweet(text=message, user_auth=True)
  return tweet