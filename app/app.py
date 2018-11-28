from flask import Flask, jsonify, request
from flask_cors import CORS
from dbdb import *
import json


# D:\Anaconda3\Scripts\activate base
app = Flask(__name__)
CORS(app)
globalkeyword = []


# raspberry
# post /deliver_keyword data: {keyword :}
@app.route('/deliver_keyword', methods=['POST'])
def deliver_keyword():
    # print(request.headers)
    global globalkeyword
    globalkeyword = request.values['keyword']
    print('globalkeyword:', globalkeyword)
    return 'ok'
# raspberry


@app.route('/', methods=['GET'])
def index():
    return "Hello 20181118888"

# get /store/<name> data: {name :}


@app.route('/store/<string:cityName>')
def get_store(cityName):
    a = []
    for event in eventsTable.find({"city": cityName}, {"_id": 0}):
        a.append(event)
    return jsonify(a)


@app.route('/yeartoevent', methods=['POST'])
def yeartoevent():
    a = []
    city = request.values['city']
    yearFrom = int(request.values['yearFrom'])
    yearTo = int(request.values['yearTo'])
    print(yearFrom, yearTo)
    events = eventsTable.find({"yearFrom": {"$gte": yearFrom-1},
                               "yearTo": {"$lte": yearTo+1},
                               "city": city, }, {"_id": 0})
    for event in events:
        a.append(event)
    return jsonify(a)


@app.route('/allCityInThisYear', methods=['POST'])
def allCityInThisYear():
    a = []
    year = int(request.values['year'])
    cities = citiesTable.find({"yearFrom": {"$lte": year},
                               "yearTo": {"$gte": year}},
                              {"_id": 0})
    for city in cities:
        a.append(city)
    return jsonify(a)


@app.route('/routesInThisYear', methods=['POST'])
def routesInThisYear():
    a = []
    year = int(request.values['year'])
    routes = routesTable.find({"yearFrom": {"$lte": year},
                               "yearTo": {"$gte": year}},
                              {"_id": 0})
    for route in routes:
        a.append(route)
    returndata = jsonify(a)
    return returndata


# @app.route('/searchKeyword', methods=['POST'])
# def searchKeyword():
#     a = []
#     Keyword = request.values['Keyword']
#     cities = eventsTable.find({}, {"_id": 0})

#     for city in cities:
#         a.append(city)
#     return jsonify(a)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
