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

user = api.get_user("USER_NAME")
print("Kullanıcı adı: " + user.screen_name)
print("İsim: " + user.name)
print("Açıklama: " + user.description)
print("Takipçi: " + str(user.followers_count))
print("Takip edilen: " + str(user.friends_count))
print("Tweet sayısı: " + str(user.statuses_count))
print("Web site: " + str(user.url))
print("Kayıt tarihi: " + str(user.created_at))
print("Lokasyon: " + user.location)
print("Dil: " + str(user.lang))
print("Favoriler: " + str(user.favourites_count))



