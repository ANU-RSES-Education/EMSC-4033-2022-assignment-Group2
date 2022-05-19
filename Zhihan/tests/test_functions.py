import pytest
import numpy
from src.my_functions import *

"""
Write some test functions to do test for each function.
"""
def test_my_documentation():
# test whether the output of the function is equal to that we expected
    
    result_docu = my_documentation()
    
    assert result_docu == """   
# What do we need to do

We need to complete the following functions to make notebook run to plot maps and do some test on these functions. The plots contain lots of information including a large area from 30-40°N and 113-123°W，features of rivers and oceans, topography of basemaps and data of thounds of earthquake events. We could get some these information easily from the final figure. 
    
## my_coastlines and my_water_features

We need to add coastlines and water features like rivers and oceans on map by these two functions. Import cartopy.feature and return cfeature.NaturalEarthFeature, which helps us to specify the types of parameters, resolution, color and other useful information. The resolution of coastlines are 10m and resolution of water features are 50m in this program.

## my_basemap

We could get the basemap from various sources from different website. We choose "Mapbox outdoors" as the source which could provide us with clear and beautiful image with topography, landscape and other basic ingredients.
The map_id and access token is available in notebook.

## download_point_data 

Then we could download the data of earthquake events we want by limiting the time span, latitude, longitude and magnitude from "IRIS" using 'obspy' package. Then unpack the obspy data into a plottable array.

## download_raster_data

Seafloor age data are stored in Cloudstor. We need to download seafloor ages from the cloudstor and assign them by latitude and longitude.
"""
" *** error is output is not equal to documentation "

def test_my_coastlines(resolution='10m'):
# test whether the type of output is equal to what we need     
    
    result_my_coastlines = my_coastlines(resolution)
    
    type_my_coastlines = type(result_my_coastlines)
    
    assert type_my_coastlines == cartopy.feature.NaturalEarthFeature 
    " *** error is type of output is not equal to cartopy.feature.NaturalEarthFeature "
    
def test_my_water_features(resolution ='10m'):
 # test whether the type of output is equal to what we need    
    
    result_my_water_features = my_water_features(resolution)
   
    type_my_water_features = type(result_my_water_features) 
    
    assert type_my_water_features == list
    " *** error is type of output is not list "
    
def test_my_basemaps():
# test whether the type of output is equal to what we need     
    
    result_my_basemaps = my_basemaps()
    
    type_my_basemaps = type(result_my_basemaps)
    
    assert type_my_basemaps == dict
    " *** error is type of output is not dict "

def test_download_point_data():
# test whether the shape(content) of output is equal to what we need     
    
    lat0 =  30  ; lat1 = 40
    lon0 =  -123; lon1 = -113

    map_extent = [lon0, lon1, lat0, lat1]
    
    result_download_point_data = download_point_data(map_extent)
    
    shape_download_point_data = result_download_point_data.shape
    
    assert shape_download_point_data == (1234, 4)
    " *** error is shape of output is not (1234, 4)"   
    
def test_my_point_data():
 #test whether the output of function is not empty
    
    lat0 =  30  ; lat1 = 40
    lon0 =  -123; lon1 = -113

    map_extent = [lon0, lon1, lat0, lat1]
    
    result_my_point_data = my_point_data(map_extent)
    
    shape_my_point_data = result_my_point_data.shape
   
    assert shape_my_point_data == (1234, 4)
    " *** error is shape of output is not (1234, 4)"
    
    
def test_download_raster_data():
 # test whether the shape(content) of output is equal to what we need   

    result_download_raster_data = download_raster_data()
    
    shape_download_raster_data = result_download_raster_data.shape
    
    assert shape_download_raster_data == (1801, 3601, 3)
    " *** error is shape of output is not (1801, 3601, 3)"
    
def test_my_global_raster_data():
 #test whether the output of function is not empty

    result_my_global_raster_data = my_global_raster_data()
    
    shape_my_global_raster_data = result_my_global_raster_data.shape
    
    assert shape_my_global_raster_data == (1801, 3601, 3)
    " *** error is shape of output is not (1801, 3601, 3)"