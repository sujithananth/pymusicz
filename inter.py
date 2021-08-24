import PySimpleGUI as sg
import tcreate
from pygame import mixer
from audiofunction import get_meta
from dbfunc import insert_into_table, select_from_table, delete_from_table,insert_into_table_other, select_from_table_other, select_id_from_table_other, select_song_from_table_other,select_song_from_table_other_prev
#importing the respective functions from the files
sg.theme("dark grey 13")
songs =[] 
#getting the list of playlists(table) in the database
playlists=tcreate.list_playlist()
import webbrowser
#creating the layout with buttons ,listbox,texts
layout=[

    [sg.InputText('',key='song',size=(50,2)),sg.FileBrowse(),sg.Button("refresh",key='refresh'),sg.Text("FOSS",font="courier")],
    [sg.Button("create playlist",key='create' ),sg.Text("playlists "),sg.Combo((playlists), enable_events=True, key='combo'),sg.Button("Add songs",key='add songs'),sg.Text("                 ",key='current'),sg.Text("                  ",key='output')],
    [sg.Listbox("", size=(60, 10), font=("Arial", 14), key='items')],
    [sg.Button("remove",key='remove'),sg.Button("select",key='select'),
    sg.Button("play",key='play'),
    sg.Button("pause",key='pause'),
    sg.Button("resume",key='resume'),
    sg.Button("stop",key='stop'),sg.Button("previous",key='previous'),sg.Button("next",key='next'),sg.Button("get metadata",key='meta')]

    
]




#intiallising the mixer module to play the songs
mixer.init()

#this function adds playing songs to the recent playlist(table)
def recent_add_item(song):
    #just getting the key 
    action = window.FindElement('play').GetText()
    #condition  whether the song is played and to avoid repitation checking whether the song alredy in that table 
    if action == 'play'and( song not in songs):
        #inserting the song into the table recent 
        #function is in dbfunc.py
        insert_into_table(song)
        #updating the window
        window.FindElement('song').Update('')
def edit_item(oldtask):
    #updates the next song name 
    window.FindElement('song').Update(value=oldtask)

def add_item():
    #gets the table name 
    f=window.FindElement('output').get()
     #a window opens to get multiple files to add in playlist
    event, values = sg.Window('add songs').Layout([[sg.Text("after adding close window")],[sg.Input(key='_FILES_'), sg.FilesBrowse()], [sg.OK(), sg.Cancel()]]).Read()
    #shows the songs to be added in playlists
    sg.popup_scrolled(values['_FILES_'].split(';'))
    qts=(values['_FILES_'].split(';'))
    #inserts the songs 
    insert_into_table_other(f,qts)
    #updates the screen 
    new_songs = select_from_table()
    window.FindElement('items').Update(values=new_songs)
    
def delete_item(song):
    #gets the table name 
    f=window.FindElement('output').get()
    #deletes the song in respective song
    delete_from_table(f,song)
    #updates the screen 
    new_songs = select_from_table()
    window.FindElement('items').Update(values=new_songs)



window=sg.Window("pymusicz-a student project ",layout)
while True:
    Events,values=window.read()
    if Events == sg.WINDOW_CLOSED:
        #when window is closed loop breaks
        break
    elif Events == 'play':
        #loads the songs 
        mixer.music.load(values['song'])
        mixer.music.set_volume(1)
        mixer.music.play()
        #adds the songs played recently to the table recent
        try:
            #gets the name of the table 
            f=window.FindElement('output').get()
            #gets the id of the playing song
            z=select_id_from_table_other(f,values['song'])
            #get the next song name and updates the screen 
            edit_item(select_song_from_table_other(f,z))
        except:
              print("oops  playlist is ended")
    elif Events == 'select':
        #updates the selected song from the table
        edit_item(values['items'][0])
    elif Events == 'remove':
        #removes the song from the respective table
        delete_item(values['items'][0])
    elif Events == 'stop':
        #stops music
         mixer.music.stop()
    elif Events == 'resume':
        #resumes  the paused song
         mixer.music.unpause()
    elif Events == 'pause':
         #pauses the song
          mixer.music.pause()
    elif Events == 'create':
        #gets the name to which the playlist is to be created 
        name = sg.popup_get_text('enter the playlist names')
        #a conformation message
        sg.popup('playlist name', 'playlist is created as ',name )
        strname=str(name)
        #creates the table in the name of the user 
        tcreate.text_in(strname)
        #a window opens to get multiple files to add in playlist
        event, values = sg.Window('add songs').Layout([[sg.Text("after adding close window")],[sg.Input(key='_FILES_'), sg.FilesBrowse()], [sg.OK(), sg.Cancel()]]).Read()
        #shows the songs to be added in playlists
        sg.popup_scrolled(values['_FILES_'].split(';'))
        #inserts the songs into table 
        qts=(values['_FILES_'].split(';'))
        insert_into_table_other(name,qts)
    elif Events == 'next':
        try:
            #stops the music 
            mixer.music.stop()
            #getting the table name
            f=window.FindElement('output').get()
            #getting id of the song 
            z=select_id_from_table_other(f,values['song'])
            z=z-1
            #getting the next song
            ed=select_song_from_table_other(f,z)
            #playing the next song
            mixer.music.load(ed)
            mixer.music.set_volume(0.7)
            mixer.music.play()
            y=z+1
            #updating  for next song 
            ed=select_song_from_table_other(f,y)
            window.FindElement('song').Update(ed)
        except:
               None
    elif Events == 'previous':
        try:
           #stops the music 
           mixer.music.stop()
           #gets the table name 
           f=window.FindElement('output').get()
           #gets the id of the song
           z=select_id_from_table_other(f,values['song'])
           z=z-1
           #getting the previous song
           ed=select_song_from_table_other_prev(f,z)
           #loading the previous song
           mixer.music.load(ed)
           mixer.music.set_volume(0.7)
           #playing
           mixer.music.play()
           y=z-1
           #updating for next song
           ed=select_song_from_table_other(f,y)
           window.FindElement('song').Update(ed)
        except:
              None
    elif Events == 'meta':
        try:
           #when we click on get metadata here we call this function
           meta=get_meta(values['song'])
           #shows the metadata as popup
           sg.Popup(meta)
        except:
            None
    elif Events == 'refresh':
        #since when we create the new playlist the combo box doesnt show it coz we need screen update so when we click on it ,it refresh 
        playlist=tcreate.list_playlist()
        #hence update thes combo values
        window.FindElement('combo').Update(values=playlist)
    elif Events == 'add songs':
        #this function adds the songs to the existing table 
         add_item()
    elif Events == 'combo':
        #getting the value selected in the combobox
        combo = values['combo'] 
        #since the result is in tuple with 2 values one is table name and another one is empty one ,we use [0] to select first one 
        new_songs = select_from_table_other(combo[0])
        #updating the listbox value .updating the tables songs in the listbox
        window.FindElement('items').Update(values=new_songs)
        #just updating the text near combo box
        window.FindElement('current').Update("playing")
        #changing the text near youtube music
        window.FindElement('output').Update(combo[0])
        
