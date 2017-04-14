#Parse imdbib from top300 box office files and retrieve associated data with ImdbPie API
from bs4 import BeautifulSoup
import sqlite3

from imdbpie import Imdb
imdb = Imdb()
imdb = Imdb(anonymize=True)

#,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016
for dyear in [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]:
	for di in ["1","2","3","4","6","7"]:
		conn = sqlite3.connect('movies.db')
		c = conn.cursor()
		filetoanalyse = "./"+str(dyear)+"_" +di+".html"
		soup = BeautifulSoup(open(filetoanalyse))
		liste = []
		for link in soup.find_all('a', href=True):
			if "/title/" in link['href'] :
				liste.append(link['href'].split("?ref")[0].split("vote?")[0].split("/title/")[1].split("/")[0])
		liste = list(set(liste))

		

		for imdbid in liste :
			try :
				dtitle = imdb.get_title_by_id(imdbid)
				movietitle = dtitle.title
				year = dtitle.year
				try:
					genre = dtitle.genres[0]
				except:
					genre = "unavailable"
				imdbrating = dtitle.rating
				imdbvotes = dtitle.votes
				try:
					runtime = dtitle.runtime
				except:
					runtime = 0
				try :
					release_date = dtitle.release_date
				except:
					0
				print(movietitle,year,genre,imdbrating,imdbvotes,runtime,release_date)
				c.execute("INSERT INTO movies(imdbid,movietitle,year,genre,imdbrating,imdbvotes,runtime,release_date) VALUES (?,?,?,?,?,?,?,?)", (imdbid,movietitle,year,genre,imdbrating,imdbvotes,runtime,release_date))
			except:
				print(imdbid + " has FAILED...")
		conn.commit()
		print (di + " " + str(dyear) + " IS DONE")
conn.close()
