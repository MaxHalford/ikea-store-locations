import csv
import json

from geopy import geocoders
import pycountry
import termcolor


# We first load store-names.json, which is a list of store names within each country
with open('store-names.json') as f:
    store_names = json.load(f)


# We load the existing stores in order to skip them when we encounter them in store-names.json
with open('stores.csv') as f:
    cache = {
        (store['country'], store['name']): store
        for store in csv.DictReader(f)
    }


with open('stores.csv', 'w') as f:

    locator = geocoders.Nominatim(user_agent='IKEA locations')

    fieldnames = ['country', 'name', 'address', 'latitude', 'longitude']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    # Write the cached items
    for store in cache.values():
        writer.writerow(store)

    for country, names in store_names.items():

        country = pycountry.countries.search_fuzzy(country)[0]

        for name in names:

            # Skip the store if it's in the cache
            if (country.name, name) in cache:
                print(termcolor.colored(f'{country.name} - {name}', 'green'))
                continue

            address = f'Ikea {name}'
            location = locator.geocode(address, country_codes=country.alpha_2.lower())

            if location is None:
                print(termcolor.colored(f'{country.name} - {name}', 'red'))
                continue

            writer.writerow({
                'country': country.name,
                'name': name,
                'address': location.address,
                'latitude': location.latitude,
                'longitude': location.longitude
            })
            print(termcolor.colored(f'{country.name} - {name}', 'green'))

    for country, names in store_names.items():
        print(f'{country}: {len(names)}')


# Now we create stores.geojson, which is the GeoJSON equivalent of stores.csv
with open('stores.csv') as f:
    stores = list(csv.DictReader(f))

geojson = {
    'type': 'FeatureCollection',
    'features': [
        {
            'type': 'Feature',
            'properties': {
                'country': store['country'],
                'name': store['name'],
                'address': store['address']
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    float(store['longitude']),
                    float(store['latitude'])
                ]
            }
        }
        for store in stores
    ]
}

with open('stores.geojson', 'w') as f:
    json.dump(geojson, f)
