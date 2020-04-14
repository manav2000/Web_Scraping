from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq
import pandas as pd

# URl to web scrap from.
page_url = 'https://gaana.com/playlist/gaana-dj-bollywood-top-50-1'

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
page_soup = soup(uClient.read(), "html.parser")

top50 = page_soup.find('div', {'class': 's_c'})
print(top50)

# finds each song from the page
songs = top50.find_all('li', {'class': 'draggable'})
print(len(songs))

print(songs[0].find('a', {'data-type': 'playSong'}).get_text())
print(songs[0].find('a', {'data-type': 'url'}).get_text())
print(songs[0].find('a', {'class': 'desktop sng_c'}).get_text())

# extracting titles
titles = [song.find('a', {'data-type': 'playSong'}).get_text()
          for song in songs]
print(titles)

# extracting artists
artists = [song.find('a', {'data-type': 'url'}).get_text() for song in songs]
print(artists)

# extracting time
time = [song.find('a', {'class': 'desktop sng_c'}).get_text()
        for song in songs]
print(time)

# creates pandas dataframe
gannaTop50 = pd.DataFrame({'Title': titles, 'Artist': artists, 'Time': time})
print(gannaTop50)

# convert pandas dataframe to csv file
gannaTop50.to_csv('ganna_Top50.csv')

print('Web Scraping Done')
