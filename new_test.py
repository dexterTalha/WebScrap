import requests
from bs4 import BeautifulSoup as soup

file = open("cashify_brand.csv", "w")
header = "brand, product_name, product_link\n"
file.write(header)
url = "https://www.newegg.com/global/in-en/p/pl?N=101300354&name=Desktop%20Graphics%20Cards&isdeptsrh=1"
res = requests.get(url)
cssClass = "item-info"
brands = soup(res.text, 'html.parser')
containers = brands.findAll("div", {"class": cssClass})

for container in containers:
    brand = container.div.a.img['title']
    title_container = container.findAll("a", {"class": "item-title"})
    product_link = title_container[0]['href']
    product_name = title_container[0].text
    file.write(brand + "," + product_name.replace(",", "|") + ","+product_link+"\n")
file.close()
