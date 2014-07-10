from twython import Twython, TwythonError
from unidecode import unidecode
import psycopg2
import time
import re

def GetResults(search_results) :
	tweetCount = 0;
	length = len(search_results['statuses'])
	print "search results: " + str(length)
	lastId = 0
	for tweet in search_results['statuses']:
		ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
		#print 'Tweet %s from @%s Date: %s Location: %s Coords: %s Geo: %s Id: %s Lang: %s' % (tweetCount, tweet['user']['screen_name'].encode('utf-8'), ts, tweet['user']['location'].encode('utf-8'), tweet['coordinates'], tweet['geo'], tweet['id'], tweet['lang'])
		#print tweet['text'].encode('utf-8'), '\n'

		queryStr = "INSERT INTO tweets (screen_name, created_at, location, coordinates, geo, lang, id, tweet) VALUES("
		#queryVals = "'" + unidecode(tweet['user']['screen_name']) + "','" + ts + "','" + unidecode(tweet['user']['location']) + "','" + unidecode(tweet['coordinates']) + "','" + tweet['geo'] + "'," + tweet['id'] + ",'" + tweet['lang'] + "')"
		if (tweet['user']['location'] == None ): 
			location = "NULL" 
		else : 
			location = tweet['user']['location']
			#print "location: " + location
		if (tweet['coordinates'] == None):
			coords = "NULL"
		else :
			coords = str(tweet['coordinates']['coordinates'][0]) + " " + str(tweet['coordinates']['coordinates'][1])
			print "coords: " + coords
		if (tweet['geo'] == None) :
			geo = "NULL"
		else :
			geo = str(tweet['geo']['coordinates'][0]) + " " + str(tweet['geo']['coordinates'][1]) 
			#print "geo: " + geo

		queryVals = "'" + re.sub(r"[',]", "", tweet['user']['screen_name']) + "','" + ts + "','" + re.sub(r"[',]", "", location)+ "','" + coords + "','" + geo + "','" + re.sub(r"[',]", "", tweet['lang']) + "'," + str(tweet['id']) + ",'" + re.sub(r"[',\/n]", "", tweet['text'])+ "')"
	
		try :
			dbCursor.execute(queryStr + queryVals)
			conn.commit()
		except Exception as e :
			print "Unable to insert: " + e[0] + " " + queryStr + queryVals
			conn.rollback()

		tweetCount = tweetCount + 1
		if (tweetCount == length-1) :
			lastId = tweet['id']

	return lastId


consumer_key="key"
consumer_secret="secret"
access_token="token"
access_token_secret="token secret"

twitter = Twython(consumer_key,
              consumer_secret,
              access_token,
              access_token_secret)

try:
    search_results = twitter.search(q='froome', count=100, max_id=486851492666941440)
except TwythonError as e:
    print e

# connect to db
try:
	 conn = psycopg2.connect("dbname='twitter_froome' user='postgres' host='localhost' password=''")
except:
	print "unable to connect to the database"
else:		
	if (conn != None):
   	 	dbCursor = conn.cursor();

#while (len(search_results) > 0) :
for i in range (0, 50) :
	newIndex = GetResults(search_results)
	print "new index:  " + str(newIndex)
	search_results = twitter.search(q='froome', count=100, max_id=newIndex)

dbCursor.close()
conn.close()