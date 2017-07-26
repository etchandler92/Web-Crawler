import requests
import csv
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError
from requests.exceptions import Timeout

result = {}

with open('sites_to_crawl.csv', 'r') as csvfile:
	content = csv.reader(csvfile, delimiter = ',')
	writer = csv.writer(open('result.csv', 'w'), delimiter=',')
	for row in content:

		url = row[0]
		r = requests.get(url, timeout=1.0)

		try:
			if r.history == [] and r.raise_for_status() == None:
				result[url] = r.text

			else: 
				result[url] = r.status_code

		except ConnectionError as e:
			result[url] = e

		except HTTPError as e:
			result[url] = e

		except Timeout as e:
			result[url] = e

	writer.writerow(result.keys())
	writer.writerow(result.values())