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
    
    user_features = summarize_playlist('https://open.spotify.com/playlist/2H5NdSB7O8tsxzUBHd7R0N?si=b0189d6073404a99')
