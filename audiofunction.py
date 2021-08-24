import tinytag 
#titag module is used to get the meta data from the songs 
def get_meta(song):
    audio = tinytag.TinyTag.get(song)
    lizt=[]
    #getting the title of the song and append to the lizt 
    lizt.append("Title:" + str(audio.title))
    #getting artists name and append to the lizt
    lizt.append("Artist:" +str(audio.artist))
    #getting the genre of the song and append to the lizt
    lizt.append("Genre:" + str(audio.genre))
    #getting the year of the song and append to the lizt
    lizt.append("Year Released: " + str(audio.year))
    #getting bitrate and append to the lizt
    lizt.append("Bitrate:" + str(audio.bitrate) + " kBits/s")
    #getting  composer and append to the lizt
    lizt.append("Composer: " + str(audio.composer))
    #getting file size and append to the lizt
    lizt.append("Filesize: " + str(audio.filesize) + " bytes")
    #album and append to the lizt
    lizt.append("AlbumArtist: " +str(audio.albumartist))
    #getting time duration and append to the lizt
    lizt.append(int(audio.duration))
    #audio total and append to the lizt
    lizt.append("TrackTotal: " + str(audio.track_total))
    #returning the lizt values from the function
    return lizt


