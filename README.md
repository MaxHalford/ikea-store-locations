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

- [ ] Poland (11 missing)
- [x] France
- [x] Australia
- [ ] India (1 missing)
- [ ] Austria (7 missing)
- [ ] United Kingdom (21 missing)
- [ ] Macau (1 missing)
- [ ] Dominican Republic (4 missing)
- [ ] Indonesia (2 missing)
- [ ] Switzerland (9 missing)
- [x] Netherlands
- [ ] South Korea (4 missing)
- [ ] Egypt (1 missing)
- [ ] Belgium (2 missing)
- [ ] Israel (6 missing)
- [ ] Russia (14 missing)
- [ ] Japan (1 too many)
- [ ] Croatia (1 missing)
- [ ] Bahrain (1 missing)
- [ ] Qatar (1 missing)
- [ ] Saudi Arabia (6 missing)
- [x] Iceland
- [ ] Romania (2 missing)
- [ ] Sweden (20 missing)
- [ ] Finland (1 missing)
- [ ] Lithuania (3 missing)
- [ ] Cyprus (1 missing)
- [ ] Estonia (1 missing)
- [ ] Greece (5 missing)
- [ ] Czech Republic (then part of Czechoslovakia) (4 missing)
- [ ] Ireland (1 missing)
- [x] Denmark
- [ ] Jordan (1 missing)
- [x] Singapore
- [ ] United States (51 missing)
- [x] Canada
- [ ] Hungary (3 missing)
- [ ] Italy (21 missing)
- [ ] Latvia (1 missing)
- [ ] Germany (1 too many)
- [ ] Slovakia (then part of Czechoslovakia) (1 missing)
- [ ] Portugal (5 missing)
- [x] Norway
- [ ] Puerto Rico (3 missing)
- [ ] Thailand (2 missing)
- [ ] United Arab Emirates (3 missing)
- [ ] Taiwan (6 missing)
- [ ] Spain (1 missing)
- [ ] Malaysia (4 missing)
- [ ] Serbia (then part of Yugoslavia) (1 missing)
- [ ] Bulgaria (1 missing)
- [x] Kuwait
- [ ] Hong Kong (4 missing)
- [ ] Morocco (1 missing)
- [ ] China (18 missing)
- [ ] Turkey (6 missing)
