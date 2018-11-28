# -*- coding: utf-8 -*-
"""
Created on Tue May  1 17:48:31 2018

@author: yiching
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib
from urllib.parse import quote
import os

thisDir = 'jade'
letter = 'A'
if not os.path.exists(thisDir):
    os.makedirs(thisDir)
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://theme.npm.edu.tw/selection/Category.aspx?sNo=03000131')
time.sleep(5)
#


def execute_times(times):
    for i in range(times + 1):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)


execute_times(10)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
#all_image = soup.find_all('img')
grid = soup.find('div', {'id', 'grid'})
infos = grid.find_all('div')
all_address = ""
count = 0
for info in infos:
    count += 1
    urllib.request.urlretrieve(quote(info.find(
        'img')['src'], safe='/:?='), thisDir + '/' + letter + "%s.jpg" % str(count))
    all_address += 'https://theme.npm.edu.tw/selection/' + \
        info.find('a')['href'] + ','

# 開啟檔案
fp = open(thisDir + "/address.txt", "a")
# 寫入 This is a testing! 到檔案
fp.write(all_address)
# 關閉檔案
fp.close()
