import json
import requests
import secret


class lastFmSpotify:

    def __init__(self):
        self.token = secret.spotify_token
        self.api_key = secret.last_fm_api
        self.user_id = secret.spotify_user_id
        self.spoitfy_headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"} 
        self.playlist_id = ""
        

    def fetchSongsFromLastfm(self):
        pass
    
    def get_uri_from_spoitfy(self):

        pass

    def create_playlist(self):
        pass

   

    def add_songs_to_playlist(self):
        pass

    def list_songs_in_playlist(self):
        pass