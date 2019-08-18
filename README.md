# Wikimania Hackathon 2019

Tools, data and scripts created during the Wikimania Hackathon 2019.

See [this Phabricator task](https://phabricator.wikimedia.org/T227036) for more details about the project proposal.

- JSON specification: https://github.com/bertspaan/georectify-json-spec
- Georectify web service: https://github.com/bertspaan/georectify-service
- Presentation: https://bertspaan.nl/wikimania-hackathon-2019/presentation
- Example map + data:
    - Map image: https://commons.wikimedia.org/wiki/File:Pigot_and_Co_(1842)_p2.138_-_Map_of_Lancashire.jpg
    - GCPs: https://commons.wikimedia.org/wiki/Data:Pigot_and_Co_(1842)_p2.138_-_Map_of_Lancashire.gcps.tab
    - Pixel mask: https://commons.wikimedia.org/wiki/Data:Pigot_and_Co_(1842)_p2.138_-_Map_of_Lancashire.mask.tab
    - Map mask: https://commons.wikimedia.org/wiki/Data:Pigot_and_Co_(1842)_p2.138_-_Map_of_Lancashire.mask.map

## Data

Convert scraped David Rumsey data to [georectify-json-spec](https://github.com/bertspaan/georectify-json-spec):

    gzcat big_dave_scrape/all_geo_data.ndjson.gz | node david-rumsey-transform.js > david-rumsey.georectify-json-spec.ndjson

Then, use the [georectify-service](https://github.com/bertspaan/georectify-service) running on http://localhost:8080 to convert these JSON files to GeoJSON:

    node david-rumsey-masks.js < david-rumsey.georectify-json-spec.ndjson > david-rumsey.masks.geojson
