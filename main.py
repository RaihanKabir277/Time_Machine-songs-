# # ---------------- Day 46 starts here ----------------
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
# ------- request the website -----------
favourable_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/" + favourable_year
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url=url, headers=header)
song_web_page = response.text

# ----scripting the website and find the values i need -------
soup = BeautifulSoup(song_web_page, "html.parser")
# song_titles = soup.find_all(name="h3", id="title-of-a-story")
# # print(song_titles)
# title_text = [song.get_text().strip() for song in song_titles]
# print(title_text)
#  ------- alternative way to find the same values ------
song_titles = soup.select(selector="li ul li h3")
song_names = [song.getText() for song in song_titles]
print(song_names)


# ------ add Spotify here ------

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username="Billboard to Spotify", 
    )
)

user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)



