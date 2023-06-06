import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util




#Info on scopes can be found here: https://developer.spotify.com/documentation/web-api/concepts/scopes#user-modify-playback-state
SCOPE = 'user-read-playback-state user-modify-playback-state'

# These are personal and will need to filled out by you
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'YOUR_LOCAL_HOST'

# Spotify Device ID of agent
# Can find it by printing sp.devices()
DEVICE_ID = "YOUR_DEVICE_ID"

    

def pause_playback():
    sp_oauth = SpotifyOAuth(client_id = CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)
    access_token = sp_oauth.get_cached_token()
    sp = Spotify(auth_manager=sp_oauth)
    isPlay = sp.current_user_playing_track()

    if isPlay['is_playing']:
        sp.pause_playback(device_id=DEVICE_ID)


def start_playback():
    sp_oauth = SpotifyOAuth(client_id = CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)
    access_token = sp_oauth.get_cached_token()
    sp = Spotify(auth_manager=sp_oauth)
    isPlay = sp.current_user_playing_track()

    if not isPlay['is_playing']:
        sp.start_playback(device_id=DEVICE_ID)

