import sqlite3

#creating a table in the name of user inputs with more columns
def text_in(name):
    text=name
    z="""CREATE TABLE """+text+""" (
         id INTEGER PRIMARY KEY,
         songname TEXT,
         artists  TEXT,
         album  TEXT,
         genre  TEXT,
         year  INTEGER ,
         Duration  FLOAT
         )"""
    sql_query=z
    #calling the execute query function with the given input to create the table in database playlists
    execute_query(sql_query)


def execute_query(sql_query):
    #connecting to the database  playlists as db
    with sqlite3.connect('playlists') as db:
        csr = db.cursor()
        #executng the query 
        result = csr.execute(sql_query)
        db.commit()
    return result

def list_playlist():
        with sqlite3.connect('playlists') as db:
             cursor = db.cursor()
             #here we want the list of playlist ,so we given this query 
             cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return cursor.fetchall()


if __name__ == '__main__':
    def checkda():
        with sqlite3.connect('playlists') as db:
             cursor = db.cursor()
             cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
             print(cursor.fetchall())

    checkda()