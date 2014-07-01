import urllib2
import re
from bs4 import BeautifulSoup
import sys
import codecs
import psycopg2

#url = 'http://www.procyclingstats.com/rankings/UCI_Individual_2014_06_02_EuropeTour'
if len(sys.argv) < 2:
	print "please provide a url"
else:
	# connect to db
	try:
    		conn = psycopg2.connect("dbname='cycling_stats' user='postgres' host='localhost' password=''")
	except:
    		print "unable to connect to the database"
	else:		

	    if (conn != None):
	    	dbCursor = conn.cursor();

		# get data from website
		url = sys.argv[1]
		#tableName = sys.argv[2]
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page)

		UTF8Writer = codecs.getwriter('utf8')
		sys.stdout = UTF8Writer(sys.stdout)
		for div in soup.find_all('div', { "class": "text1"})[1:]:
			#for div in prediv.find_all('div', {"width": "245px"})[1:]:
			element = div
			riders = []
			riderCount = 0
			team = "";
			while True :
				element = element.next_element
				try :
					tag = element.name
				except AttributeError:
					tag = ""
				if (tag == "div") :
					#try:
					#	rightDiv = re.match("width: 245px", element.style)
					#except:
					#	rightDiv = None
					#if (rightDiv != None) :
					strTeamValues = "( '" + team + "'"
					strTeamInfo = "INSERT INTO cs_tdf_riders (Team, Name, Timestamp) VALUES ('" + team + "',"
					for rider in riders:
						formatName = rider.strip().replace("'",'')
						print strTeamInfo + "'" + formatName + "', current_timestamp);"
					break;
				if tag == "a" :
					#print element.text
					if (re.match('team', element.get('href'))):
						team = element.text.strip()
					if (re.match('rider', element.get('href'))):
						riders.append(element.text.strip())
