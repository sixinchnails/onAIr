import tekore as tk
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def authorize():
    CLIENT_ID = config['SPOTIFY']['CLIENT_ID']
    CLIENT_SECRET = config['SPOTIFY']['CLIENT_SECRET']
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)

    return tk.Spotify(app_token)
