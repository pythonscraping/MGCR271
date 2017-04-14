#Retrieve movies budget imdb page
import urllib.request
from bs4 import BeautifulSoup
import sqlite3

for dyear in [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]:
	for di in ["1","2","3","4","6","7"]:
		filetoanalyse = "./"+str(dyear)+"_" +di+".html"
		soup = BeautifulSoup(open(filetoanalyse))
		liste = []
		for link in soup.find_all('a', href=True):
			if "/title/" in link['href'] :
				liste.append(link['href'].split("?ref")[0].split("vote?")[0].split("/title/")[1].split("/")[0])
		liste = list(set(liste))

		

		for imdbid in liste :
			name = "budget_" + imdbid + ".html"
			link = "http://www.imdb.com/title/" + imdbid + "/business?ref_=tt_ql_dt_4"
			urllib.request.urlretrieve (link , name)