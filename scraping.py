from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq
import pandas as pd
page_url = 'https://gaana.com/playlist/gaana-dj-bollywood-top-50-1'
uClient = uReq(page_url)
page_soup = soup(uClient.read(), "html.parser")
top50  = page_soup.find('div', {'class': 's_c' })
print(top50)
songs = top50.find_all('li', {'class': 'draggable'})
print(len(songs))
print(songs[0].find('a', {'data-type': 'playSong'}).get_text())
print(songs[0].find('a', {'data-type': 'url'} ).get_text())
print(songs[0].find('a', {'class': 'desktop sng_c'} ).get_text())
titles = [song.find('a', {'data-type': 'playSong'} ).get_text() for song in songs ]
print(titles)
artists = [song.find('a', {'data-type': 'url'} ).get_text() for song in songs ]
print(artists)
time = [song.find('a', {'class': 'desktop sng_c'} ).get_text() for song in songs]
print(time)
gannaTop50 = pd.DataFrame({'Title': titles, 'Artist': artists, 'Time': time})
print(gannaTop50)
gannaTop50.to_csv('ganna_Top50.csv')
