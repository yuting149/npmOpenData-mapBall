from dbdb import *
import json


# a = []
# result = eventsTable.find(
#     {"city": '中國'},
#     {"detail": 0}
# )

# a = []
# result = eventsTable.find(
#     {"yearFrom": {"$gt": 300},
#      "city": '中國', },
#     {"detail": 0}
# )
# for event in result:
#     if('清明' in event['title']):
#         a.append(event)
# print(a)

# a = []
# result = citiesTable.find({"yearFrom": {"$lt": 1700},
#                            "yearTo": {"$gt": 1700}},
#                           {"_id": 0})
# for city in result:
#     a.append(city)
# print(a)

# eventsTable.createIndex({"detail": "text"})

# for event in result:
#     if 'BC' in event["yearFrom"]:
#         newvalues = {"$set": {"yearFrom": "-" + event["yearFrom"][2:]}}
#         myquery = {"_id": event["_id"]}
#         eventsTable.update_one(myquery, newvalues)
#     print("-" + event["yearFrom"][2:])

# eventsTable.remove({"city": "中國"})
