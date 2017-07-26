import csv
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

with open('Book1.csv', 'r') as csvfile:
	content = csv.reader(csvfile, delimiter = ',')
	for row in content:
		try:
			html = urlopen(row[0])
			read = BeautifulSoup(html.read(),"html.parser")
		except HTTPError as e:
			print(e)
		except URLError as e:
			print("No Server!")
		else:
			print(read)