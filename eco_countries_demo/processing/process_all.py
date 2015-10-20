import getpass
from eco_countries_demo.processing import average_rasterio
from eco_countries_demo.processing import anomalies_rasterio
from eco_countries_demo.processing import anomaly_dpy_rasterio
from eco_countries_demo.processing import variance_rasterio
from eco_countries_demo.processing import standard_deviation_rasterio
from eco_countries_demo.processing import zscore_rasterio


# SEQUENCE
#   average
#   anomaly
#   anomaly dpy(difference of the month respect to previuos year)
#   standard deviation
#   zscore

basepath = '/media/'+getpass.getuser()+'/LaCie/NENA_REGION/MOD13A3'

average_rasterio.process_all(basepath)             #/avg
anomalies_rasterio.process_all(basepath)           #/anomalies
anomaly_dpy_rasterio.process_all(basepath)          #/anomalies_dpy
standard_deviation_rasterio.process_all(basepath)   #/sd
zscore_rasterio.process_all(basepath)               #/zscore
