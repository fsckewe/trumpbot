#MAGA reply bot v0.1
#Not possible without the help of this:
#https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library
#So many idiotic "twitter bot" tutorials out there. You cunts should be ashamed of yourselves for wasting people's time.

import tweepy
import random
from time import sleep
from tbcreds import *

#setup auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#open video file and grab lines
videos = open('videos.txt', 'r')
video_lines = videos.readlines()
videos.close()
video_lines = [x.strip() for x in video_lines]

#open intro file and grab lines
intro = open('intro.txt', 'r')
intro_lines = intro.readlines()
intro.close()
intro_lines = [x.strip() for x in intro_lines]


while True:
	
	i=0

	for tweet in tweepy.Cursor(api.search, q='#maga').items(100):
		try:
			#console output info for debugging/status
			print('\n#######################\nTweet by: @' + tweet.user.screen_name)
			print tweet.id
			print tweet.text
			print tweet.retweeted
        
			#check for retweets, either offical tweetid status or the addition of RT/RETWEET        
			if not tweet.retweeted and 'RT @' not in tweet.text and 'RETWEET' not in tweet.text:
				print ('\nGood tweet for reply\n')
				x = random.sample(video_lines, 1) #pick random video
				y = random.sample(intro_lines, 1) #pick random intro of reply tweet
				
				#build reply message and ship it
				m = "@" + tweet.user.screen_name + " " + y[0] + " Did you see this https://www.youtube.com/watch?v=" + x[0] + " !!"
				#api.update_status(m, tweet.id)
				print('Replied to the tweet')
				i+=1
				
			sleep(5)
	
			if i > 1:
				print ('\n####\nThat\'s enough for now\n####')
				break

		except tweepy.TweepError as e:
			print(e.reason)

		except StopIteration:
			break
	print('\nwaiting...')
	sleep(200)
	print('\nstill waiting...')
	sleep(200)
	print('\njust a little more waiting...')
	sleep(200)
	

