import tweepy

consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_key = "ACCESS_KEY"
access_secret = "ACCESS_SECRET"

from twython import Twython

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_secret
)

message = "TWEET_MESSAGE"
twitter.update_status(status=message)
print("Tweeted: %s" % message)
