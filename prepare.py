import requests
# import re
from collections import namedtuple
from random import randint
from bs4 import BeautifulSoup

Color = namedtuple('Color', ['red', 'green', 'blue'])


def random_colors():
    return Color(randint(0, 255), randint(0, 255), randint(0, 255))


page = requests.get('https://www.imdb.com/chart/top')
soup = BeautifulSoup(page.text, 'html.parser')
titles = soup.find_all('td', {'class': 'titleColumn'})
selection = randint(1, len(titles))
link = titles[selection].find('a')
quote_url = 'https://www.imdb.com' + link.get('href').split("?")[0] + 'quotes'
title = link.contents[0]
print('opening page ' + quote_url + 'for movie ' + title);
page = requests.get(quote_url)
parsed = BeautifulSoup(page.text, 'html.parser')
container = parsed.find('div', {'class': 'list'})
quotes = container.find_all('div', {'class': 'sodavote'})
quote_selection = randint(1, len(quotes));
text = quotes[quote_selection].find('div', {'class': 'sodatext'}).text
# likes = container.find('a', {'class': 'interesting-count-text'}).text
# if likes:
#    count = re.findall(r'\d+', likes) or [0]
# else:
#    count = [0]
print(text);
colors = random_colors()
for color in colors:
    print(color);
