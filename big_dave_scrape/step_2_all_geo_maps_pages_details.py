import glob
import json
import requests



pages = json.load(open('all_geo_maps_pages.json'))


complete_maps_ids = list(glob.glob('dave_maps/*.json'))
print(len(complete_maps_ids), 'total maps so far')
for p in pages:

	for m in p["@list"]:

		mapId = m['id']

		if f'dave_maps/{mapId}.json' not in complete_maps_ids:



			geoUrl = f'https://davidrumsey.georeferencer.com/api/v1/georeferences/{mapId}'
			geoMetaUrl = f'https://davidrumsey.georeferencer.com/api/v1/maps/{mapId}'

			print(geoUrl)
			daveData = {}

			daveData['urlGeo'] = geoUrl
			daveData['urlMeta'] = geoMetaUrl

			geoUrlresp = requests.get(url=geoUrl)
			urlMetaresp = requests.get(url=geoMetaUrl)

			try:


				geoUrlrespJson = geoUrlresp.json()
				urlMetarespJson = urlMetaresp.json()
			except:
				print('error on ', mapId)

			
			daveData['geoMeta'] = urlMetarespJson
			daveData['geoData'] = geoUrlrespJson
			json.dump(daveData,open(f'dave_maps/{mapId}.json','w'),indent=2)
		else:
			print('skipping',mapId)