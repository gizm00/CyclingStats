import urllib2
from bs4 import BeautifulSoup
import re
import sys
import codecs
import psycopg2

#url = 'http://www.procyclingstats.com/rankings/PCS_Specials_2014_06_01_Team_Distances'
if len(sys.argv) < 2:
	print "please provide a url"
else:
	# connect to db
	try:
    		conn = psycopg2.connect("dbname='cycling_stats' user='postgres' host='localhost' password=")
	except:
    		print "unable to connect to the database " + e
	else:		

	    if (conn != None):
	    	dbCursor = conn.cursor();

	url = sys.argv[1]
	tableName = sys.argv[2]
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page)
	table = soup.table['id']

	statsTable = soup.find("table", { "id": "list9"})
	UTF8Writer = codecs.getwriter('utf8')
	sys.stdout = UTF8Writer(sys.stdout)

	for tr in statsTable.find_all('tr')[1:]:
	 	tds = tr.find_all('td')
	 	string  = re.match(r'^(\d*).(\d{3,6})', tds[4].text.strip())
	 	if (string != None) :
	 		formatted = re.sub('\.', ',', tds[4].text.strip())
	 	else :
	 		formatted = tds[4].text.strip()

	 		if ((table != None) & (dbCursor != None)) :
		 			strValues = tds[0].text[:-1] + ",'" + tds[3].text.strip() + "'," +  formatted + ", '2013-06-01 12:00:00'"
		 			strQuery = """INSERT INTO """ + tableName.strip() + """(Rank, TeamName, TotalPoints, Timestamp) VALUES (""" + strValues + """)"""
		 			try:
	    					dbCursor.execute(strQuery)
					except Exception as e:
	    					print "cannot insert into database! " + strQuery

	 					print tds[0].text[:-1] + '\t' + tds[3].text.strip() + '\t' +  formatted
	conn.commit()
	dbCursor.close()
	conn.close()	