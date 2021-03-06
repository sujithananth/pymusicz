import sqlite3


def execute_query(sql_query):
    #connecting to the database playlists
    with sqlite3.connect('playlists') as db:
        csr = db.cursor()
        result = csr.execute(sql_query)
        db.commit()
    return result

#get the song name to be inserted to the recent table 
def insert_into_table(song):
    #setting the query to insert song in recent table
    sql_query = """INSERT INTO RECENT(songname) VALUES('%s')""" % (song)
    execute_query(sql_query)

#this function is called when a playlist is created to add more songs to the table 
def insert_into_table_other(name,song):
    #we are using the for loop because of too many songs 
    for i in range(len(song)):
        #setting sql query to add songs to the respective table
       sql_query = """INSERT INTO """+name+"""(songname) VALUES('%s')""" % (song[i])
       #executing the query
       execute_query(sql_query)

#this function extracts the songs in table 
def select_from_table_other(name):
    sql_query = """SELECT songname from """+name+""" """
    result = execute_query(sql_query)
    return [result[0] for result in result.fetchall()]

#this function is used to find the next song name by the id 
def select_song_from_table_other(name,y):
    #here the table name and id of the currently playing song is given as arguments 
    #here we need id of next song so adding  plus 1 
    x=y+1
    a=int(x)
    #here name of the table and id is giving to the query 
    sql_query = """SELECT songname from """+name+""" WHERE id=('%s') """ % (a)
    result = execute_query(sql_query)
    #the result will in tuple so using the index getting 
    z=[result[0] for result in result.fetchall()]
    return z[0]

def select_song_from_table_other_prev(name,y):
    #here the table name and id of the currently playing song is given as arguments 
    #here we need id of next song so adding  plus 1 
    x=y-1
    a=int(x)
    #here name of the table and id is giving to the query 
    sql_query = """SELECT songname from """+name+""" WHERE id=('%s') """ % (a)
    result = execute_query(sql_query)
    #the result will in tuple so using the index getting 
    z=[result[0] for result in result.fetchall()]
    return z[0]

#this function is called when song is palyed and here the song name is sent and it returns the id of playing song
def select_id_from_table_other(name,z):
    a=str(z)
    sql_query = """SELECT id from """+name+""" WHERE songname=('%s')""" % (a)
    result = execute_query(sql_query)
    z= [result[0] for result in result.fetchall()]
    return z[0]



def select_from_table():
    sql_query = """SELECT songname from RECENT"""
    result = execute_query(sql_query)
    return [result[0] for result in result.fetchall()]


#this function works when remove button is clicked
def delete_from_table(name,song):
    #here query is to  deletes the respective song from the respective table
    sql_query = """DELETE FROM """+name+""" WHERE songname=('%s')""" % (song)
    #again execute our query
    execute_query(sql_query)