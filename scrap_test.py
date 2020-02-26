import requests
from bs4 import BeautifulSoup
import xlwt
import re
from pathlib import Path


regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
url = input('Enter the sraping url\n')

if re.match(regex, url):
    sheetName = "diksha"
    findElement = input('Enter element you want to scrap\n')
    res = requests.get(url)
    fileName = "aa"
    if Path("C:\\Users\\Anand\\Desktop\\"+fileName+".xls").is_file():
        workbook = xlwt.Workbook("C:\\Users\\Anand\\Desktop\\"+fileName+".xls")
    else:
        workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheetName)
    print(res.text)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        count = 0
        for srpt in soup.find_all(findElement):
            print(srpt['href'])
        # for srpt in soup.select(findElement):
        #     sheet.write(count, 0, srpt['href'])
        #     print(srpt)
        #     count = count + 1
        # workbook.save("C:\\Users\\Anand\\Desktop\\"+fileName+".xls")
        # print("Location of the excel file "+fileName+".xls is at Desktop")

    else:
        print("Connection error")
else:
    print("Not a valid url")
