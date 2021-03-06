import glob
import rasterio
import getpass
from geobricks_common.core.filesystem import get_filename
from eco_countries_demo.processing.utils_rasterio import initialize_rasterio_raster
from eco_countries_demo.processing.utils import get_month_by_filename, get_year_by_filename, get_base_filename
import numpy


def calc(basepath, output_path, layers, epsg="3857"):
    print "-----Anomaly DPY"


    for layer in layers:
        # print get_year_by_filename(layer)
        year = get_year_by_filename(layer)

        data = None
        month = get_month_by_filename(layer)
        filename = get_filename(layer)
        base_filename = get_base_filename(filename)
        yearPrev = str(int(year) - 1)

        layerPrev = basepath + "/" + base_filename + "_" + yearPrev + month + "_" + epsg + ".tif"

        print "Processing: ", layer, layerPrev

        try:
            print "Reading: ",  layer
            r = rasterio.open(layer)
            r_data = r.read_band(1).astype(float)

            print "Reading: ",  layerPrev
            r_prev = rasterio.open(layerPrev)
            r_prev_data = r_prev.read_band(1).astype(float)

            if data is None:
                data, kwargs = initialize_rasterio_raster(r, rasterio.float32)


            nodata = 0
            index1 = (r_data != nodata)
            index2 = (r_prev_data != nodata)
            r_data = index1 * index2 * r_data
            r_prev_data = index1 * index2 * r_prev_data
            data = r_data - r_prev_data

            # writing
            output_layer_path = output_path + "/" + filename + ".tif"
            print "Writing: ", output_layer_path
            with rasterio.open(output_layer_path, 'w', **kwargs) as dst:
                dst.write_band(1, data.astype(rasterio.float32))
        except Exception, e:
            print e

def process_all(basepath, basename):
    output_path = basepath + basename + "/anomalies_dpy"
    layers = glob.glob(basepath + basename + "/*.tif")
    calc(basepath + basename, output_path, layers)
