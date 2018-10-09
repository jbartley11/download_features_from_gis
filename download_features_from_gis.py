# Download features from ArcGIS Online or Portal for ArcGIS
# Jason Bartley
# Written for use in Python 3.x
# Requires ArcGIS API for Python
# Instructions to install:
# https://developers.arcgis.com/python/guide/install-and-set-up/

from arcgis.gis import GIS
from arcgis.gis import Item
from arcgis.features.manage_data import extract_data
import arcpy
import getpass

try:

    # set these variables
    username = "jason_pug"
    password = getpass.getpass()

    # get item id of layer
    itemid = "90c142b286144f918c53e005c8bf056c"
    directory = r'C:\Users\jaso9356\Desktop\dev'

    # url will be https://www.arcgis.com for ArcGIS Online
    # for portal use http://machinename.domain.com/webadapter
    url = "https://www.arcgis.com"


    # create gis object
    gis = GIS(url=url, username=username, password=password)

    # get item of layer
    data = gis.content.get(itemid)
    feature_layer = arcgis.features.FeatureLayer(data.url, gis)

except Exception as e:
    print(e)
    
# assignment_fl = arcgis.features.FeatureLayer(wf_project["assignments"]["url"], gis)
# print("Getting assignments...")
# assignments = assignment_fl.query("1=1")

# gis = GIS("http://yourROOT.maps.arcgis.com/","User","Pw")
# layer = FeatureLayer("https://services1.arcgis.com/oz19jk1209j09j39j/ArcGIS/rest/services/ServiceName/FeatureServer/0",gis)
# featureSet = layer.query(where='1=1', out_fields='*')

# rawJSON = featureSet.to_json

# jsonFile = 'c:\\somelocalpath\example.json'
# localFC = 'c:\\somelocalpath\\Example.gdb\\data'
# with open(jsonFile, "w") as file:
#     file.write(rawJSON)
# arcpy.JSONToFeatures_conversion(jsonFile,localFc)

# data = gis.content.get(itemid)
# outputgdb = extract_data([data])
# outputgdb.download(directory)

# data_item = gis.content.get(itemid)
# data_item
# # data_item.download(save_path = directory)
# outputgdb = extract_data([data_item])
# print(outputgdb)
# outputgdb.download(directory)

# item = Item(gis, itemid)
# item.download(save_path = directory)
# outputgdb = extract_data([csv_lyr])
# outputgdb.download('C:\\xc')

# from arcgis.features.manage_data import extract_data
# csv_lyr = gis.content.get('c8bc7d3c3b60415e9845bc00dcd777ed')
# outputgdb = extract_data([csv_lyr])
# outputgdb.download('C:\\xc')