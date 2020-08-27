import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E1018&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&sortByPriceDescending=&_includeLetAgreed=on&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&letType=&letFurnishType=&houseFlatShare=", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

content = request.content

soup = BeautifulSoup(content, "html.parser")

# print(soup.prettify)

# Address, Bedroom number, Property info and Price

all_properties = soup.find_all("div", { "class": "propertyCard" })

for property in all_properties:

    property_bedrooms = property.find("h2", { "class": "propertyCard-title" }).text.replace(" ", "", 12)
    property_address = property.find("address", { "class": "propertyCard-address" }).text.replace("\n", "")
    property_price = property.find("span", { "class": "propertyCard-priceValue" }).text.replace("\n", "").replace(" ", "")
    property_listed_by = property.find("div", { "class": "propertyCard-branchSummary" }).text.replace("\n", "")
    property_contact = property.find("a", { "class": "propertyCard-contactsPhoneNumber" }).text

    print("---")
    print(property_bedrooms)
    print(property_address)
    print(property_price)
    print(property_listed_by)
    print(property_contact)
