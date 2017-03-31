#Trump bot v0.1
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

#open greetings file and grab lines
greet = open('greetings.txt', 'r')
greet_lines = greet.readlines()
greet.close()
greet_lines = [x.strip() for x in greet_lines]

#open hashtag file and grab lines
hashtag = open('hashtags.txt', 'r')
hashtag_lines = hashtag.readlines()
hashtag.close()
hashtag_lines = [x.strip() for x in hashtag_lines]

while True:
	#grab random video ID
	x = random.sample(video_lines, 1)
	#grab random greeting
	y = random.sample(greet_lines, 1)
	#grab random hashtag
	z = random.sample(hashtag_lines, 1)
	
	tweetstring = y[0] + ' https://www.youtube.com/watch?v=' + x[0] + ' ' + z[0]
	#api.update_status(tweetstring)
	sleep(5)
	
















