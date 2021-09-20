from config.config import engine
import pandas as pd
"""
CHECK FUNCTIONS
"""
def check_artist(artist):
    """
    function that checks if artist is already found in database
    ARGS: artist name
    RETURN: Returns -1 if artist already found in database, if return is not -1, then it returns id of new artist that has been inserted into database
    """
    
    cursor = engine.execute(f"SELECT idartists FROM artists WHERE artist_name = '{artist}'")
    try:
        id_artist = list(cursor)[0][0]
    except Exception as err:
        return -1
    return id_artist

def check_album(album):
    """
    function that checks if album is already found in database
    ARGS: album name
    RETURN: Returns -1 if album is already found in database, if return is not -1, then it returns id of new album that has been inserted into database
    """
    
    cursor = engine.execute(f"SELECT idalbums FROM albums WHERE album_name = '{album}'")
    try:
        id_album = list(cursor)[0][0]
    except Exception as err:
        return -1
    return id_album

def check_lyrics(lyrics):
    """
    function that checks if lyrics are already found in database
    ARGS: lyrics
    RETURN: Returns -1 if lyrics already found in database, if return is not -1, then it returns id of new lyrics that has been inserted into database
    """
    cursor = engine.execute(f"SELECT idlyrics FROM lyrics WHERE lyrics = '{lyrics}'")
    try:
        id_lyrics = list(cursor)[0][0]
    except Exception as err:
        return -1
    return id_lyrics

def check_song(song):
    """
    function that checks if song is already found in database
    ARGS: song name
    RETURN: Returns -1 if song already found in database, if return is not -1, then it returns id of new song that has been inserted into database
    """
    cursor = engine.execute(f"SELECT idsong FROM songs WHERE song_name = '{song}'")
    try:
        id_song = list(cursor)[0][0]
    except Exception as err:
        return -1
    return id_song

"""
INSERT FUNCTIONS

"""

def insertArtist(artist):
    """
    function that inserts a new artist into the database, uses check function first of all to make sure that no duplicates are found
    ARGS: artist name
    RETURN: Returns artist id if artist already found in database, if not already in database, then function inserts artist and returns id of new artist that has been inserted.
    """
    id_artist = check_artist(artist)
    if id_artist > 0:
        return id_artist
    else:
        cursor = engine.execute(f" INSERT INTO artists (artist_name) VALUES ('{artist}');")
        return cursor.lastrowid

def insertAlbum(album,artistid):
    """
    function that inserts a new album into the database, uses check function first of all to make sure that no duplicates are found
    ARGS: album name, artist id of artist that owns the album
    RETURN: Returns album id if album already found in database, if not already in database, then the function inserts the album name based on artist id and returns id of new album that has been inserted.
    """
    id_album = check_album(album)
    
    if id_album > 0:
        return id_album
    else:
        cursor = engine.execute(f" INSERT INTO albums (album_name,artists_idartists) VALUES ('{album}',{artistid});")
        return cursor.lastrowid

def insertlyrics(lyrics):
    """
    function that inserts new lyrics into the database, uses check function first of all to make sure that no duplicates are found
    ARGS: lyrics
    RETURN: Returns lyrics id if lyrics already found in database, if not already in database, then the function inserts lyrics and returns id of new lyrics that have been inserted.
    """

    id_lyrics = check_lyrics(lyrics)
    if id_lyrics > 0:
        return id_lyrics
    else:
        cursor = engine.execute(f" INSERT INTO lyrics(lyrics) VALUES ('{lyrics}');")
        return cursor.lastrowid

def insertSong(song,artistid,idlyrics):
    """
    function that inserts a new song into the database, uses check function first of all to make sure that no duplicates are found
    ARGS: song, artistid and lyricsid
    RETURN: Returns songid if song is already found in database, if not in database, then function inserts song and returns id of new song that has been inserted into database.
    """
    id_song = check_song(song)
    
    if id_song > 0:
        return id_song
    else:
        cursor = engine.execute(f" INSERT INTO songs (song_name,artists_idartists,lyrics_idlyrics) VALUES ('{song}',{artistid},{idlyrics});")
        return cursor.lastrowid

"""
CALL FUNCTIONS
"""

artist_id = {"Oasis": 82,
            "Liam Gallagher" : 83,
            "Noel Gallagher´s flying birds": 84}

def artistsalbums(artist):
    """
    Calls API with artist name to receive all artists albums found in DB
    ARGS : artist name
    Returns: Artists albums
    """
    print(artist)
    if artist == "Oasis":
        artists_id = (artist_id["Oasis"])
    elif artist == "Liam Gallagher":
        artists_id = (artist_id["Liam Gallagher"])
    elif artist == "Noel Gallagher´s flying birds":
        artists_id = (artist_id["Noel Gallagher´s flying birds"])
    else:
        print("This artist is not in database or has been spelt incorrectly, please try again")
    
    query = f"""SELECT * 
    FROM albums
    WHERE artists_idartists = {artists_id}
    """

    print(query)

    datos = pd.read_sql_query(query,engine)

    return datos.to_json(orient="records")


song_lyrics_id = {"Wonderwall":32,
"Morning glory":33,
"Champagne supernova":34,
"She´s electric":35,
"Stop crying your heart out":36,
"Wall of glass":37,
"Greedy soul":38,
"Come back to me":39,
"Once":40,
"The river":41,
"In the heat of the moment":42,
"If i had a gun":43,
"Everybody´s on the run ":44,
"Stop the clocks":45,
"Dream on":46
}

def songslyrics(songname):
    """
    Calls API with song name to receive lyrics of the song found in DB.
    ARGS : song name
    Returns: songs lyrics
    """
    print(songname)
    song_id = song_lyrics_id.get(songname)
    print(song_id)

    query = f"""SELECT * 
    FROM lyrics
    WHERE idlyrics = {song_id}
    """
    datos = pd.read_sql_query(query, engine)

    return datos.to_json(orient="records")



    






