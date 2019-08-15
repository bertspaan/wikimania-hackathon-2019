
import re
import json
import requests

id_lookup = {}
with open('mapwarper.objects.ndjson') as input:
	for line in input:
		d = json.loads(line)
		# print(d)
		if 'data' in d:
			if 'imageId' in d['data']:
				imageid = str(d['data']['imageId'])
				id_lookup[imageid] = d

record_count = 0
all_data = []
with open('nypl_images.xml') as input:

	record = []


	for line in input:

		if '</page>' in line:
			
			# if record_count % 100 == 0:
				# print(record_count)
			record.append(line)


			xml = "".join(record)
			
			r1 = re.findall(r"DigitalID=(.*?)\n",xml)
			r2 = re.findall(r"{{NYPL-image\|(.*?)}}",xml)
			r3 = re.findall(r"{{NYPL-image-DigitalID|id=(.*?)}}",xml)
			r4 = re.findall(r"DigitalID\s?=\s?(.*?)",xml)

			ids = []

			
			if len(r1) > 0:
				# print(r1)
				ids = ids +  r1
				pass
			elif len(r2) > 0:
				ids = ids +  r2
				# print(r2)
				pass
			elif len(r3) > 0:
				ids = ids +  r3
				# print(r3)				
				pass
			elif len(r4) > 0:
				ids = ids +  r4
				# print(r3)				
				pass				
			else:
				pass
				# print(xml)

			clean_ids = []
			for x in ids:
				x = x.replace('id=','')
				x = x.strip()
				if len(x) > 0:
					clean_ids.append(x)

			# print(clean_ids)

			for i in clean_ids:
				if i in id_lookup:

					if 'cropped' not in xml and 'crop' not in xml:

						# print(id_lookup[i])
						wiki_id = re.findall(r"<id>(.*?)</id>\n",xml)[0]
						wiki_title = re.findall(r"<title>(.*?)</title>\n",xml)[0]
						print(wiki_id)
						print(wiki_title)
						# print(xml)

						imageinfourl = f'https://www.mediawiki.org/w/api.php?action=query&titles={wiki_title}&prop=imageinfo&iilimit=50&iiend=1900-12-31T23:59:59Z&iiprop=timestamp%7Cuser%7Curl&format=json'

						imageinfo = requests.get(url=imageinfourl)

						try:
							imageinfo = imageinfo.json()
							history = imageinfo['query']['pages']['-1']['imageinfo']
							history = sorted(history, key = lambda i: i['timestamp'])
							history = history[0]
							# print(imageinfo['query']['pages']['-1']['imageinfo'])
							# print() 

						except:
							print("JSON imageinfo Error with this file",wiki_title)
							continue



						all_data.append({'mapwarper':id_lookup[i], 'commons':{'orgImg': history['url'], 'id':wiki_id,'title':wiki_title,'xml':xml}})
						record_count+=1

			record = []
		else:
			record.append(line)


print(record_count)
json.dump(all_data,open('waper_on_commons.json','w'),indent=2)
