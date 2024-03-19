import configparser
import spotipy
from spotipy import SpotifyOAuth

SCOPE = ['user-library-read',
         'user-follow-read',
         'user-top-read',
         'playlist-read-private',
         'playlist-read-collaborative',
         'playlist-modify-public',
         'playlist-modify-private']

properties = configparser.ConfigParser()
properties.read('config.ini')

REDIRECT_URI = properties.get('CONFIG', 'REDIRECT_URI')
CLIENT_ID = properties.get('CONFIG', 'CLIENT_ID')
CLIENT_SECRET = properties.get('CONFIG', 'CLIENT_SECRET')

def getAPIObject():
    auth_manager = SpotifyOAuth(
        scope=SCOPE,
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

    sp = spotipy.Spotify(auth_manager=auth_manager)

    return sp