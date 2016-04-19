from bs4 import BeautifulSoup
import urllib2
import MySQLdb

# connecting to database
db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="password", db="LabBasedProject",charset='utf8' )
cursor=db.cursor()

# url to start with
url='https://www.wikidata.org/w/index.php?title=Special:WhatLinksHere/Q5&limit=500'

for i in range(1,101) :

	# get web page from given url
	data = urllib2.urlopen( url ).read()
	
	# making a soup object
	soup = BeautifulSoup(data)

	# finding all links
	link_array=soup.find_all('a')

	url=''
	# looking for next page url
	for link in link_array:
		if link.string=='next 500':
			temp=link['href']
			url='https://www.wikidata.org'+temp
			break

	# searching for name specific list on webpage
	if soup.ul['id']=='mw-whatlinkshere-list' :
		data=soup.ul
		person_list=data.find_all('li')
		
		for person in person_list :
			temp=person.a['title']
			temp1=temp.split('|')
			if len(temp1)>=2 :
				name=temp1[0][0:len(temp1[0])-1].lower()
				description=temp1[1][1:len(temp1[1])-1].lower()
				cursor.execute("INSERT INTO `WikiPersons`(`NAME`,`DESCRIPTION`) VALUES (%s,%s)",(name,description))

		# write url of next page on a text file so that can resume process if error occurs
		f = open('url', 'w')
		f.write(url)
		f.close()
		db.commit()
		print i

cursor.close()
db.close()
