
import tweepy

consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_key = "ACCESS_KEY"
access_secret = "ACCESS_SECRET"

try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    auth.get_authorization_url()
    api = tweepy.API(auth)
except tweepy.TweepError:
    print('Hata')

public_tweets = api.user_timeline(screen_name="USER_NAME", count=10)  #  Kullanıcının son 10 tweeti
for tweet in public_tweets:
    print(tweet.text)


