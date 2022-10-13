# Mood-enhancer
detect facial expressions and play music and binaural beats in an attempt to improve the mood.

We use openCV to capture the face using the camera, then by using the deepface module, we detect the mood and display the dominant emotion.

To reccomend songs, the user has to enter the link to their favorite playlist, and the algorithm will use the a spotify API ( spotipy ) to anaylize different features of the song and learn the 'taste' of music the user likes. Then it will search through a database of 40,000+ songs to look for most similar songs and sort them with increasing positivity. 
In this way, the song reccomendations are according to the user's taste of music and at the same time positive and uplifting.

Hence helping the user enhance their mood if their dominant emotion is negative.
