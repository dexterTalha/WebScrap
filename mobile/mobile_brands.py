import requests
from bs4 import BeautifulSoup as soup

my_url = "https://www.cashify.in/sell-old-mobile-phone"
res = requests.get(my_url)
html_text = soup(res.text, "html.parser")
item_holder = html_text.findAll("ul", {"class": "jsx-1363013921 jsx-2802770802 layout horizontal center-justified"})[0]
file = open("mobile_brands.csv", "w")
headers = "brand,title"
file.write(headers+"\n")
for item in item_holder:
    brand = item.a.div.span.img['alt']
    title = item.a['title']
    print(title)
    file.write(brand+","+title+"\n")
file.close()