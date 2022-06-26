import S_1.models 
import basic_app.models
import S_2.models 
import S_5P.models 
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
import json


class APIfunc():

    api = SentinelAPI('franciscopg98', 'Sporting37', 'https://apihub.copernicus.eu/apihub')

    queries = basic_app.models.Query.objects.get(platform= "Sentinel - 5P")
    print('x')
    print(queries)
    print('y')
    print(type(queries.area))
    print(queries.area)
   #area_json = json.dumps(queries.area)
    print('k')
    #print(type(area_json))
    #print(area_json)
    footprint = geojson_to_wkt(queries.area)
    print(type(footprint))
    print('z')
    start = queries.startdate 
    end = queries.enddate 
    platform = queries.platform 
    products = api.query(footprint,
                     date=(start, end),
                     platformname= platform)

  
