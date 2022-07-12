import pandas
import folium
from folium import plugins

# Convert to / create dataframe as per your choice  
# Here I have converted a .csv file using pandas module.

df = pandas.read_csv('PY_Users.csv')

map_ = folium.Map(location=[19.0760, 72.8777 ], zoom_start=10)

# we can also adjust height and width of map on our html page for e.g width="%80", height="%80
# there are different types of maps tiles = 'stamen toner' gives b&w map tiles="Stamen Watercolor" gives watercoloured_map and more

m = folium.Marker(location=[19.2183, 72.9781 ], popup='Thane').add_to(map_)
# Adds Normal marker on map
m = folium.CircleMarker(location=[19.2183, 72.9781 ], radius =40 , popup='Thane', color='#00FF00' ,fill_color='orange').add_to(map_)
# Adds CircleMarkers with given specifications 
m = folium.CircleMarker(location=[19.0760, 72.8777 ], radius = 40 , popup='Mumbai', color='#00FF00' ,fill_color='red').add_to(map_)
m.save('abc.html')

map2 = folium.Map(location=(19.0760, 72.8777), zoom_start=12)
minimap = plugins.MiniMap()
map2.add_child(minimap)
map2.save('xyz.html')

# Creates a minimap view of a given map location

map_.add_child()