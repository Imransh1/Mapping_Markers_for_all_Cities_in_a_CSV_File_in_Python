import pandas as pd
import folium as fol
import numpy as np
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

# Convert to / create dataframe as per your choice  
# Here I have converted a .csv file using pandas module.

df = pd.read_csv('PY_Users.csv')
   
# declare an empty list to store
# latitude and longitude of values 
# of city column

longitude = []
latitude = []
   
# function to find the coordinate
# of a given city 

def findGeocode(city):
       
    # try and catch is used to overcome
    # the exception thrown by geolocator
    # using geocodertimedout  

    try:
          
        # Specify the user_agent as your
        # app name it should not be none

        geolocator = Nominatim(user_agent="your_app_name")
          
        return geolocator.geocode(city)
      
    except GeocoderTimedOut:
          
        return findGeocode(city)    

# each value from city column
# will be fetched and sent to
# function find_geocode  
 
for i in (df["City"]):
      
    if findGeocode(i) != None:
           
        loc = findGeocode(i)
          
        # coordinates returned from 
        # function is stored into
        # two separate list

        latitude.append(loc.latitude)
        longitude.append(loc.longitude)
       
    # if coordinate for a city not
    # found, insert "NaN" indicating 
    # missing value 
    else:
        latitude.append(np.nan)
        longitude.append(np.nan)

df["latitude"] = latitude
df["longitude"] = longitude

# Add latitude and longitude to dataframe 'df'

stationArr = df[['City','Users','latitude','longitude']].values

map_ = fol.Map(location=(20.5937,78.9629), zoom_start = 12)

# Adding Map Figure

for cities in range(len(stationArr)):
    m = fol.Marker(location=[stationArr[cities][2],stationArr[cities][3]], popup=stationArr[cities][0] , ).add_to(map_)
    m.save('users.html')
    # For each city in our csv file marker will be added
    # Markers will change as soon as the city names changes or more cities are added in the .csv file
    # Just need to run this file once in order to implement changes 
    # You can do many more things try to explore it more.

# Peace Out :-) 
# Developed By @ImranSh1 Github