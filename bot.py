import tweepy
         
consumer_key = 'auHo5WKYN4jxzMQkj0D5MRmp7'
consumer_secret = 'tIg8lPxREu6U3FGnM5YLyJwS51os0aDN4qjMxZ4e3n6hFjyJJP'

key = '1302252892359815169-wuv0kpE41P78thQbbc7UKCC0I1yjvb'
secret = 'LqHrNzQZG7Je84W8F3b6ekiPuhEKTKILNQYsN3JFBCar8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

tweets = api.mentions_timeline()
for i in tweets:

	print(i.text)