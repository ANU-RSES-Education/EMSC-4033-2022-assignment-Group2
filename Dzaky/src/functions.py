# a random placeholder function to be replaced with
# actual functional functions :)

def function_try(x):
    return x**2 + x*2 + x


def paying_debt(outstanding):
    """obtained from the exercise about For and While loop.
    It calculate the incoming months you will get
    to be able to fully repay your debt"""
    
    repayment = 2000 #Define amount that should be paid every month
    paid_amount = 0 
    months = 0
    early_rate = 0.023 #interests rate for Year 1 and Year 2
    later_rate = 0.041 #interests rate for Year 3 and so on

    while outstanding > 0:
        if months <= 24:
            paid_amount = paid_amount + repayment
            outstanding = outstanding - repayment + (outstanding - repayment)*(early_rate/12)
            months += 1
        else:
            paid_amount = paid_amount + repayment
            outstanding = outstanding - repayment + (outstanding - repayment)*(later_rate/12)
            months += 1
    print("total months=", months)
    return months

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

def city_to_city():
    """obtained from the Python exercise about Map and Cartopy.
    Transform the map projection from geodetic to PlateCarree
    Plot the line that connect the location between the two cities on top of the map
    In this case, we are going to plot the line between Jakarta and Canberra"""
    
    ax = plt.axes(projection=ccrs.PlateCarree()) #Choose map projection
    ax.set_extent((94, 155, -37.5, 7)) #Define map extent
    ax.coastlines()
    ax.stock_img()
    
    jak_lat, jak_lon = -6.2, 106.8 #Latitude and longitude of Jakarta
    can_lat, can_lon = -35.2, 149.1 #Latitude and longitude of Canberra
    
    # New bit: transform the given lat/lon points into the Plate Carree projection
    geodetic = ccrs.Geodetic()
    pc = ccrs.PlateCarree()
    jak_lon_t, jak_lat_t = pc.transform_point(jak_lon, jak_lat, geodetic)
    can_lon_t, can_lat_t = pc.transform_point(can_lon, can_lat, geodetic)
    
    plt.plot([jak_lon_t, can_lon_t], [jak_lat_t, can_lat_t],
         color='blue', linewidth=1, marker='o', markersize=3,
         # Be explicit about which transform you want:
         transform=pc)
    
    plt.show()
# -


