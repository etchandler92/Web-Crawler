import requests
import csv

with open('test.csv', 'r') as csvfile:
	content = csv.reader(csvfile, delimiter = ',')
	for row in content:

		try:
			url = row[0]
			r = requests.get(url, timeout=1.0)

		except Exception:
			continue

		except r.history != []:
			print(url.encode('ascii', 'ignore'))
			print(r.status_code)

		except r.status_code() != 200:
			print(url.encode('ascii', 'ignore'))
			print(r.status_code)
		else:
			print(r.text.encode('ascii', 'ignore'))