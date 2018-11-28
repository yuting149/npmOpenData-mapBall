import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyC4vLCktJ4cYux419dPHAn5j__QhIdnKKA')

# Geocoding an address
geocode_result = gmaps.geocode('W.Germany')

print('====')
print(geocode_result[0]['geometry']['location'])  # 'lat': 緯度, 'lng': 經度
print('====')

# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((23.9, 120.9))

# print('====')
# print(reverse_geocode_result)
# print('====')

# {'address_components': [{'long_name': 'Taiwan', 'short_name': 'Taiwan', 'types': ['establishment', 'natural_feature']}, {'long_name': 'Taiwan', 'short_name': 'TW', 'types': ['country', 'political']}],
#  'formatted_address': 'Taiwan',
#  'geometry': {'bounds': {'northeast': {'lat': 25.3011502, 'lng': 122.0069052}, 'southwest': {
#      'lat': 21.8966958, 'lng': 120.0277765}}, 'location': {'lat': 23.9036873, 'lng': 121.0793705}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 25.3011502, 'lng': 122.0069052}, 'southwest': {'lat': 21.8966958, 'lng': 120.0277765}}}, 'place_id': 'ChIJpcNhK8vVbjQRoH--QrDdIM8', 'types': ['establishment', 'natural_feature']}
