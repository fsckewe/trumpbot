# trumpbot
There are two bots here:
trumpbot.py - tweets random alex jones videos at donnie at an interval of your choosing
trumpbotsearch.py - searches for #maga and replies with random greeting and random video

trumpbot.py - Getting started: uses trumpbot.py, greetings.txt, videos.txt and hashtags.txt

1 - Change sleep to something more than 5 seconds.

2 - Uncomment this:

	#api.update_status(tweetstring)
	
3 - Add your own tbcreds.py with the following:

	CONSUMER_KEY = " "
	CONSUMER_SECRET = " "
	ACCESS_KEY = " "
	ACCESS_SECRET = " "

4 - edit greetings.txt, videos.txt and hashtags.txt as you see fit


trumpbotsearch.py - Getting started: uses trumpbotsearch.py, intro.txt and videos.txt 

1 - modify search term (q=) and number of results if you wish
	
	for tweet in tweepy.Cursor(api.search, q='#maga').items(100):

2 - Uncomment this:

	#api.update_status(m, tweet.id)

3 - Add your own tbcreds.py with the following:

	CONSUMER_KEY = " "
	CONSUMER_SECRET = " "
	ACCESS_KEY = " "
	ACCESS_SECRET = " "
