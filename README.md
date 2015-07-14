#tile-size

Quick & dirty analysis of bandwidth for urban institute mapbox maps

- Parses browser [har](https://en.wikipedia.org/wiki/.har) files for 3 different urban mapbox projects ([shotspotter](http://datatools.urban.org/features/everydayviolence/), [ncbd inequality](http://datatools.urban.org/features/ncdb/top-bottom/index.html#8/38.940/-89.209), [ncdb immigration](http://datatools.urban.org/features/ncdb/immigrants-reshaping-residential-segregation/), searches for .png requests (mostly tiles, the rest get washed out in the average).
- Grabs file size from response, ignores 0b pngs (404's or cached files), gets average file size.
- Based on mapbox usage stats (in config.py), calculates avg monthly data usage for tiles, as well as peak hourly data usage