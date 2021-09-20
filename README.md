# OASIS API Project

The purpose of this project is to upload my info about the musical group Oasis and their solo parts to a API to be able to do a sentiment analysis of the songs when the group was together and whenthey split up because of their differences.

## Endpoints
Main connection to API, used to receive README. Must be added before endpoints 

http://127.0.0.1:5000/

## POST endpoints
Endpoint used to insert new artists into database that can later be accessed via API

/insertartists

Endpoint used to insert new albums into database that can later be accessed via API

/insertalbum

Endpoint used to insert new songs into database that can later be accessed via API

/insertsong

Endpoint used to insert new lyrics into database that can later be accessed via API

/insertlyrics

*These endpoints may not work from web browser, jupyter notebook or other software may have to be used to insert into this specific API *

## GET endpoints

/albums/_artistname_

Endpoint that returns the album names of the choosen artist from the DB via the API. _artistname_ is variable in API call.

/lyrics/_songname_

Endpoint that returns the lyrics of the choosen song from the DB via API. _songname_ is a variable in API call.

/NLP/_artist_/_song_

Endpoint that returns the natural language process of the choosen artist and song from the DB via API. _song_ and _artist_ are variables in API call. The NLP measures the positivity of each song made by a specific artist.

/NLP/_artist_

Endpoint that returns the natural language process of the choosen artist from the DB via API. _artist_ is variable in API call. The NLP measures the positivity of each artist throughout the songs found in the DB.


** ALL GET ENDPOINTS RETURN INFORMATION IN JSON FORMAT **

## Conclusions
From the NLP done for each artist, we can see that Noel Gallagher's High Flying Birds which is the group that Noel created after the split from Oasis has more negative lyrics then the songs when he was part of Oasis. Also Noel´s songs are more negative then his brothers songs after the split. This is most probably due to Noel´s group being formed very shortly after the split with Oasis and there being still some bitterness towards his brother after the bad breakup.

### Libraries
-	Pandas [here] (https://pandas.pydata.org/docs/)
-	Requests [here] (https://docs.python-requests.org/en/master/)
-	Json [here] (https://docs.python.org/3/library/json.html)
-   Flask [here] (https://flask.palletsprojects.com/en/2.0.x/)
-   DotEnv [here] (https://www.npmjs.com/package/dotenv)
-   SqlAlchemy [here] (https://docs.sqlalchemy.org/en/14/)






