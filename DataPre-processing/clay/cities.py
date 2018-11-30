# -*- coding: utf-8 -*-
from dbdb import *


# coordinates(緯度, 經度)


if __name__ == '__main__':
    cities = [
        {
            "name": "新石器時代 大汶口文化",
            "coordinates": [36.13368, 115.65028],
            "yearFrom": -4300,
            "yearTo": -2500
        },
        {
            "name": "紅山文化晚期",
            "coordinates": [39.87204, 106.77333],
            "yearFrom":-3500,
            "yearTo":-3000
        },
        {
            "name": "良渚文化",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":-3200,
            "yearTo":-2000
        },
        {
            "name": "龍山文化",
            "coordinates": [36.13368, 115.65028],
            "yearFrom":-2500,
            "yearTo":-2000
        },
        {
            "name": "商",
            "coordinates": [33.6103, 112.04677],
            "yearFrom":-1600,
            "yearTo":-1046
        },
        {
            "name": "西周",
            "coordinates": [35.13364, 114.77138],
            "yearFrom":-1046,
            "yearTo":-771
        },
        {
            "name": "春秋",
            "coordinates": [33.6103, 112.04677],
            "yearFrom":-770,
            "yearTo":-476
        },
        {
            "name": "戰國",
            "coordinates": [33.6103, 112.04677],
            "yearFrom":-475,
            "yearTo":-276
        },
        {
            "name": "秦",
            "coordinates": [31.23655, 104.66396],
            "yearFrom":-221,
            "yearTo":-207
        },
        {
            "name": "漢",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":-206,
            "yearTo":-220
        },
        {
            "name": "西漢",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":-206,
            "yearTo":8
        },
        {
            "name": "新莽",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":9,
            "yearTo":23
        },
        {
            "name": "東漢",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":25,
            "yearTo":220
        },
        {
            "name": "晉",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":265,
            "yearTo":420
        },
        {
            "name": "唐",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":618,
            "yearTo":907
        },
        {
            "name": "五代",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":907,
            "yearTo":960
        },
        {
            "name": "宋",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":960,
            "yearTo":1279
        },
        {
            "name": "北宋",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":960,
            "yearTo":1127
        },
        {
            "name": "南宋",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":1127,
            "yearTo":1279
        },
        {
            "name": "金",
            "coordinates": [35.13364, 114.77138],
            "yearFrom":1115,
            "yearTo":1234
        },
        {
            "name": "元",
            "coordinates": [35.13364, 114.77138],
            "yearFrom":1279,
            "yearTo":1368
        },
        {
            "name": "明",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":1368,
            "yearTo":1644
        },
        {
            "name": "清",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":1644,
            "yearTo":1911
        },
        {
            "name": "民國",
            "coordinates": [27.32813, 115.91396],
            "yearFrom":1911,
            "yearTo":9999
        },
        {
            "name": "台灣",
            "coordinates": [23.973875, 120.982025],
            "yearFrom":1911,
            "yearTo":9999
        }
    ]
    # save to dbdb
    citiesTable.insert_many(cities)
    # save to dbdb
#
# 頁面url
# year
# itemName
# 圖片url
