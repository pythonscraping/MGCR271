#Retrieve Rotten Tomatoes html pages for each movie
from lxml import etree, html
import glob
import sqlite3
import urllib.request
conn = sqlite3.connect('movies.db')
c = conn.cursor()
c.execute('SELECT imdbid,movietitle,year FROM movies WHERE year = 2016')
d = c.fetchall()
for imdbid,movietitle,year in d:
	filename = "rotten_"+ str(year) + "_" + imdbid + ".html"
	

	improved = ''.join(ch for ch in movietitle if (ch.isalnum() or ch==" "))
	improved = improved.replace(" ","_").lower()
	try :
		link = "https://www.rottentomatoes.com/m/"+improved
		urllib.request.urlretrieve (link , filename)
		#print(imdbid +" " +movietitle +" " + improved+  " " + str(year))
	except:
		print(" Did not find : " + imdbid + " " + movietitle + " " + improved)
