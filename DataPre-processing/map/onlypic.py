import os

allyears = os.listdir('mapballs')
i = 0

for folder in allyears:
    os.remove("mapballs/"+folder+'/googlemaps.html')
    os.remove("mapballs/"+folder+'/index.html')
    os.remove("mapballs/"+folder+'/leaflet.html')
    os.remove("mapballs/"+folder+'/metadata.json')
    os.remove("mapballs/"+folder+'/openlayers.html')
    print(i, folder)
    i += 1
