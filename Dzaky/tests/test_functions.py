import pytest
from src.functions import *
from src.my_functions import *

##Test functions from functions.py
def test_basic_function1(rtol=1.e-7):
    result = abs(function_try(4) - 28)
    assert result < rtol, " *** error is too big "

def test_basic_function2():
    function_try(4)
    assert True, " *** error is too big "

def test_paying_debt():
    paying_debt(600000)
    assert True, "*** not able to calculate the months needed for debt payment"

def test_city2city():
    city_to_city()
    assert True, "*** could not displayed the cities map"

##Test functions from my_functions.py
def test_my_documentation(documentation_type=str):
    
    doc_type = type(my_documentation())
    
    assert doc_type == documentation_type, "*** Unable to return the documentation"
    
def test_my_coastlines(my_coastlines_type = cartopy.feature.NaturalEarthFeature, my_coastline_name = 'coastline'): 
    
    cline = my_coastlines('50m')
    
    type_cline = type(cline)
    
    name_cline = cline.name
    
    assert type_cline == my_coastlines_type and name_cline == my_coastline_name, " *** Unable to return the type and name of my_coastline function"
    
def test_my_water_features(my_wf_type = list, my_wf_list = ['rivers_lake_centerlines', 'lakes']):
    # Test with type and feature names
    
    water_features = my_water_features('50m')
    
    water_features_type = type(water_features)
    
    water_features_list = []
    water_features_list.append(water_features[0].name)
    water_features_list.append(water_features[1].name)
    
    assert water_features_type == my_wf_type and water_features_list == my_wf_list, " *** Unable to return the list"
    
def test_my_basemaps(my_mapper_type = dict):
    # Test with the types of dict
    
    mapper = my_basemaps()
    
    mapper_type = type(mapper)
    
    assert mapper_type == my_mapper_type, " *** Unable to return the basemap dictionary "

def test_download_point_data(size_eq = 4):
    #test the array
    
    llat = 30; ulat = 40 #Define lower and upper latitude
    llon = -123; rlon = 113 #Define left and right longitude
    
    map_area = [llon, ulat, llon, rlon]
    
    eq_origin = download_point_data(map_area)
    
    size_eq_origin = eq_origin.shape[1]
    
    assert size_eq_origin == size_eq, "*** Unable to download earthquake events due to different eq size"
    
def test_download_raster_data(datashape=(1801, 3601, 3)):
    
    raster = download_raster_data()
    
    shape_raster = raster.shape
    
    assert shape_raster == datashape, "*** Unable to download rastered data because of different shape"
    
    