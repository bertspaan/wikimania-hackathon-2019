
import requests
import json

url = "https://davidrumsey.georeferencer.com/api/v1/display?start=gANYIAAAADIwMTktMDgtMTRUMTc6MTQ6MTYuMzQzMDAyKzAwOjAwcQBN47CGcQEu"
counter = 0
pages = []
while url != None and url != 'None':



	print(url)
	r = requests.get(url=url)
	page = r.json()

	pages.append(page)

	try:
		url = page['next']
	except:
		json.dump(pages,open('all_geo_maps_pages.json','w'),indent=2)



	counter+=1

	if counter % 100 == 0:
		json.dump(pages,open('all_geo_maps_pages.json','w'),indent=2)


json.dump(pages,open('all_geo_maps_pages.json','w'),indent=2)

	

