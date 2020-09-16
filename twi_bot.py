import tweepy
import time
consumer_key = 'auHo5WKYN4jxzMQkj0D5MRmp7'
consumer_secret = 'tIg8lPxREu6U3FGnM5YLyJwS51os0aDN4qjMxZ4e3n6hFjyJJP'

key = '1302252892359815169-wuv0kpE41P78thQbbc7UKCC0I1yjvb'
secret = 'LqHrNzQZG7Je84W8F3b6ekiPuhEKTKILNQYsN3JFBCar8'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)



f_name = 'last_tweet.txt'

def file_reader(f_name):
	reader=open(f_name, 'r')
	last_id=int(reader.read().strip())
	reader.close()
	return last_id

def file_writter(f_name,las_id):
	writer=open(f_name, 'w')
	writer.write(str(las_id))
	writer.close()
	return 



def reply():
	tweets = api.mentions_timeline(file_reader(f_name),tweet_mode='extended')
	for t in reversed(tweets):

		if 'welcome' in t.full_text.lower():
			print(t.user.id)
			api.send_direct_message(t.user.id,"Thanks for mentioning or following me!")
			api.update_status('@'+ t.user.screen_name+ ' hello there..',t.id)
			api.create_favorite(t.id)
			api.retweet(t.id)
			file_writter(f_name,t.id)
while True:
	reply()
	time.sleep(2)

		