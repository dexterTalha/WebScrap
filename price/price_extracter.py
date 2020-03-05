import time
from bs4 import BeautifulSoup as soup
from selenium import webdriver as driver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

browser = driver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
browser.get("https://www.cashify.in/sell-old-mobile-phone/sell-xiaomi")

# city selection
city_container = WebDriverWait(browser, 20).until(EC.presence_of_element_located(
    (By.XPATH, "//*[@class='MuiGrid-root MuiGrid-container MuiGrid-justify-xs-center']")))
city = city_container.find_elements_by_xpath(
    "//*[@class='MuiGrid-root jss278 cursor MuiGrid-container MuiGrid-item MuiGrid-zeroMinWidth MuiGrid-direction-xs-column MuiGrid-wrap-xs-nowrap MuiGrid-align-items-xs-center MuiGrid-justify-xs-center']")
city[2].click()

# scroll load more
elem = browser.find_element_by_tag_name("body")
no_of_pagedowns = 10
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -= 1

no_of_pagedowns = 10
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_UP)
    time.sleep(0.2)
    no_of_pagedowns -= 1
# model selection
mobile_models = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(
    (By.XPATH, "//*[@class='jsx-1143766650 layout horizontal center-center card-margin ']")))

for mobile in range(len(mobile_models)):
    a = mobile_models[mobile].find_element_by_tag_name("a")
    print(a.text)
    url = a.get_attribute("href")
    browser.execute_script("window.open('')")
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    browser.get(url)
    # variant selection
    variant_container = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@class='jsx-391710674 jsx-3475687450 layout horizontal wrap']")))
    # print(variant_container.get_attribute('innerHTML'))
    try:
        variant = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(
            (By.XPATH, "//*[@class='jsx-391710674 jsx-3475687450 pad10']")))

        for varCount in range(len(variant)):
            print(variant[varCount].text)
            variant[varCount].click()

            variant_price = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@itemprop='offers']")))
            price_span = variant_price.find_element_by_xpath(
                "//*[@class='jsx-391710674 jsx-3475687450 font-medium font40-30 accent-text']")
            print(price_span.text.replace(",", "")[1: len(price_span.text) - 1])
            browser.back()
            variant = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@class='jsx-391710674 jsx-3475687450 pad10']")))
    except:
        variant_price = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@itemprop='offers']")))
        price_span = variant_price.find_element_by_xpath(
            "//*[@class='jsx-391710674 jsx-3475687450 font-medium font40-30 accent-text']")
        print(price_span.text.replace(",", "")[1: len(price_span.text) - 1])

    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    mobile_models = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located(
        (By.XPATH, "//*[@class='jsx-1143766650 layout horizontal center-center card-margin ']")))
