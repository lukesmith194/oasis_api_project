# OASIS API Project

The purpose of this project is to upload my info about the musical group Oasis and their solo parts to a API to be able to do a sentiment analysis of the songs when the group was together and whenthey split up because of their differences.

## Endpoints
Main connection to API, used to recieve README. Must be added before endpoints 

http://127.0.0.1:5000/

### POST endpoints
Endpoint used to insert new artists into database that can later be accessed via API

/insertartists

Endpoint used to insert new albums into database that can later be accessed via API

/insertalbum

Endpoint used to insert new songs into database that can later be accessed via API

/insertsong

Endpoint used to insert new lyrics into database that can later be accessed via API

/insertlyrics

*These endpoints may not work from web browser, jupyter notebook or other software may have to be used to insert into this specific API *

### GET endpoints

/albums/_artistname_

Endpoint that returns the album names of the choosen artist from the DB via the API. _artistname_ is variable in API call.

/lyrics/_songname_

Endpoint that returns the lyrics of the choosen song from the DB via API. _songname_ is a variable in API call.

** ALL GET ENDPOINTS RETURN INFORMATION IN JSON FORMAT **







