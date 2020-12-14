import requests
import pandas
import pathlib

from bs4 import BeautifulSoup
from datetime import datetime

request = requests.get("https://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E1018&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&sortByPriceDescending=&_includeLetAgreed=on&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&letType=&letFurnishType=&houseFlatShare=", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

content = request.content

soup = BeautifulSoup(content, "html.parser")

all_properties = soup.find_all("div", { "class": "propertyCard" })

property_data = []

base_url = "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E1018&propertyTypes=&includeLetAgreed=false&mustHave=&dontShow=&furnishTypes=&keywords=&index="

page_number = soup.find("span", { "class": "searchHeader-resultCount" }).text

for page in range(0, int(page_number) - 25, 24):
    request = requests.get(base_url + str(page))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    all_properties = soup.find_all("div", { "class": "propertyCard" })

    for item in all_properties:

        data = {}

        try:
            data["Property Type"] = item.find("h2", { "class": "propertyCard-title" }).text.replace("\n", "").replace("            ", "")
            print('--------')
            print(item.find("h2", { "class": "propertyCard-title" }).text.replace("\n", "").replace("            ", ""))
        except:
            data["Property Type"] = None
            print(None)

        try:
            data["Property Address"] = item.find("address", { "class": "propertyCard-address" }).text.replace("\n", "")
            print(item.find("address", { "class": "propertyCard-address" }).text.replace("\n", ""))
        except:
            data["Property Address"] = None
            print(None)

        try:
            data["Rental Cost"] = item.find("span", { "class": "propertyCard-priceValue" }).text.replace("\n", "").replace(" ", "")
            print(item.find("span", { "class": "propertyCard-priceValue" }).text.replace("\n", "").replace(" ", ""))
        except:
            data["Rental Cost"] = None
            print(None)

        try:
            data["Listing Details"] = item.find("div", { "class": "propertyCard-branchSummary" }).text.replace("\n", "")
            print(item.find("div", { "class": "propertyCard-branchSummary" }).text.replace("\n", ""))
        except:
            data["Listing Details"] = None
            print(None)

        try:
            data["Contact Number"] = item.find("a", { "class": "propertyCard-contactsPhoneNumber" }).text
            print(item.find("a", { "class": "propertyCard-contactsPhoneNumber" }).text)
        except:
            data["Contact Number"] = None
            print(None)

        property_data.append(data)

data_frame = pandas.DataFrame(property_data)

scan_date = datetime.today().strftime('%Y-%m-%d')
scan_time = datetime.today().strftime('%H:%M:%S')

data_frame.to_csv(F'data/{scan_date}_{scan_time}.csv')