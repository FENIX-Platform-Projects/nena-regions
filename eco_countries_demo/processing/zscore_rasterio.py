import glob
import rasterio
from eco_countries_demo.processing.utils_rasterio import initialize_rasterio_raster
from eco_countries_demo.processing.utils import get_month_by_filename, get_date_by_filename


def calc(basepath, layers, filename, epsg="3857"):
    print "-----Z-SCORE"
    for layer in layers:
        date = get_date_by_filename(layer)
        month = get_month_by_filename(layer)
        sd_path = basepath + "/sd/" + filename + "_" + month + "_" + epsg + ".tif"
        output_path = basepath + "/zscore/" + filename + "_" + date + "_" + epsg + ".tif"


        print "Processing: ", layer, " ", sd_path
        r = rasterio.open(layer)
        r_sd = rasterio.open(sd_path)
        data, kwargs = initialize_rasterio_raster(r, rasterio.float32)
        r_band = r.read_band(1)
        r_sd_band = r_sd.read_band(1)


        nodata = 0
        index1 = (r_band != nodata)
        index2 = (r_sd_band != nodata)
        r_band = index1 * index2 * r_band
        r_sd_band = index1 * index2 * r_sd_band

        data = (r_band.astype(float) / r_sd_band.astype(float))

        # writing
        print "Writing: ", output_path
        with rasterio.open(output_path, 'w', **kwargs) as dst:
            dst.write_band(1, data.astype(rasterio.float32))

def process_all(basepath, basename):
    layers = glob.glob(basepath + basename + "/anomalies/*.tif")
    calc(basepath + basename, layers, basename)
