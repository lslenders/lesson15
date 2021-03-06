# Write structure of file as comments before writing code
from input_output import read_txt
from input_output import write_shape
from shapely.geometry import mapping
from apis import get_latlon
from apis import get_height_ahn2
from geobuilder import point

# files
in_cities = 'cities.txt'
out_shapefile = '/home/jasondavis/Wageningen/geocities/city_info_result.shp'

# data will look like this
schema = {'geometry': 'Point','properties': {'city': 'str', 'height_ahn2': 'float'}} #point geometry and attribute table with city and string

# we want to store the results in a list
results = []

# read the text file with cities 
cities = read_txt(in_cities)

# main loop over cities
for city in cities:
	city = city.strip() #preventing whitespace
	print city
	location = get_latlon(city)
	print location
	geometry = point(location['lng'], location['lat'])
	geometry_wkt = geometry.wkt
	height_ahn2 = get_height_ahn2(geometry_wkt)
	results.append({'geometry': mapping(geometry), 'properties': {'city': city, "height_ahn2": height_ahn2}})
# save the results to a shapefile
write_shape(out_shapefile, schema, results)



