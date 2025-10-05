# ---------------- Day 46 starts here ----------------
from bs4 import BeautifulSoup
import requests

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




