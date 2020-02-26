from bs4 import BeautifulSoup as soup

file = open("laptop_brand.html", "r")
csvFile = open("laptop_brands.csv", "w")
headers = "title,brand,image\n"
csvFile.write(headers)
html_text = soup(file.read(), "html.parser")

for liObject in html_text.find_all('li'):
    title = liObject.a['title']
    brand = liObject.div.img['alt']
    image = liObject.div.img['src']
    csvFile.write(title + "," + brand + "," + image + "\n")
    # print(image)
file.close()
