# IKEA store locations

This is an ongoing effort to list and analyse the locations of every IKEA store in the world. The current goal is simply to locate each store. The pipe dream is to then do some analysis, for instance by correlating the distance to the closest IKEA with house prices. As far as I can tell, the location of each IKEA store isn't available elsewhere. There's a [Wikipedia article](https://www.wikiwand.com/en/List_of_countries_with_IKEA_stores) that indicates the number of IKEA stores per country, but doesn't provide more detail. Most countries have a dedicated page that lists all their stores, for instance see [this](https://www.ikea.com/fr/fr/stores/) page for France.

The current process begins by copy/paste a list of store names for a given country into the `store-names.json` file. Then, the `geocode.py` script goes through the store names of each country and applies [geocoding](https://www.wikiwand.com/en/Geocoding) to find detailed addresses and the geographical coordinates that go along. All the information is stored into `stores.csv`. The `stores.geojson` file is the [GeoJSON](https://geojson.org/) equivalent of `stores.csv`. The contents of `stores.geojson` are fetched in `index.html` from GitHub. The map is served [here](https://maxhalford.github.io/ikea-store-locations/). Additionally, it turns out that GitHub is capable of rendering GeoJSON files, which you can see in action [here](https://github.com/MaxHalford/ikea-store-locations/blob/master/stores.geojson). Finally, the `count.py` is used to check that the number of collected IKEA locations per country is correct, by using as a reference the aforementioned [Wikipedia article](https://www.wikiwand.com/en/List_of_countries_with_IKEA_stores).

**TLDR**

```sh
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python geocode.py
python count.py
```

Because this is an ongoing effort, every store location isn't yet accounted for. Of course, pull requests are welcome. Here is the current state of things, as given by the `count.py` script:

- [x] Australia
- [ ] Austria (7 missing)
- [ ] Bahrain (1 missing)
- [ ] Belgium (2 missing)
- [ ] Bulgaria (1 missing)
- [x] Canada
- [ ] China (18 missing)
- [ ] Croatia (1 missing)
- [ ] Cyprus (1 missing)
- [ ] Czech Republic (then part of Czechoslovakia) (4 missing)
- [x] Denmark
- [ ] Dominican Republic (4 missing)
- [ ] Egypt (1 missing)
- [ ] Estonia (1 missing)
- [ ] Finland (1 missing)
- [x] France
- [ ] Germany (1 too many)
- [ ] Greece (5 missing)
- [ ] Hong Kong (4 missing)
- [ ] Hungary (3 missing)
- [x] Iceland
- [ ] India (1 missing)
- [ ] Indonesia (2 missing)
- [ ] Ireland (1 missing)
- [ ] Israel (6 missing)
- [ ] Italy (21 missing)
- [ ] Japan (1 too many)
- [ ] Jordan (1 missing)
- [x] Kuwait
- [ ] Latvia (1 missing)
- [ ] Lithuania (3 missing)
- [ ] Macau (1 missing)
- [ ] Malaysia (4 missing)
- [ ] Morocco (1 missing)
- [x] Netherlands
- [x] Norway
- [ ] Poland (11 missing)
- [ ] Portugal (5 missing)
- [ ] Puerto Rico (3 missing)
- [ ] Qatar (1 missing)
- [ ] Romania (2 missing)
- [ ] Russia (14 missing)
- [ ] Saudi Arabia (6 missing)
- [ ] Serbia (then part of Yugoslavia) (1 missing)
- [x] Singapore
- [ ] Slovakia (then part of Czechoslovakia) (1 missing)
- [ ] South Korea (4 missing)
- [ ] Spain (1 missing)
- [ ] Sweden (20 missing)
- [ ] Switzerland (9 missing)
- [ ] Taiwan (6 missing)
- [ ] Thailand (2 missing)
- [ ] Turkey (6 missing)
- [ ] United Arab Emirates (3 missing)
- [ ] United Kingdom (21 missing)
- [ ] United States (51 missing)
