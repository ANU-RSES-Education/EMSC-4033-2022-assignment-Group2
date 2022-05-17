"""
This is to define test functions to each of my functions

"""

import pytest
from src.my_functions import *

def documentation_test(my_doc_type = str):
    # test with type

    document_type = type(my_documentation())
    document_length = len(my_document())
    
    
    assert document_type == my_doc_type, " *** Fail test, no documentation to return*** "

    
    
    
def coastline_test(my_cl_type = cartopy.feature.NaturalEarthFeature, my_cl_name = 'coastline'):
    # Test with type and feature name
    cl = my_coastlines('50m')
    type_cl = type(cl)
    name_cl = cl.name             
                   
    assert type_cl == my_cl_type and name_cl == my_cl_name, " ***Fail test, no cartopy features for coastlines*** "
                   
                   
def water_features_test(my_wf_type = list, my_wf_name = ['rivers', 'lakes']):
    # Test with type and feature names

    wf = my_water_features('50m')

    type_wf = type(wf)

    name_wf = []
    name_wf.append(wf[0].name)
    name_wf.append(wf[1].name)

    assert type_wf == my_wf_type and name_wf == my_wf_name, " *** Fail test, no [list] of water cartopy features to return "


def test_my_basemaps(type_of_my_mapper = dict, type_of_my_od = cartopy.io.img_tiles.MapboxTiles):
    # Test with the types of returned dict and  outdoor map

    mapper = my_basemaps()

    mapper_type = type(mapper)

    od_type = type(mapper["mapbox_outdoors"])

    assert mapper_type == type_of_my_mapper and od_type == type_of_my_od, " *** Fail test, no basemap from 'mapbox_outdoors' to return "
                   
                   

                   
def test_download_point_data(my_eq_type = np.ndarray, my_eq_size = 4):
    # Test with type and test if the array do has correct shape/features

    lat0 =  -20  ; lat1 = 55
    lon0 =  -90; lon1 = -160
    map_extent = [lon0, lon1, lat0, lat1]

    eq = download_point_data(map_extent)

    type_eq = type(eq)

    size_eq = eq.shape[1]

    assert type_eq == my_eq_type and size_eq == my_eq_size, " *** Fail tes, no  np.array of earthquake information to download "


def test_my_point_data(type_my_element = np.bool_):
    # Test with the type of each element in the array

    lat0 =  -20  ; lat1 = 55
    lon0 =  -90; lon1 = -160
    map_extent = [lon0, lon1, lat0, lat1]

    point_data = my_point_data(map_extent)

    type_element = type(point_data.all())

    assert  type_element == type_my_element, " *** Fail to return the requested point data "


def test_download_raster_data(my_raster_data_shape = (1801, 3601, 3)):
    # Test with the shape of the global grid coordinate array

    raster_data = download_raster_data()

    shape_raster_data = raster_data.shape

    assert shape_raster_data == my_raster_data_shape, " *** Fail test to download correct raster data of seafloor age "


def test_my_global_raster_data():
    # Test if the retuned age data are not empty

    data_2 = my_global_raster_data()

    data_age = data_2[:,:,2]

    shape_age = data_age.shape
    print(shape_age)
    empty_array = np.empty(shape_age)

    assert (data_age != empty_array).any(), " *** Fail to return the raster data "
                   

    
    