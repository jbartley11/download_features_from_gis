# Download features from ArcGIS Online or Portal for ArcGIS
# into a new feature class
# Written for use in Python 3.x
# Requires ArcGIS API for Python and Arcpy
# Instructions to install:
# https://developers.arcgis.com/python/guide/install-and-set-up/


from arcgis.gis import GIS
from arcgis.gis import Item
from arcgis.features import FeatureLayer
import getpass

try:

    # username and password
    username = "<username>"
    password = getpass.getpass()

    # get item id of layer
    item_id = "<itemid>"

    # output_location
    # can be gdb or folder if you want shp
    directory = r'<path>'

    # url will be https://www.arcgis.com for ArcGIS Online
    # for portal use http://machinename.domain.com/webadapter
    url = "https://www.arcgis.com"

    # no modifications below here -----------------------------------------
    # create gis object
    gis = GIS(url=url, username=username, password=password)

    # get item of layer
    data_item = gis.content.get(item_id)
    data_url = data_item.url

    # prompt user for which layer to export
    layers = data_item.layers
    layer_choice = 0
    if len(layers) > 1:

        # print out choices
        print("Choices for layers are:")
        for layer in layers:
            print("{}: {}".format(layer.properties.id,
                                  layer.properties.name))

        # prompt user for choice
        layer_choice = input("Index of layer: ")

    # construct layer url and get name
    layer_url = '/'.join([data_url, str(layer_choice)])

    # make feature layer, query, and then save
    feature_layer = FeatureLayer(layer_url, gis)
    layer_name = feature_layer.properties.name.replace(" ", "_")
    featureSet = feature_layer.query(where='1=1', out_fields='*')
    featureSet.save(directory, layer_name)

    print("completed export of {}".format(layer_name))

except Exception as e:
    print(e)
