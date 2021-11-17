#Name: Namira Zaman
#Email: namira.zaman01@myhunter.cuny.edu
#Date: 9 November 2021

import folium
import pandas as pd

restaurants = pd.read_csv("open_restaurant_applications.csv")
belmont = restaurants.groupby("NTA").get_group("Belmont")
print(belmont)
mymap = folium.Map(location=[40.855357,-73.887198], zoom_start=15)
for index,row in belmont.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Street"]
    newMarker = folium.Marker([lat,lon], popup=name)
    newMarker.add_to(mymap)
mymap.save(outfile="belmont.html")
