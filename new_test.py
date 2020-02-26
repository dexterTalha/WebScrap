import time

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.cashify.in/sell-old-mobile-phone/sell-xiaomi"

browser = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
browser.get(url)
series_container = browser.find_elements_by_xpath("//*[@class='mar-t20 layout horizontal wrap pad-lr-16-mob']")

for series in series_container:
    s = series.find_elements_by_xpath("//*[@class='pad10']")
    for li in s:
        span1 = li.find_element_by_tag_name("span")
        span = span1.find_element_by_tag_name("span")
        print(span.text)
        li.click()

        cl.click()
