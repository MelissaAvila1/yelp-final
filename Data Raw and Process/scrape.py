import requests
import csv
import time

from BeautifulSoup import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException


list_of_rows = []
toprint = False


with open('sites.csv', 'rU') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		url = row[0]
		print url
		response = requests.get(url)
		html = response.content
		soup = BeautifulSoup(html)
		priceCont = soup.find("div", attrs={'class': 'island summary'})
		price = priceCont.find("dd", attrs={'class': 'nowrap price-description'}).text
		list_of_cells = []
		list_of_cells.append(price)
		holder = soup.find("div", attrs={'class': 'short-def-list'})

		for item in holder.findAll("dl"):
			descriptor = item.find("dt", attrs={'class': 'attribute-key'}).text
			response = item.find("dd").text
			line = descriptor + ": " + response
			list_of_cells.append(line)
		list_of_rows.append(list_of_cells)

outfile = open("./additional.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Price", "Take Reservations", "Delivery", "Takeout", "Accepts Credit Cards", "Bike Parking", "Good for Kids", "Good for Groups", "Attire", "Ambience", "Noise Level", "Alcohol", "Outdoor Seating", "Wifi", "Has TV", "Caters"])
writer.writerows(list_of_rows)