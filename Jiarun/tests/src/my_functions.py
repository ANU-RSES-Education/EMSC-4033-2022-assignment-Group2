"""
Functions we would like to test should be consistent with Jiarun/src/my_functions
"""

from .dependencies import *

def my_documentation():
    '''
    This function returns a Markdown document explaining information of this program. 
    '''

    markdown_documentation = """   
# Map plotting

In this notbook, we plot a high-resolution map at the region of 30-40°N, 113-123°W. The map displays a variety of information containing coastlines and water features, locations of past earthquake events, seafloor age and topography on the basemap. The following explains more information about how each element of the map is obtained and plotted.
 
## Basemap

At first, image tiles are required as the basemap. `cartopy` implements the functionality to get access to various sources providing map image tiles. 
[Mapbox](https://docs.mapbox.com/api/maps/styles/) provides a lot of map styles allowing us to choose. Here, we use **Mapbox outdoors**, which provides vivid natural features, topopraphy as well as roadways and built fatures. we need to login into mapbox [website](https://docs.mapbox.com/api/maps/styles/) to get an `access_token`.
The full list of image tiles and their sources can be found in the source code in [Github](https://github.com/SciTools/cartopy/blob/master/lib/cartopy/io/img_tiles.py).

## Coastlines and water features

Then, coastlines and water features containing lakes, reivers and ocean are added to the basemap. `cartopy.feature.NaturalEarthFeature` provides interfaces to obtain them at a specified resolution, i.e. ‘10m’, ‘50m’, or ‘110m’ corresponding to 1:10,000,000, 1:50,000,000, and 1:110,000,000 respectively. In this case, the coastlines are plotted at the resolution of '10m' and the water features are plotted at the resolution of '50m'.

## Earthquake events

In this case, 3-year (1977-1979) earthquake events occurred within a specified region are collected. The records of earthquake events are input as point data from **IRIS** (Incorporated Research Institution for Seismology) using the functions from `obspy` package. Each point datum consists of 4 parameters: longitude, latitude and depth of the origin and magnitude of the earthquake.


## Seafloor age

Seafloor age data are stored on `Cloudstor`, which provides cloud storage service helping people upload and download data anywhere. Seafloor age information is displayed on the map applying a diverging colormap from red to blue.


"""
    
    return markdown_documentation



def my_coastlines(resolution):
    """ 
    Returns the cartopy features of coastlines at the requested resolution, for example, .
    """

    import cartopy.feature as cfeature

    return cfeature.NaturalEarthFeature('physical', 'coastline', resolution, # Name = 'coastline'
                                        edgecolor=(0.0,0.0,0.0),# Black edge
                                        facecolor= "none")


def my_water_features(resolution, lakes=True, rivers=True, ocean=False):
    """
    Returns a [list] of cartopy features at the requested resolution, for example, '10m', '50m' or '110m'.
    The water features that want to be returned can be specified. Ocean features are not returned by default.
    """

    features = [] # return a list

    import cartopy.feature as cfeature

    lake_feature = cfeature.NaturalEarthFeature('physical', 'lakes', resolution,
                                        facecolor= "blue")
    river_feature = cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', resolution,
                                        facecolor= "none")
    ocean_feature = cfeature.NaturalEarthFeature('physical', 'ocean', resolution,
                                        facecolor= "blue")


    # determine which water features are required
    if rivers == True:
        features.append(river_feature)

    if lakes == True:
        features.append(lake_feature)

    if ocean == True:
        features.append(ocean_feature)

    return features

def my_basemaps():
    """
    Returns a dictionary of map tile generators that cartopy can use.
    It contains: "mapbox_outdoors", "open_street_map" now.
    """

    ## The full list of available interfaces is found in the source code for this one:
    ## https://github.com/SciTools/cartopy/blob/master/lib/cartopy/io/img_tiles.py

    # dictionary of possible basemap tile objects
    mapper = {"open_street_map":0, "mapbox_outdoors":0}

    ## Open Street map
    mapper["open_street_map"] = cimgt.OSM()
    
    ## Open outdoors map
    mapper["mapbox_outdoors"] = cimgt.MapboxTiles(access_token = "pk.eyJ1IjoiamlhcnVuIiwiYSI6ImNsMnBxZmliazAxZ3Ezam5xZGUwMWhobmYifQ.q52OXYQru12b3_2siR1OxQ",
                                                  map_id = "outdoors-v11")

    return mapper


## specify some point data (e.g. global seismicity in this case)
def download_point_data(region):
    """
    Returns a np.array of earthquake features containing the longitude, latitude and depth of origins and earthquake magnitudes.
    The range of the earthquake occurring region should be input as the form of [min_lon, max_lon, min_lat, max_lat].
    """

    from obspy.core import event
    from obspy.clients.fdsn import Client
    from obspy import UTCDateTime

    # Set data source
    client = Client("IRIS")
    
    time_start = UTCDateTime("1977-01-01")
    time_end  = UTCDateTime("1980-01-01")

    cat = client.get_events(starttime = time_start, endtime = time_end,
                           minlatitude = region[2],maxlatitude = region[3],
                            minlongitude = region[0],maxlongitude = region[1])

    print ("Point data: {} events in catalogue".format(cat.count()))

    # Unpack the obspy data into a plottable np.array
    event_count = cat.count()

    eq_origins = np.zeros((event_count, 4))

    for i in range(event_count):
        eq_origins[i][0] = cat[i].origins[0].longitude
        eq_origins[i][1] = cat[i].origins[0].latitude
        eq_origins[i][2] = cat[i].origins[0].depth
        eq_origins[i][3] = cat[i].magnitudes[0].mag

    return eq_origins


def my_point_data(region):
    '''
    Download earthquake event data using the defined function: download_point_data().
    Region should be provided as the form of [min_lon, max_lon, min_lat, max_lat].
    '''

    data = download_point_data(region)

    return data


## - Some global raster data (lon, lat, data) global plate age, in this example
def download_raster_data():
    '''
    Returns a np.array of seafloor ages with longitude and latitude.
    '''

    # Seafloor age data and global image - data from Earthbyters

    # The data come as ascii lon / lat / age tuples with NaN for no data. 

    from cloudstor import cloudstor
    
    # Download data from cloudstor
    teaching_data = cloudstor(url="L93TxcmtLQzcfbk", password='')
    teaching_data.download_file_if_distinct("global_age_data.3.6.z.npz", "global_age_data.3.6.z.npz")

    ages = np.load("global_age_data.3.6.z.npz")["ageData"]
    
    datasize = (1801, 3601, 3)
    
    # Create a global grid coordinate array
    raster_data = np.empty(datasize)
    
    lats = np.linspace(90, -90, datasize[0])
    lons = np.linspace(-180.0,180.0, datasize[1])
    
    arrlons,arrlats = np.meshgrid(lons, lats)
    
    raster_data[...,0] = arrlons[...] # Longitude
    raster_data[...,1] = arrlats[...] # Latitude
    raster_data[...,2] = ages[...] # Add age data to the array

    return raster_data


def my_global_raster_data():
    '''
    Download seafloor age data using the defined function: download_raster_data().
    '''

    raster = download_raster_data()

    return raster
