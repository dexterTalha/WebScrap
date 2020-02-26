import time
from selenium import webdriver
from urllib import request
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import os

browser = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")

browser.get("https://www.cashify.in/sell-old-mobile-phone/sell-ivoomi")
time.sleep(1)
elem = browser.find_element_by_tag_name("body")
if not os.path.exists("ivoomi_phone"):
    Path("ivoomi_phone").mkdir(parents=True, exist_ok=True)
    Path("ivoomi_phone/images").mkdir(parents=True, exist_ok=True)
file = open("ivoomi_phone/ivoomi_phone_models.csv", "w")

headers = "models,images\n"
file.write(headers)
no_of_pagedowns = 20
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -= 1
post_elems = browser.find_elements_by_xpath("//*[@class='jsx-1143766650 layout horizontal center-center card-margin ']")
for p in post_elems:
    imageAlt = p.find_element_by_class_name("img-resp").get_attribute("alt")
    imageSrc = p.find_element_by_class_name("img-resp").get_attribute("src")
    request.urlretrieve(imageSrc, "ivoomi_phone/images/"+imageAlt+".jpg")
    imageAlt = imageAlt.replace(",", "|")
    print(imageAlt + ", " + imageSrc)
    file.write(imageAlt + "," + imageSrc + "\n")
file.close()
