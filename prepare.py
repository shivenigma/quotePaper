import requests
import csv
from bs4 import BeautifulSoup
page = requests.get('https://www.imdb.com/chart/top')
soup = BeautifulSoup(page.text, 'html.parser')
titles = soup.find_all('td', {'class': 'titleColumn'})
file = csv.writer(open('top.csv', 'w'))
for title in titles:
    link = title.find('a')
    # quotes sample URL, needs to use regex
    # https://www.imdb.com/title/tt0111161/quotes/
    file.writerow([link.contents[0], 'https://www.imdb.com' + link.get('href').split("?")[0] + 'quotes'])
print('done');