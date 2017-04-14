#Parse Rotten Tomatoes Pages
from lxml import etree, html
import sqlite3
import glob
conn = sqlite3.connect('movies.db')
c = conn.cursor()
parser = etree.HTMLParser()
	#filename = "rotten_2001_tt0278488.html"
for filename in glob.glob("./rotten*.html"):
	tree = etree.parse(filename, parser)
	imdbid = filename.split("rotten_")[1].split("_")[1].split(".html")[0]
	#print(imdbid)
	try :
		tomatometer1 = tree.xpath('//div[contains(@id,"scorePanel")]//*[@id="all-critics-numbers"]//div[contains(@class,"critic-score meter")]//span[contains(@class,"meter-value")]/span/text()')
		tomatoraveragerating1 = tree.xpath('//div[contains(@class,"tomato-left")]//*[@id="scoreStats"][1]/div[1]/text()')
		tomatoreviewcounted1 = tree.xpath('//div[contains(@class,"tomato-left")]//*[@id="scoreStats"][1]/div[2]/span[2]/text()')
		#tomatoraveragerating = tree.xpath('//div[contains(@id,"top-critics-number")]//*[@id="scoreStats"][1]/div[1]/text()')


		tomatometer = tomatometer1[0]
		tomatoraveragerating = "".join(tomatoraveragerating1).split("/10")[0].strip()
		tomatoreviewcounted = "".join(tomatoreviewcounted1) 
		
	except :
		tomatometer = "unavailable"
		tomatoraveragerating  = "unavailable"
		tomatoreviewcounted = "unavailable"


	try :
		metervalue = tree.xpath('//div[contains(@class,"meter-value")]/span/text()')[0].split("%")[0]
		metervalueaveragerating = "".join(tree.xpath('//div[contains(@class,"audience-info")]/div[1]/text()')).split("/5")[0].strip()
		metervaluereviewcounted = "".join(tree.xpath('//div[contains(@class,"audience-info")]/div[2]/text()')).replace(",","").strip()
		
	except:
		metervalue = "unavailable"
		metervalueaveragerating = "unavailable"
		metervaluereviewcounted  = "unavailable"
	print(imdbid, "   ", tomatometer,tomatoraveragerating,tomatoreviewcounted," metervalue : " ,metervalue ," average ", metervalueaveragerating, " counts : ", metervaluereviewcounted)
	c.execute("INSERT INTO tomato(imdbid,tomatometer,tomatoraveragerating,tomatoreviewcounted,metervalue,metervalueaveragerating,metervaluereviewcounted) VALUES (?,?,?,?,?,?,?)", (imdbid,tomatometer,tomatoraveragerating,tomatoreviewcounted,metervalue,metervalueaveragerating,metervaluereviewcounted))

conn.commit()
conn.close()