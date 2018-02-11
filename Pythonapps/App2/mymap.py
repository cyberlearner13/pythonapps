import folium
import pandas

volcanoes = pandas.read_csv("Volcanoes_USA.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
elev = list(volcanoes["ELEV"])

def colorProducer(elevation):
    if elevation <= 1000:
        return 'green'
    elif elevation > 1000 and elevation <= 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58,-99.09], zoom_start=6,tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=folium.Popup(str(el)+" m",parse_html=True), 
    radius= 6, fill_color=colorProducer(el), fill=True, color='grey', fill_opacity = 0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <=x['properties']['POP2005']  < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")

