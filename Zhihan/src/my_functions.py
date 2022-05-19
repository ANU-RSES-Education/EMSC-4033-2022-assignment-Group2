"""All the functions we need to make a map:

    - my_documentation()
    - my_coastlines()
    - my_water_features()
    - my_basemaps()

"""

from .dependencies import *

def my_documentation():

    markdown_documentation = """   
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
    
    return markdown_documentation



def my_coastlines(resolution):
    """ returns the relevant coastlines at the requested resolution 10m"""

    import cartopy.feature as cfeature

    return cfeature.NaturalEarthFeature('physical', 'coastline', resolution,
                                        edgecolor=(0.0,0.0,0.0),
                                        facecolor="none")
    # We do this by function 'cfeature.NaturalEarthFeature' 

def my_water_features(resolution, lakes=True, rivers=True, ocean=False):
    """Returns a [list] of cartopy features in resolution or color of water features"""
    import cartopy.feature as cfeature
    features = []
    
    rivers_features = cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', resolution, edgecolor='Blue', facecolor="none")


    lakes_features = cfeature.NaturalEarthFeature('physical', 'lakes', resolution, edgecolor="blue", facecolor="blue")

    
    ocean_features = cfeature.NaturalEarthFeature('physical', 'ocean', resolution, edgecolor="green", facecolor="blue")
    
    if rivers == True:
        features.append(rivers_features)
    # add rivers features to the end of the list
    
    if lakes == True:
        features.append(lakes_features)
    # add lakes features to the end of the list
    
    if ocean == True:
        features.append(ocean_features)
   # add ocean features to the end of the list 

    return features

def my_basemaps():
    """Returns a dictionary of map tile generators that cartopy can use by 'open_street_map' and 'mapbox_outdoors' """
    
    ## The full list of available interfaces is found in the source code for this one:
    ## https://github.com/SciTools/cartopy/blob/master/lib/cartopy/io/img_tiles.py

    # dictionary of possible basemap tile objects
   
   
    ## Create a dictionary of map first
    mapper = {"open_street_map":0,"mapbox_outdoors":0} 
    
    ## Open Street map 
    mapper["open_street_map"] = cimgt.OSM()
   
    ## Open outdoors map
    mapper["mapbox_outdoors"] = cimgt.MapboxTiles(map_id='outdoors-v11', 
                                     access_token='pk.eyJ1IjoibG91aXNtb3Jlc2kiLCJhIjoiY2pzeG1mZzFqMG5sZDQ0czF5YzY1NmZ4cSJ9.lpsUzmLasydBlS0IOqe5JA')
    ## Use mapbox as basemap
    
 
    return mapper


## specify some point data (e.g. global seismicity in this case)

def download_point_data(region):
    """
    Function 'client.get_events' help us to obtain earthquake events we want by limiting time, latitude and longitude by region and magnitude.
    """
    from obspy.core import event
    from obspy.clients.fdsn import Client
    from obspy import UTCDateTime

    client = Client("IRIS")

    extent = region
    
    start_time = UTCDateTime("1995-01-01")
    end_time   = UTCDateTime("2022-01-01")
    
    cat = client.get_events(starttime = start_time, endtime = end_time,
                            minlatitude = region[2], maxlatitude = region[3],
                            minlongitude = region[0], maxlongitude = region[1],
                            minmagnitude = 4, maxmagnitude = 10)
    # The return value is a Catalog object which can contain any number of events.
    
    print ("Point data: {} events in catalogue".format(cat.count()))
    
    # Unpack the obspy data into a plottable array
    """
    We need to unpack the obspy data into a plottable array and return this np.array. We could use function 'np.zeros' and for loop to write the longtitude,       latitude, depth and magnitudes. 
    """
    event_count = cat.count()

    eq_origins = np.zeros((event_count, 4))
    # returns a zero-filled array of the given shape and type
    
    for i in range(event_count):
            eq_origins[i][0] = cat[i].origins[0].longitude
            eq_origins[i][1] = cat[i].origins[0].latitude
            eq_origins[i][2] = cat[i].origins[0].depth
            eq_origins[i][3] = cat[i].magnitudes[0].mag
 
    return eq_origins


def my_point_data(region):
    
    data = download_point_data(region)
    
    return data


## - Some global raster data (lon, lat, data) global plate age, in this example

def download_raster_data():
    """
    Return the np.array of seafloor ages with longitude, latitude and ages.
    """
    # Seafloor age data and global image - data from Earthbyters

    # The data come as ascii lon / lat / age tuples with NaN for no data. 
    # This can be loaded with ...

    # age = numpy.loadtxt("Resources/global_age_data.3.6.xyz")
    # age_data = age.reshape(1801,3601,3)  # I looked at the data and figured out what numbers to use
    # age_img  = age_data[:,:,2]

    # But this is super slow, so I have just stored the Age data on the grid (1801 x 3601) which we can reconstruct easily

    from cloudstor import cloudstor
    
    teaching_data = cloudstor(url="L93TxcmtLQzcfbk", password='')
    teaching_data.download_file_if_distinct("global_age_data.3.6.z.npz", "global_age_data.3.6.z.npz")

    ages = np.load("global_age_data.3.6.z.npz")["ageData"]
    # read numpy files
    datasize = (1801, 3601, 3)
                                               
    raster_data = np.empty(datasize)
    # return a array with radom data
    
    lats = np.linspace(90,-90,datasize[0])
    lons = np.linspace(-180,180,datasize[1])
    # Create arithmetic progression
    
    arrlons,arrlats = np.meshgrid(lons,lats)
    # Return coordinate matrices from coordinate vectors. 
    
    raster_data[...,0] = arrlons[...] 
    raster_data[...,1] = arrlats[...]
    raster_data[...,2] = ages[...]
        
    # Match the latitude, longitude and age of each point  
    return raster_data


def my_global_raster_data():

    raster = download_raster_data()
    
    return raster
