from selenium import webdriver

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--proxy-server=%s' % '202.74.243.38:32449')
browser = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe", options=chrome_option)
browser.get("https://youtube.com")
