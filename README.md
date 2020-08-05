# IKEA store locations

This is an ongoing effort to list and analyse the locations of every IKEA store in the world. The current goal is simply to locate each store. The pipe dream is to then do some analysis, for instance by correlating the distance to the closest IKEA with house prices. As far as I can tell, the location of each IKEA store isn't available elsewhere. There's a [Wikipedia article](https://www.wikiwand.com/en/List_of_countries_with_IKEA_stores) that indicates the number of IKEA stores per country, but doesn't provide more detail. Most countries have a dedicated page that lists all their stores, for instance see [this](https://www.ikea.com/fr/fr/stores/) page for France.

The current process begins by copy/paste a list of store names for a given country into the `store-names.json` file. Then, the `run.py` script goes through the store names of each country and applies [geocoding](https://www.wikiwand.com/en/Geocoding) to find an address. All the information is stored into `stores.csv`. The `stores.geojson` file is the [GeoJSON](https://geojson.org/) equivalent of `stores.csv`. The contents of `stores.geojson` are fetched in `index.html` from GitHub. The map is served [here](https://maxhalford.github.io/ikea-store-locations/). Additionally, it turns out that GitHub is capable of rendering GeoJSON files, which you can see in action [here](https://github.com/MaxHalford/ikea-store-locations/blob/master/stores.geojson).

**TLDR**

```sh
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python run.py
```

As this is an ongoing effort, every store location isn't yet accounted for. Of course, pull requests are welcome. Here is a checklist of the countries to go through:

- [ ] Sweden
- [x] Norway
- [x] Denmark
- [ ] Switzerland
- [x] Japan
- [x] Germany
- [x] Australia
- [x] Canada
- [ ] Hong Kong
- [ ] Austria
- [x] Singapore
- [x] Netherlands
- [x] Spain
- [x] Iceland
- [x] France
- [ ] Saudi Arabia
- [x] Belgium
- [x] Kuwait
- [ ] United States
- [ ] United Kingdom
- [ ] Italy
- [ ] Hungary
- [ ] Poland
- [ ] Czech Republic(then part ofCzechoslovakia)
- [ ] Serbia(then part ofYugoslavia)
- [ ] United Arab Emirates
- [ ] Slovakia(then part ofCzechoslovakia)
- [ ] Taiwan
- [ ] Finland
- [ ] Malaysia
- [ ] China
- [ ] Russia
- [ ] Israel
- [ ] Greece
- [ ] Portugal
- [ ] Turkey
- [ ] Romania
- [ ] Cyprus
- [ ] Ireland
- [ ] Dominican Republic
- [ ] Bulgaria
- [ ] Thailand
- [ ] Macau
- [ ] Lithuania
- [ ] Puerto Rico
- [ ] Egypt
- [ ] Qatar
- [ ] Jordan
- [ ] Croatia
- [ ] Indonesia
- [ ] South Korea
- [ ] Morocco
- [ ] India
- [ ] Latvia
- [ ] Bahrain
- [ ] Estonia
