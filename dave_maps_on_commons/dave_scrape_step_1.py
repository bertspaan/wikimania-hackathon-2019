from bs4 import BeautifulSoup
import requests
import json


# this script web scrapes the external links search page on commons 

urls = ['https://commons.wikimedia.org/w/index.php?title=Special:LinkSearch&limit=500&offset=0&target=http%3A%2F%2Fwww.davidrumsey.com%2Fluna%2Fservlet%2Fdetail',
		'https://commons.wikimedia.org/w/index.php?title=Special:LinkSearch&limit=500&offset=500&target=http%3A%2F%2Fwww.davidrumsey.com%2Fluna%2Fservlet%2Fdetail',
		'https://commons.wikimedia.org/w/index.php?title=Special:LinkSearch&limit=500&offset=1000&target=http%3A%2F%2Fwww.davidrumsey.com%2Fluna%2Fservlet%2Fdetail',
		'https://commons.wikimedia.org/w/index.php?title=Special:LinkSearch&limit=500&offset=1500&target=http%3A%2F%2Fwww.davidrumsey.com%2Fluna%2Fservlet%2Fdetail'
		]


pages = []

all_data = []

for url in urls:



	# this is the url that we've already determined is safe and legal to scrape from.
	page_response = requests.get(url, timeout=5)
	# here, we fetch the content from the url, using the requests library
	page_content = BeautifulSoup(page_response.content, "html.parser")
	#we use the html parser to parse the url content and store it in a variable.
	

	lis = page_content.find("ol")
	lis = lis.find_all("li")

	for li in lis:
		a = li.find_all("a")

		dav_link = a[0]['href']
		wikicommonsFile = a[1]['href'].replace('/wiki/','')


		resp = requests.get(url=f'https://commons.wikimedia.org/w/api.php?action=query&titles={wikicommonsFile}&prop=imageinfo&iiprop=extmetadata&format=json')

		
		print(resp.content)
		print(f'https://commons.wikimedia.org/w/api.php?action=query&titles={wikicommonsFile}&prop=imageinfo&iiprop=extmetadata&format=json')
		data = resp.json()		
		

		all_data.append({'commons':wikicommonsFile, 'dave':dav_link,'commonsMetadata':data})

		print(len(all_data))
		if len(all_data) % 100 == 0:

			json.dump(all_data,open('dave_scrape.json','w'),indent=2)