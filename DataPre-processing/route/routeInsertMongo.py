from bs4 import BeautifulSoup as Soup
import numpy as np
from os import listdir
from dbdb import *


def routeObject(filename):
    with open(f'kmlfile/{filename}', encoding='utf8') as data:
        kml_soup = Soup(data, 'lxml-xml')  # Parse as XML+

    routeName = kml_soup.find('name').get_text()
    yearFrom = int(kml_soup.find('yearFrom').get_text())
    yearTo = int(kml_soup.find('yearTo').get_text())
    detail = kml_soup.find('detail').get_text()
    lines = []
    points = []

    Placemarks = kml_soup.find_all('Placemark')

    for Placemark in Placemarks:
        name = Placemark.find('name').get_text()
        try:  # 線
            coordinates = []
            coordinatess = Placemark.select(
                'LineString > coordinates')[0].get_text().split(',')
            coordinatess = coordinatess[0:-1]
            coordinatess = [float(coordinate.replace('0\n', '').replace(
                '\n', '').strip()) for coordinate in coordinatess]
            for i in range(0, len(coordinatess), 2):
                coordinates.append([coordinatess[i], coordinatess[i+1]])
            color = Placemark.find('styleUrl').get_text().split('-')[1]
            line = {
                "name": name,
                "color": color,
                "coordinates": coordinates
            }
            lines.append(line)
        except:  # 點
            coordinates = Placemark.select('Point > coordinates')[
                0].get_text().split(',')[0:-1]
            coordinates = [float(coordinate.replace('0\n', '').replace(
                '\n', '').strip()) for coordinate in coordinates]
            point = {
                "name": name,
                "coordinates": coordinates
            }
            points.append(point)

        routes = {}
        routes['routeName'] = routeName
        routes['yearFrom'] = yearFrom
        routes['yearTo'] = yearTo
        routes['detail'] = detail
        routes['lines'] = lines
        routes['points'] = points
    return routes


if __name__ == '__main__':
    files = [routeObject(f) for f in listdir('kmlfile') if f.endswith('.kml')]
    print(files[0].keys())
    print(len(files))
    routesTable.insert_many(files)
