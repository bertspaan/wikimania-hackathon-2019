import requests
import json


# this script grabs the data from the dave site

all_data = json.load(open('dave_scrape_with_dave_url.json'))


dave_data = {}
dave_count = 0

for d in all_data:

	if 'daveDataUrl' in d:

		if d['daveDataUrl'][-1] != '/':
			d['daveDataUrl'] = d['daveDataUrl'] + '/'

		if d['daveDataUrl'] not in dave_data:

			daveData = {}


			page_response = requests.get(d['daveDataUrl'], timeout=5,allow_redirects=False)

			print(d['daveDataUrl'])
			
			if 'Location' not in page_response.headers:
				d['daveError'] = '404 not found'
				continue

			mapId = page_response.headers['Location'].split('/maps/')[1].replace('/view','')


			geoUrl = f'https://davidrumsey.georeferencer.com/api/v1/georeferences/{mapId}'
			geoMetaUrl = f'https://davidrumsey.georeferencer.com/api/v1/maps/{mapId}'

			daveData['urlGeo'] = geoUrl
			daveData['urlMeta'] = geoMetaUrl

			geoUrlresp = requests.get(url=geoUrl)
			urlMetaresp = requests.get(url=geoMetaUrl)

			try:


				geoUrlrespJson = geoUrlresp.json()
				urlMetarespJson = urlMetaresp.json()
			except:
				d['daveError'] = 'Sign in required?'
				continue


			daveData['geoMeta'] = urlMetarespJson
			daveData['geoData'] = geoUrlrespJson

			print(daveData)

			dave_data[d['daveDataUrl']] = daveData

			d['daveData'] = daveData

			# page_response = requests.get(d['dave'], timeout=5)
			# # here, we fetch the content from the url, using the requests library
			# page_content = BeautifulSoup(page_response.content, "html.parser")

			# geo_ref_link = page_content.find('a',attrs={'id':'GeoreferencerButton'})

			# if geo_ref_link != None:
					
			# 	d['daveDataUrl'] = geo_ref_link['href']

			# 	dave_data[d['dave']] = geo_ref_link['href']
			dave_count+=1


		else:

			d['daveData'] = dave_data[d['daveDataUrl']]

# 	print(d['dave'])

	if dave_count % 25 == 0:
		json.dump(all_data,open('dave_scrape_with_dave_data.json','w'),indent=2)


json.dump(all_data,open('dave_scrape_with_dave_data.json','w'),indent=2)

	# this is the url that we've already determined is safe and legal to scrape from.

	#we use the html parser to parse the url content and store it in a variable.
	

	# lis = page_content.find("ol")
	# lis = lis.find_all("li")

	# for li in lis:
	# 	a = li.find_all("a")

	# 	dav_link = a[0]['href']
	# 	wikicommonsFile = a[1]['href'].replace('/wiki/','')


	# 	resp = requests.get(url=f'https://commons.wikimedia.org/w/api.php?action=query&titles={wikicommonsFile}&prop=imageinfo&iiprop=extmetadata&format=json')

		
	# 	print(resp.content)
	# 	print(f'https://commons.wikimedia.org/w/api.php?action=query&titles={wikicommonsFile}&prop=imageinfo&iiprop=extmetadata&format=json')
	# 	data = resp.json()		
		

	# 	all_data.append({'commons':wikicommonsFile, 'dave':dav_link,'commonsMetadata':data})

	# 	print(len(all_data))
	# 	if len(all_data) % 100 == 0:

	# 		json.dump(all_data,open('dave_scrape.json','w'),indent=2)