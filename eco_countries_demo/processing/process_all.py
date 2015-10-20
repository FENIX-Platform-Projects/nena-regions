from eco_countries_demo.processing import average_rasterio
from eco_countries_demo.processing import anomalies_rasterio
from eco_countries_demo.processing import anomaly_dpy_rasterio
from eco_countries_demo.processing import variance_rasterio
from eco_countries_demo.processing import standard_deviation_rasterio
from eco_countries_demo.processing import zscore_rasterio

#average
#anomaly
#anomaly dpy(difference of the month respect to previuos year)
#standard deviation
#zscore

average_rasterio.process_all()
anomalies_rasterio.process_all()
anomaly_dpy_rasterio.process_all()
standard_deviation_rasterio.process_all()
zscore_rasterio.process_all()
