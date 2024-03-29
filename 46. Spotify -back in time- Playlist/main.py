from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_SECRET_ID")

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.find_all("h3", {"class": "a-no-trucate"})
song_list = [song.getText() for song in song_names]

# Spotify Authentication
sp = spotipy.Spotify(
	auth_manager=SpotifyOAuth(
		scope="playlist-modify-private",
		redirect_uri="http://example.com",
		client_id=SPOTIFY_CLIENT_ID,
		client_secret=SPOTIFY_CLIENT_SECRET,
		show_dialog=True,
		cache_path="token.txt"
	)
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_list:
	result = sp.search(q=f"track:{song} year:{year}", type="track")
	# print(result)
	try:
		uri = result["tracks"]["items"][0]["uri"]
		song_uris.append(uri)
	except IndexError:
		print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False
)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
