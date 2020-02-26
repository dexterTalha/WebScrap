import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")

browser.get("https://www.cashify.in/sell-old-laptop/sell-hcl")
time.sleep(1)
elem = browser.find_element_by_tag_name("body")

file = open("hcl_models.csv", "w")
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
    imageAlt = imageAlt.replace(",", "|")
    print(imageAlt+", "+imageSrc)
    file.write(imageAlt+", "+imageSrc+"\n")
file.close()