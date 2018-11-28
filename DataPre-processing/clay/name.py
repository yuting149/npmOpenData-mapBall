# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import urllib
from urllib.parse import quote
from dbdb import *
import os
import requests


def execute_times(times):
    for i in range(times + 1):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)


def printAndSave(info):
    imgurl = quote(info.find('img')['src'], safe='/:?=')
    html = 'https://theme.npm.edu.tw/selection/' + info.find('a')['href']
    r = requests.get(html)
    itemsoup = BeautifulSoup(r.text, 'lxml')
    try:
        detail = ''
        detaillist = itemsoup.select('div.content_intro > div > div > div')
        detaillist[0]
        for det in detaillist:
            detail += det.get_text()
    except:
        detail = ''
        detaillist = itemsoup.select('div.content_intro > div > div > p')
        for det in detaillist:
            detail += det.get_text()
    itemName = itemsoup.select('div.hd > h1')[0].get_text()
    try:
        author = itemsoup.select('div.hd > h2')[0].get_text()
    except:
        author = ''

    countryYear = itemsoup.select('div.hd > h3')[0].get_text().split('　')
    country = countryYear[0]
    year = countryYear[-1].split('-')
    try:
        if '西元前' in year[0]:
            year[0] = '-'+year[0][3:]
            if '西元前' in year[1]:
                year[1] = '-'+year[1][3:]
            if '西元' in year[1]:
                year[1] = year[1][2:]
        if '西元' in year[0]:
            year[0] = year[0][2:]
            if '西元' in year[1]:
                year[1] = year[1][2:]
    except:
        print('st happ')
        print(itemName)
        print('st happ')

    details = [category, country, author, detail]
    try:
        year[1]
    except:
        year.append(year[0])
    if(year[0] == ''):
        year = ['0', '0']
    print(year[0], year[1])
    event = {
        "title": itemName,
        "category": "Art",
        "yearFrom": int(year[0]),
        "yearTo": int(year[1]),
        "city": "中國",
        "image": imgurl,
        "detail": details,
        "url": html
    }

    # print(year)
    # print(details)
    # print(itemName)
    print(itemName)
    print('===')
    return event

    # print(itemName)
    # print(country)
    # print(year)
    # print(imgurl)
    # print(html)
    # print('===')


if __name__ == '__main__':
    # 繪畫 "https://theme.npm.edu.tw/selection/Category.aspx?sNo=03000117"
    # 書法 "https://theme.npm.edu.tw/selection/Category.aspx?sNo=03000118"
    # 文獻 "https://theme.npm.edu.tw/selection/Category.aspx?sNo=03000120"
    # 陶瓷 "https://theme.npm.edu.tw/selection/Category.aspx?sNo=03000129"
    # 銅器 "https://theme.npm.edu.tw/selection/Category.aspx?sNo=03000130"
    # 珍玩 "https://theme.npm.edu.tw/selection/Category.aspx?sNo=03000132"
    # 玉器 "https://theme.npm.edu.tw/selection/Category.aspx?sNo=03000131"

    urls = [
        {"category": "painting", "url": "03000117"},
        {"category": "calligraphy", "url": "03000118"},
        {"category": "literature", "url": "03000120"},
        {"category": "ceramics", "url": "03000129"},
        {"category": "bronze", "url": "03000130"},
        {"category": "toy", "url": "03000132"},
        {"category": "Jade", "url": "03000131"},
    ]
    events = []
    for url in urls:
        driver = webdriver.Chrome('chromedriver.exe')
        category = url["category"]
        driver.get(
            "https://theme.npm.edu.tw/selection/Category.aspx?sNo="+url["url"])
        time.sleep(5)
        execute_times(10)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        # all_image = soup.find_all('img')
        grid = soup.find('div', {'id', 'grid'})
        infos = grid.find_all('div')
        all_address = ""
        count = 0
        print('imgere')

        for info in infos:
            events.append(printAndSave(info))

    # save to dbdb
    eventsTable.insert_many(events)
    # save to dbdb
#
# 頁面url
# year
# itemName
# 圖片url
