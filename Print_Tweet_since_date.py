import tweepy
import csv
import pandas as pd

consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_key = "ACCESS_KEY"
access_secret = "ACCESS_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####HASHTAG_NAME    ->->->Araştırılacak hashtag buraya girilir.
# Dosya yaratıldı.
csvFile = open('tweet_finder1.csv', 'a')
#csv Writer kullanıldı.
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q='#HASHTAG_NAME',count=3,
                           lang="en",
                           since="2019-06-20").items():
    print (tweet.created_at, tweet.text)
csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

