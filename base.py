import json
import requests
import secret
from pprint import pprint

class lastFmSpotify:

    def __init__(self):
        self.token = secret.spotify_token()
        self.api_key = secret.last_fm_api()
        self.user_id = secret.spotify_user_id()
        self.spoitfy_headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"} 
        self.playlist_id = ""
        
        

    def fetchSongsFromLastfm(self):
        params = {'limit': 20, 'api_key': self.api_key}
        url = f"http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&format=json"
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("something went wrong ")
        res = response.json()
        for item in res['tracks']['track']:
            song = item['name'].title()
            artist = item['artist']['name'].title()
            self.get_uri_from_spoitfy(song, artist )


    
    def get_uri_from_spoitfy(self, song, artist):
        
        url = f"https://api.spotify.com/v1/search?query=track%3A{song}+artist%3A{artist}&type=track&offset=0&limit=20"
        response = requests.get(url, headers=self.spoitfy_headers)
        res = response.json()
        for item in res['tracks']['items']:
            print(item)

        

    def create_playlist(self):
        data ={
            "name": "LastFm playlist",
            "description": "بلاي لست جامده",
            "public": False
        }

   

    def add_songs_to_playlist(self):
        pass

    def list_songs_in_playlist(self):
        pass


d = lastFmSpotify()
d.fetchSongsFromLastfm()