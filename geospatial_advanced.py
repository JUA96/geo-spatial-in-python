#Chloropeth Maps
import geopandas as gpd
from pyproj import CRS

#Load in the Nashville Building Permits dataset:
permits = pd.read_csv('https://assets.datacamp.com/production/repositories/2409/datasets/b8781d54c145e27ce43442bc6b327ac64158ebd6/building_permits_2017.csv')
permits.head()

import geojson
#with open('data/council_districts.geojson') as f:
 #   gj = geojson.load(f)
#council_districts = gj['features'][0]

#features = gj


fname = "./data/council_districts.geojson"

council_districts = gpd.read_file(fname)
print(type(df))
council_districts


from shapely.geometry import Point

# Create a shapely Point from lat and lng
permits['geometry'] = permits.apply(lambda x: Point((x.lng , x.lat)), axis = 1)

# Build a GeoDataFrame: permits_geo
permits_geo = gpd.GeoDataFrame(permits, crs = council_districts.crs, geometry = permits.geometry)

# Spatial join of permits_geo and council_districts
permits_by_district = gpd.sjoin(permits_geo, council_districts, op = 'within')
print(permits_by_district.head(2))

# Create permit_counts
permit_counts = permits_by_district.groupby(['district']).size()
print(permit_counts)
