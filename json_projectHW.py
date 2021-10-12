from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('US_fires_9_1.json', 'r')

list_of_fires = json.load(infile)

print(len(list_of_fires))

print(type(list_of_fires))

lats, lons, brights = [],[],[]

for fire in list_of_fires:
    bright = fire['brightness']
    if bright > 450:
        lat = fire['latitude']
        lon = fire['longitude']
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

print(lats[:5])
print(lons[:5])
print(brights[:5])
print(len(brights))

data = [Scattergeo(lon=lons, lat=lats)]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*3.5 for b in brights],
        'color':brights,
        'colorscale': 'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Magnitude'}
    }
}]

my_layout = Layout(title="US Fires - 9/1/2020 through 9/13/2020")

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='US_fires_9_1.html')



