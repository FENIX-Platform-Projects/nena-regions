from eco_countries_demo.processing import average_rasterio
from eco_countries_demo.processing import anomalies_rasterio_diff
from eco_countries_demo.processing import anomalies_rasterio_percentage
from eco_countries_demo.processing import anomaly_dpy_rasterio_diff
from eco_countries_demo.processing import variance_rasterio
from eco_countries_demo.processing import standard_deviation_rasterio
from eco_countries_demo.processing import zscore_rasterio
import getpass

# Temperatures:
# Anomaly AVG: Celsius degree
# Anomaly DPY: Celsius degree
#
# ET:
# Anomaly AVG: mm/month
# Anomaly DPY: mm/month
#
# Rainfall:
# Anomaly AVG: mm
# Anomaly DPY: mm
#
# NDVI
# Anomaly AVG: %
# Anomaly DPY: %

#basepath = "/media/"+getpass.getuser()+"/LaCie/NENA_REGION/"
basepath = "/home/"+getpass.getuser()+"/Desktop/NENA_REGION/"

# basename = "CHIRPS"
# average_rasterio.process_all(basepath, basename)
# anomalies_rasterio_percentage.process_all(basepath, basename)
# anomalies_rasterio.process_all(basepath, basename)
# anomaly_dpy_rasterio_diff.process_all(basepath, basename)
# standard_deviation_rasterio.process_all(basepath, basename)
# zscore_rasterio.process_all(basepath, basename)

# TEMPERATURE
basename = "MYD11C3"
# average_rasterio.process_all(basepath, basename)
#anomalies_rasterio_diff.process_all(basepath, basename)
#anomaly_dpy_rasterio_diff.process_all(basepath, basename)
standard_deviation_rasterio.process_all(basepath, basename)
zscore_rasterio.process_all(basepath, basename)

# EVAPOTRASPIRTION
# basename = "MOD16/ET"
# anomaly_dpy_rasterio_diff.process_all(basepath, basename)

