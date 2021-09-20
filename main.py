from flask import Flask, request
from flask.json import jsonify
import random
import json
import tools.sqltools as sql
import tools.NLPtools as npl


app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo"

@app.route("/insertartists", methods=["POST"])
def insertartist():
    artist = request.form.get("artist")
    
    return sql.insertArtist(artist)

@app.route("/insertalbum", methods=["POST"])
def insertalbum():
    album = request.form.get("album")
    
    return sql.insertAlbum("album")

@app.route("/insertsong", methods=["POST"])
def insertsong():
    song = request.form.get("song")
    
    return sql.insertSong(song)

@app.route("/insertlyrics", methods=["POST"])
def insertlyric():
    lyrics = request.form.get("lyrics")
    
    return sql.insertlyrics(lyrics)

@app.route("/albums/<artistname>")
def artistsalbum(artistname):
    print("\n" * 20)
    print(artistname)
    albums = sql.artistsalbums(artistname)
    return albums

@app.route("/lyrics/<songname>")
def lyricssongname(songname):
    print("\n" * 20)
    print(songname)
    lyrics = sql.songslyrics(songname)
    return lyrics

@app.route("/NLP/<artist>/<song>")
def nlpsong(artist,song):
    print("\n" * 20)
    print(artist,song)
    song_nlp = npl.connecttablessong(artist,song)
    song_nlp["polarity"] = song_nlp.lyrics.apply(npl.nlp)
    song_nlp["compound"] = song_nlp.polarity.apply(npl.compound)
    song_nlp = song_nlp.to_json()
    song_nlp2 = json.loads(song_nlp)
    return song_nlp2["compound"]












if __name__ == '__main__':
    app.run(debug=True)