from bs4 import BeautifulSoup
import requests
import json


# this script finds the geo ref url on the dave site


all_data = json.load(open('dave_scrape.json'))


dave_data = {}
dave_count = 0

for d in all_data:

	if d['dave'] not in dave_data:


		page_response = requests.get(d['dave'], timeout=5)
		# here, we fetch the content from the url, using the requests library
		page_content = BeautifulSoup(page_response.content, "html.parser")

		geo_ref_link = page_content.find('a',attrs={'id':'GeoreferencerButton'})

		if geo_ref_link != None:
				
			d['daveDataUrl'] = geo_ref_link['href']

			dave_data[d['dave']] = geo_ref_link['href']
			dave_count+=1


	else:

		d['daveDataUrl'] = dave_data[d['dave']]

	print(d['dave'])

	if dave_count % 25 == 0:
		json.dump(all_data,open('dave_scrape_with_dave_url.json','w'),indent=2)


json.dump(all_data,open('dave_scrape_with_dave_url.json','w'),indent=2)
