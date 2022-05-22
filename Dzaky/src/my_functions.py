"""All the functions we need to make a map:

    - my_documentation()
    - my_coastlines()
    - my_water_features()
    - my_basemaps()

"""

from .dependencies import *

def my_documentation():

    markdown_documentation = """ This function consist of information for each function in my_functions.py, and return the markdown document 
    
# Map Making

Plot high resolution map of particular region. The map displays various information, from basic geographical features such as coastline and water of bodies, to the past earthquake event locations and seafloor age
    
## Coastline
Fundamental geographical feature to plot, to map the global land and ocean
    
## Water Bodies
Subsequent geographical features including river and lakes
    
## Basemap
Set up a new Mapbox tiles instance. In this function, we will use Mapbox outdoor which displays natural features.Full list of available interface can be explroed here https://github.com/SciTools/cartopy/blob/master/lib/cartopy/io/img_tiles.p
    
## Point Data
Handle global events of earthquakes in certain periods (in this case 2000 - 2006). First, the earthquake data is obtained from IRIS. And then, specific functions from Obspy are utilized to get event  with requested parameters, such as latitude range, longitude range, and maximum depth, before being plotted.
    
## Raster Data
Handle global seafloor age data which is obtained from Cloudstor. 
    """
    
    return markdown_documentation


def my_coastlines(resolution):
    """ returns the relevant coastlines following the resolution in input, such as '10m' or '100m' """

    import cartopy.feature as cfeature

    return cfeature.NaturalEarthFeature('physical', 'coastline', resolution,
                                        edgecolor=(0.0, 0.0, 0.0),
                                        facecolor= "none")


def my_water_features(resolution, lakes=True, rivers=True, ocean=False):
    """Returns a list of cartopy features"""
    
    features = [] #create empty list

    river = cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', resolution, facecolor='blue')

    lake = cfeature.NaturalEarthFeature('physical', 'lakes', resolution, facecolor='blue')

    ocean = cfeature.NaturalEarthFeature('physical', 'ocean', resolution, facecolor='blue')
    
    #Add features to list
    if rivers == True:
        features.append(river)

    if lakes == True:
        features.append(lake)

    if ocean == True:
        features.append(ocean)

    return features

def my_basemaps():
    """Returns a dictionary of map tile generators that Cartopy can use
    This function stores open street and mapbox outdoor features"""


    ## The full list of available interfaces is found in the source code for this one:
    ## https://github.com/SciTools/cartopy/blob/master/lib/cartopy/io/img_tiles.py
    ## dictionary of possible basemap tile objects
    
    #Empty dictionary
    mapper = {}

    ## Open Street map
    mapper["open_street_map"] = cimgt.OSM()
    
    ##Open Outdoor map
    mapper["mapbox_outdoors"] = cimgt.MapboxTiles(access_token = "pk.eyJ1IjoiamlhcnVuIiwiYSI6ImNsMnBxZmliazAxZ3Ezam5xZGUwMWhobmYifQ.q52OXYQru12b3_2siR1OxQ",
                                                  map_id = "outdoors-v11")

    return mapper


## specify some point data (e.g. global seismicity in this case)

def download_point_data(area):
    """get data of multiple earthquake events with specified coordinates (lat and lon), depth, and magnitude"""
    
    #Import necessary module
    from obspy.core import event
    from obspy.clients.fdsn import Client
    from obspy import UTCDateTime

    client = Client("IRIS")

    # The function input is to define the seismic event observation area
    start_time = UTCDateTime("2001-01-01")
    end_time   = UTCDateTime("2006-01-01")

    #Obtain events with specified region
    cat = client.get_events(starttime = start_time, endtime = end_time,
                            minlatitude = area[2],maxlatitude = area[3],
                            minlongitude = area[0],maxlongitude = area[1], 
                            minmagnitude=4.0)

    print ("Point data: {} events in catalogue".format(cat.count()))

    ## Unpack the obspy data into a plottable array
    event_count = cat.count()
    eq_origin = np.zeros((event_count, 4))
    
    for i in range(event_count):
        eq_origin[i][0] = cat[i].origins[0].longitude
        eq_origin[i][1] = cat[i].origins[0].latitude
        eq_origin[i][2] = cat[i].origins[0].depth
        eq_origin[i][3] = cat[i].magnitudes[0].mag

    return eq_origin


def my_point_data(area):
    """download event data by call download_point_data()"""
    data = download_point_data(area)
    return data

## - Some global raster data (lon, lat, data) global plate age, in this example

def download_raster_data():
    """make an array of seafloor age along with coordinates"""

    # Seafloor age data and global image - data from Earthbyters
    # The data come as ascii lon / lat / age tuples with NaN for no data. 
    # This can be loaded with ...

#     # age = numpy.loadtxt("Resources/global_age_data.3.6.xyz")
#     # age_data = age.reshape(1801,3601,3)  
      # I looked at the data and figured out what numbers to use
#     # age_img  = age_data[:,:,2]

#     # But this is super slow, so I have just stored the Age data on the grid (1801 x 3601) which we can reconstruct easily

    from cloudstor import cloudstor
    teaching_data = cloudstor(url="L93TxcmtLQzcfbk", password='')
    teaching_data.download_file_if_distinct("global_age_data.3.6.z.npz", "global_age_data.3.6.z.npz")
    
    ages = np.load("global_age_data.3.6.z.npz")["ageData"]

    datasize = (1801, 3601, 3)
    
    #Create empty array
    raster_data = np.empty(datasize)
    
    #Fill the empty array
    lat = np.linspace(90.0, -90.0, datasize[0])
    lon = np.linspace(-180.0, 180.0, datasize[1])
    
    lon_array, lat_array = np.meshgrid(lon, lat) #Create coordinate grid from lat and lon
    
    raster_data[...,0] = lon_array[...] #Longitude
    raster_data[...,1] = lat_array[...] #Latitude
    raster_data[...,2] = ages[...] #Age

    return raster_data

def my_global_raster_data():
    """call download raster data which have been constructed to download the seafloor data"""
    raster = download_raster_data()
    return raster
