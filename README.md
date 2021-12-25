# pymusicz

### this page is a mirror of original project at gitlab[https://gitlab.com/univrz/pymusicz](https://gitlab.com/univrz/pymusicz) 
basic music player made with  python's pysimpleGUI,mixer module of pygame and tinytag.it is a college student project.

Before getting started we need certain python modules:

    GRAPHICAL USER INTERFACE (GUI): PySimpleGUI

    MUSIC: mixer module of pygame

    METADATA OF SONGS: tinytag


module installing :
    
    pip install PySimpleGUI
                                
    pip install pygame
                                    
    pip install tinytag

the mixer module of pygame can play the song ,the song is loaded and we can change the volume and play it :

`mixer.music.load(values['song'])`
`mixer.music.set_volume(1)`
`mixer.music.play()`

now started to play the song ,now we have to pause, resume and stop the song which is playing..


`mixer.music.pause()`
`mixer.music.unpause()`
`mixer.music.stop()`

so now we can do all the basic things with it .next we want  metadata of the song that is the details embedded in the songs.see here how we can get [audiofunction.py](https://gitlab.com/univrz/pymusicz/-/blob/main/audiofunction.py),exaplained in comments.in that the statements are inside the function so while returning values i need all of them ,so i used a list to return all the values .

now we got song playing ,getting metadata.next the ui ...here pysimplegui .created a layout and buttons with keys ,the keys helps to identify which button is pressed .based on the buttons pressed giving commands to mixer module.in the layout used file browser to fetch songs.and used sqlite to create playlist.and can add or remove songs to the existing playlists.for more look into the comments of the code files ...[inter.py](https://gitlab.com/univrz/pymusicz/-/blob/main/inter.py)(the main file),[tcreate.py](https://gitlab.com/univrz/pymusicz/-/blob/main/tcreate.py)(for creating playlists),[dbfunc.py](https://gitlab.com/univrz/pymusicz/-/blob/main/dbfunc.py)(used to add ,remove songs to playlists and to get list of playlists)
