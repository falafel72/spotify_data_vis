from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def createPoints(filename):
  with open(filename) as fp:
    soup = BeautifulSoup(fp)

  rows = soup.find('table',{'id':'song-table'}).find('tbody').find_all('tr')
  songs = []

  for row in rows:
    cols = [col.get_text() for col in row.find_all('td')]
    entry = {'name':cols[1], 'artist':cols[2], 'data':[int(cols[8]),int(cols[5])]}
    songs.append(entry)

  points = [song['data'] for song in songs]
  x = [point[0] for point in points]
  y = [point[1] for point in points]

  return x,y

x1,y1 = createPoints("2016.html")
x2,y2 = createPoints("2017.html")
x3,y3 = createPoints("2018.html")

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x1,y1,c="r",label="2016",alpha=0.8)
ax1.scatter(x2,y2,c="g",label="2017",alpha=0.8)
ax1.scatter(x3,y3,c="b",label="2018",alpha=0.8)
plt.title("Songs in Spotify's 'Best Of' Playlists")
plt.xlabel("Valence")
plt.ylabel("Energy")
plt.legend(loc="lower right")
plt.show()
