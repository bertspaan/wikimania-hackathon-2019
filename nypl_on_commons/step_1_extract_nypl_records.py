

nyplxmp = open('nypl_images.xml','w')
nyplxmp.write('<pages>')
record_count = 0
nypl_count = 0
with open('/Volumes/Lately/commonswiki-20190720-pages-meta-current.xml') as input:

	record = []


	for line in input:

		if '</page>' in line:
			record_count+=1
			if record_count % 100000 == 0:
				print(record_count, nypl_count)
			record.append(line)
			xml = "".join(record)
			if 'NYPL-image' in xml or 'nypl-image' in xml:
				nypl_count+=1
				nyplxmp.write(xml +'\n')

			record = []
		else:
			record.append(line)


nyplxmp.write('</pages>')


