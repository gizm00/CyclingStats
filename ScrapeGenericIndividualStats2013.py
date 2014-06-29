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
		tableName = sys.argv[2]
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page)
		table = soup.table['id']

		UTF8Writer = codecs.getwriter('utf8')
		sys.stdout = UTF8Writer(sys.stdout)

		statsTable = soup.find("table", { "id": "list9"})
		#f = codecs.open(sys.argv[2],'w',encoding='utf8')
		for tr in statsTable.find_all('tr')[1:]:
		 	tds = tr.find_all('td')
		 	string  = re.match(r'^(\d*).(\d{3,6})', tds[5].text.strip())
		 	formattedName = tds[3].text.strip().replace("'",'')
		 	if (string != None) :
		 		formatted = re.sub('\.', '', tds[5].text.strip())

		 	else :
		 		formatted = tds[5].text.strip()


		 	if ((table != None) & (dbCursor != None)) :
		 		strValues = tds[0].text[:-1] + ",'" + formattedName + "','" +  tds[4].text.strip() + "'," +  formatted + ", '2013-06-01 12:00:00'"
		 		strQuery = """INSERT INTO """ + tableName.strip() + """(Rank, Name, Team, Points, Timestamp) VALUES (""" + strValues + """)"""
		 		try:
	    				dbCursor.execute(strQuery)
				except Exception as e:
	    				print "cannot insert into database! " + e[0]
		 			print tds[0].text[:-1] + '\t' + formattedName + '\t' +  tds[4].text.strip() + '\t' +  formatted
			
		conn.commit()
		dbCursor.close()
		conn.close()	
