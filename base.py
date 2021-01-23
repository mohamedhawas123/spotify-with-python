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
        self.song_info = {}
        self.uries = []

        
        

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
            self.song_info[song] = artist
        self.get_uri_from_spoitfy()


    
    def get_uri_from_spoitfy(self):
        for song, artist in self.song_info.items():

            url = f"https://api.spotify.com/v1/search?query=track%3A{song}+artist%3A{artist}&type=track&offset=0&limit=20"
            response = requests.get(url, headers=self.spoitfy_headers)
            print(response.status_code)
            res = response.json()
            output_uri = res['tracks']['items']
            uri = output_uri[0]['uri']
            self.uries.append(uri)

        

    def create_playlist(self):
        data ={
            "name": "LastFm playlist",
            "description": " so nice",
            "public": True
        }

        data = json.dumps(data)

        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = requests.post(url, data=data, headers=self.spoitfy_headers)
        if response.status_code == 200:
            res = response.json()
            self.playlist_id = res['id']
            print("done your playlist")
        else:
            print(response.text)


   

    def add_songs_to_playlist(self):
        uris_list = json.dumps(self.uries)
        url = f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks"
        reponse = requests.post(url, data=uris_list, headers={self.spoitfy_headers})
        if reponse.status_code == 201:
            print("done")


    def list_songs_in_playlist(self):
        pass


d = lastFmSpotify()
d.create_playlist()