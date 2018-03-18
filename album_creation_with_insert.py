import sqlite3


db = sqlite3.connect('albumcollection.db')
cursor = db.cursor()

def table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS albums(id INTEGER PRIMARY KEY, name TEXT, year INTEGER, artist TEXT, genre TEXT)''')

def data_entry():
    cursor.execute('''INSERT INTO albums VALUES(1, 'Roots', 1995, 'Sepultura', 'Metal')''')
    db.commit()
    cursor.close()
    db.close()

table()
data_entry()
