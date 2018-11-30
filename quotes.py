import csv
import requests
import re
from bs4 import BeautifulSoup
with open('top.csv', newline="") as top:
    file = csv.reader(top, delimiter=',', quotechar='"')
    for movie in file:
        print('starting for' + movie[0])
        newFile = csv.writer(open('movies/' + movie[0] + '.csv', 'w'))
        page = requests.get(movie[1])
        parsed = BeautifulSoup(page.text, 'html.parser')
        container = parsed.find('div', {'class': 'list'})
        quotes = container.find_all('div', {'class': 'sodavote'})
        for quote in quotes:
            text = quote.find('div', {'class': 'sodatext'}).text
            likes = container.find('a', {'class': 'interesting-count-text'}).text
            if likes:
                count = re.findall(r'\d+', likes) or [0]
            else:
                count = [0]
            newFile.writerow([text, count[0]])
        print('finished for ' + movie[0])
