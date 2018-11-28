import pymongo
from pymongo import MongoClient
from dbdb import *


# print(myCollection.find_one())

# event = {
#     "title": "巴拿馬成為西班牙殖民地。",
#     "category": "political",
#     "yearFrom": "1501",
#     "yearTo": "1501",
#     "city": "巴拿馬"
# }
# x = eventsTable.insert_one(event)

cities = [{
    "name": "中國",
    "coordinates": [
        35.86166,
        104.195397
    ],
    "yearFrom": -4000,
    "yearTo": 9999
}]

for city in cities:
    citiesTable.insert_one(city)
    print(city["name"])

# a = []
# for event in eventsTable.find({"city": "法國"}):
#     a.append(event)
# print(a)
