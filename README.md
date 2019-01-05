# Spotify Playlist Data Grapher
Takes Echo Nest data from playlists as shown with [http://sortyourmusic.playlistmachinery.com/]. Currently graphs valence and energy in a scatter plot. 

## Usage
Clone the repo: 
```
git clone https://github.com/falafel72/spotify_data_vis
```
Install matplotlib and BeautifulSoup if you don't have them already: 
```
pip3 install bs4
pip3 install matplotlib
```

Scraping is a work in progress, currently can only parse local html files stored in the same directory.

Then run: 
```
python3 graph.py
```

## Potential Improvements
 - Automatic login and playlist search
 - Use the Spotify API
