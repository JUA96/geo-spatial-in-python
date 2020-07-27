#The aim of this project is to run through how you would go about creating geospatial visualisation from the ground up.
#The emphasis is on gradually increasing the complexity of the plotting using different python libraries.

#Stage 1: Understanding the importance of Geo Visualization in Data Science with an overview of the whole project (This first recorded non-technical task isn't included in the Jupyter notebook).

#Stage 2: Generating basic maps with Folium.

#Stage 3: Generating Stamen Toner Maps and Stamen Terrain Maps.

#Stage 4: Plotting and Visualizing your own City on the World Map.

#Stage 5: Solving a short project using Geographical Maps.

#Package dependencies
import numpy as np #scientific computing
import pandas as pd #data structure

import folium

#Define the world map
world_map = folium.Map()

#Display world map
world_map

#Define the world map in Africa
world_map = folium.Map(location=[20.2, -1.4],zoom_start=5)

#Display world map
world_map

#Generating Stamen Toner Maps and Stamen Terrain Maps - High Contrast Maps
#Create a Stamen Toner Map of Africa
world_map = folium.Map(location=[20.2, -1.4], zoom_start=4, tiles='Stamen Toner')

#Display Map
world_map

world_map = folium.Map(location=[20.2, -1.4], zoom_start=4, tiles='Stamen Terrain')

#Display Map 
world_map

#Visualising a City on the Map
latitude = 28.644800
longitude = 77.216721
#Create map and display it 
delhi_map = folium.Map(location=[latitude, longitude],)

delhi_map
