"""
Define test functions for each of my_fucntions 
"""

import pytest
from src.my_functions import *

def test_my_documentation(type_my_doc = str): 
    # Test with type
    
    type_docu = type(my_documentation())
    len_docu = len(my_documentation())
    
    
    assert type_docu == type_my_doc, " *** Fail to return a documentation "
    

def test_my_coastlines(type_my_cl = cartopy.feature.NaturalEarthFeature, name_my_cl = 'coastline'): 
    # Test with type and feature name
    
    cl = my_coastlines('50m')
    
    type_cl = type(cl)
    
    name_cl = cl.name
    
    assert type_cl == type_my_cl and name_cl == name_my_cl, " *** Fail to return the cartopy features of coastlines "
    
    
def test_my_water_features(type_my_wf = list, name_my_wf = ['rivers_lake_centerlines', 'lakes']):
    # Test with type and feature names
    
    wf = my_water_features('50m')
    
    type_wf = type(wf)
    
    name_wf = []
    name_wf.append(wf[0].name)
    name_wf.append(wf[1].name)
    
    assert type_wf == type_my_wf and name_wf == name_my_wf, " *** Fail to return a [list] of water cartopy features "

    
def test_my_basemaps(type_my_mapper = dict, type_my_od = cartopy.io.img_tiles.MapboxTiles):
    # Test with the types of returned dict and  outdoor map
    
    mapper = my_basemaps()
    
    type_mapper = type(mapper)
    
    type_od = type(mapper["mapbox_outdoors"])
    
    assert type_mapper == type_my_mapper and type_od == type_my_od, " *** Fail to return the basemap from 'mapbox_outdoors' "

    
def test_download_point_data(type_my_eq = np.ndarray, size_my_eq = 4):
    # Test with type and test if the array do has correct shape/features
    
    lat0 =  30  ; lat1 = 40
    lon0 =  -123; lon1 = -113
    map_extent = [lon0, lon1, lat0, lat1]
    
    eq = download_point_data(map_extent)
    
    type_eq = type(eq)
    
    size_eq = eq.shape[1]
    
    assert type_eq == type_my_eq and size_eq == size_my_eq, " *** Fail to download a np.array of earthquake information "
    
    
def test_my_point_data(type_my_element = np.bool_):
    # Test with the type of each element in the array
    
    lat0 =  30  ; lat1 = 40
    lon0 =  -123; lon1 = -113
    map_extent = [lon0, lon1, lat0, lat1]
    
    point_data = my_point_data(map_extent)
    
    type_element = type(point_data.all())
    
    assert  type_element == type_my_element, " *** Fail to return the requested point data "
    
    
def test_download_raster_data(shape_my_raster_data = (1801, 3601, 3)):
    # Test with the shape of the global grid coordinate array
    
    raster_data = download_raster_data()
    
    shape_raster_data = raster_data.shape
    
    assert shape_raster_data == shape_my_raster_data, " *** Fail to download correct raster data of seafloor age "
    
    
def test_my_global_raster_data():
    # Test if the retuned age data are not empty
    
    data_2 = my_global_raster_data()
    
    data_age = data_2[:,:,2]
    
    shape_age = data_age.shape
    print(shape_age)
    empty_array = np.empty(shape_age)
    
    assert (data_age != empty_array).any(), " *** Fail to return the raster data "
    