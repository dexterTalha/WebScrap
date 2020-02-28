import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


url = "https://www.cashify.in/sell-old-mobile-phone/sell-xiaomi"

browser = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
browser.get(url)
city_container = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@class='MuiGrid-root MuiGrid-container MuiGrid-justify-xs-center']")))
city = city_container.find_elements_by_xpath("//*[@class='MuiGrid-root jss278 cursor MuiGrid-container MuiGrid-item MuiGrid-zeroMinWidth MuiGrid-direction-xs-column MuiGrid-wrap-xs-nowrap MuiGrid-align-items-xs-center MuiGrid-justify-xs-center']")
city[2].click()
series_container = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@class='mar-t20 layout horizontal wrap pad-lr-16-mob']")))
elem = browser.find_element_by_tag_name("body")
for series in series_container:
    s = series.find_elements_by_xpath("//*[@class='pad10']")
    for li in range(len(s)):
        span1 = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='layout horizontal center-center radius-6 shadow cursor pad10']")))
        span = span1[li].find_element_by_tag_name("span")
        print(span.text)
        span1[li].click()
        main_container = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='jsx-1143766650 product-discovery min-height70']")))
        mobile_containers = main_container.find_elements_by_xpath("//*[@class='jsx-1143766650 layout horizontal center-center card-margin ']")

        no_of_pagedowns = 10
        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            no_of_pagedowns -= 1
        # print(len(mobile_containers))
        for mobile_container in range(len(mobile_containers)):
            print(mobile_containers[mobile_container].text)
        no_of_pagedowns = 10
        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_UP)
            time.sleep(0.2)
            no_of_pagedowns -= 1

        close = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@class='jss357']")))
        close.click()
