# 🎵 Billboard Hot 100 to Spotify Playlist

This project automatically creates a **private Spotify playlist** containing the **Billboard Hot 100 songs** from any date you choose.  
It scrapes Billboard's historical charts and uses the **Spotify Web API** to find and add those songs to your Spotify account.

---

## 🚀 Features

- ✅ Scrapes Billboard’s *Hot 100* songs from any given date  
- ✅ Uses the Spotify Web API to search and match each song  
- ✅ Automatically creates a **private playlist** in your Spotify account  
- ✅ Adds all matched tracks from the chosen year/date  
- ✅ Clean and customizable Python implementation  

---

## 🧰 Technologies Used

- **Python 3.8+**
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) – for HTML scraping  
- [Requests](https://docs.python-requests.org/en/latest/) – for fetching Billboard charts  
- [Spotipy](https://spotipy.readthedocs.io/en/2.23.0/) – Python library for Spotify Web API  
- [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) – for OAuth credentials  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/billboard-to-spotify.git
cd billboard-to-spotify
