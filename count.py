import collections
import csv
import itertools

import bs4
import requests

# Scrape the number of stores per country from Wikipedia

url = 'https://en.wikipedia.org/wiki/List_of_countries_with_IKEA_stores?oldformat=true'
wiki = requests.get(url)
soup = bs4.BeautifulSoup(wiki.text, 'lxml')

expected = collections.Counter()
for items in soup.find('table').find_all('tr')[1:]:
    data = items.find_all(['th', 'td'])
    country = data[1].text.strip().replace('  ', ' ')
    n_stores = int(''.join(c for c in itertools.takewhile(str.isdigit, data[4].text.strip())))
    expected[country] = n_stores

# Count the number of collected stores per country

with open('stores.csv') as f:
    stores = list(csv.DictReader(f))
    stores = sorted(stores, key=lambda x: x['country'])
    collected = collections.Counter({
        country: len(list(stores))
        for country, stores in itertools.groupby(stores, lambda x: x['country'])
    })

for country in sorted(set(expected) | set(collected)):

    if expected[country] > collected[country]:
        print(f'- [ ] {country} ({expected[country] - collected[country]} missing)')

    elif collected[country] > expected[country]:
        print(f'- [ ] {country} ({collected[country] - expected[country]} too many)')

    else:
        print(f'- [x] {country}')
