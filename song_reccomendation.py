import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 

client_id = ''
client_secret = ''
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getTrackFeatures(id):
    '''
    gets the features of a particular song
    input: song ID
    output: list of features
    '''
    meta = sp.track(id)
    features = sp.audio_features(id)

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    valence = features[0]['valence']
    track = [name, album, artist, release_date, length, danceability, acousticness, 
            energy, instrumentalness, liveness, loudness, speechiness, valence]
    
    '''
    track = [["name",name],['album', album], ["artists",artist], ["release date",release_date],['length' ,length,],
           ["popularity",popularity],["danceability",danceability] ,['acousticness',acousticness] , 
           ['energy',energy], ['instrumentalness',instrumentalness],['liveness',liveness] , 
           ['loudness',loudness] ,['speechiness',speechiness] ,['tempo',tempo] ,
          ['valence',valence]]   
    ''' 
    return track
    
def summarize_playlist(url):
    playlist_URI = url.split("/")[-1].split("?")[0]
    track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]] #gets the URL of songs in a playlist
    playlist_data = pd.DataFrame(columns = ['name','album', 'artist', 'release_date', 'length',
                                            'danceability', 'acousticness', 'energy', 'instrumentalness',
                                            'liveness', 'loudness', 'speechiness', 'valence'])
    
    for i in track_uris:
        data = getTrackFeatures(i)
        playlist_data.loc[len(playlist_data)] = data #adding song data to a dataframe
    playlist_features = playlist_data.iloc[:,5:].mean() #gets the average of the features of the plalist data
    return playlist_features
    
    user_features = summarize_playlist('https://open.spotify.com/playlist/2H5NdSB7O8tsxzUBHd7R0N?si=b0189d6073404a99') #link to the favorite playlist

def comparison(user_features, database): # compare user features with songs in the database
    loss = []
    for i in range(len(database)):
        loss.append(((database.iloc[i] - user_features)**2).sum())
    return loss

def playlist_songs(loss, database): # selecct the songs for the playlist
    losses = list(loss)
    losses.sort()
    x = losses[:10]
    for i in x:
        a = loss.index(i)
        print(df.iloc[a]['song_name'])

import requests
'''
authorization bearer code is temporary

'''
def create_playlist(): # create a playlist
    import json
    user_id = ""
    endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    request_body = json.dumps({
              "name": "Indie bands like Franz Ferdinand but using Python",
              "description": "My first programmatic playlist, yooo!",
              "public": False # let's keep it between us - for now
            })
    response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                            "Authorization":"Bearer BQA3a_wqUx3SR18K0lZLjbxij6tf7DDCYecXdCVpwSfsPyHSinZg_lCEKdmWHMdJo8M1krI7JCOEHyKb1e7yb0VihIEISEm6N-nj956eHTKI-_99e7pKMsDUNDIzzdg6DbWfRScfV_oJFliTjABNshgVhxg2sm4D7-RptqM9INU-Vb0skwnBgdTrQzHo8kvjVSAgeT7QkkColsZVDf3rByRSJDB_raDwL2Nlr0en"})
    playlist_id = response.json()['id']
    endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    request_body = json.dumps({
              "uris" : uris
            })
    response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                            "Authorization":"Bearer BQA3a_wqUx3SR18K0lZLjbxij6tf7DDCYecXdCVpwSfsPyHSinZg_lCEKdmWHMdJo8M1krI7JCOEHyKb1e7yb0VihIEISEm6N-nj956eHTKI-_99e7pKMsDUNDIzzdg6DbWfRScfV_oJFliTjABNshgVhxg2sm4D7-RptqM9INU-Vb0skwnBgdTrQzHo8kvjVSAgeT7QkkColsZVDf3rByRSJDB_raDwL2Nlr0en"})

    print(response.status_code)
