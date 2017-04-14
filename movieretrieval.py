#Retrieved top 300 box office files for each year

years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
i =  ["1","2","3","4","6","7"]
import urllib.request
for year in years:
	for page in i :
		name = str(year) + "_" + page + ".html"
		link = "http://www.imdb.com/search/title?release_date=" + str(year) + "&sort=boxoffice_gross_us,desc&view=simple&page=" + page + "&ref_=adv_nxt"
		urllib.request.urlretrieve (link , name)