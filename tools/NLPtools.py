import requests
import pandas as pd
from config.config import engine
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

artist_id = {"Oasis": 82,
            "Liam Gallagher" : 83,
            "Noel Gallagher´s flying birds": 84}

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

def connecttablessong(artist,song):
    artists_id = artist_id.get(artist)
    print(artist_id)
    song_id = song_lyrics_id.get(song)
    print(song_id)
    df= pd.read_sql_query(f"""

    SELECT idartists,idsongs,idlyrics,lyrics.lyrics
    FROM artists
    INNER JOIN songs
    ON artists.idartists = songs.artists_idartists
    INNER JOIN lyrics
    ON lyrics.idlyrics = songs.lyrics_idlyrics
    WHERE artist_name = "{artist}" AND idlyrics = {song_id};
    """, engine)
    return df

def nlp(col):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(col)

def compound(col_new):
    for j, v in col_new.items():
        print(j)
        if j == "compound":
            return v







def songanalysis(songname):
    data = requests.get('http://127.0.0.1:5000/lyrics/<songname>')
