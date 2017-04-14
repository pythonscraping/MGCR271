import sqlite3
conn = sqlite3.connect('movies.db')
c = conn.cursor()

#c.execute('''CREATE TABLE movies
#             (imdbid text, movietitle TEXT, year INTEGER, genre text, imdbrating real, imdbvotes INTEGER,runtime REAL,release_date TEXT)''')
c.execute('''CREATE TABLE tomato
             (imdbid text, 
             tomatometer TEXT, tomatoraveragerating TEXT, tomatoreviewcounted TEXT,
             metervalue TEXT, metervalueaveragerating TEXT, metervaluereviewcounted TEXT )''')
conn.commit()
conn.close()