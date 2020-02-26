import requests
from bs4 import BeautifulSoup as soup

my_url = "https://www.flipkart.com/mobile-phones-store?otracker=nmenu_sub_Electronics_0_Mobiles"
res = requests.get(my_url)
containers = soup(res.text, "html.parser")
file = open("flipkartBrand.csv", "w")
headers = "brands\n"
file.write(headers)
for ptag in containers.findAll("p", {"class": "yHn1qE"}):
    print(ptag.text)
    file.write(ptag.text+"\n")

file.close()