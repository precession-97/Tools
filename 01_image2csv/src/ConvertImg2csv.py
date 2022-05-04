import csv
import numpy
import os

import cv2    # OpenCV

ext = "jpg"
img_name = "test"
csv_name = "test"

input_path = r'../input'
output_path = r'../output'

fname = img_name + "." + ext
fpath = os.path.join(input_path, fname)
bgr_array = cv2.imread(fpath)

fnamelist = ["_b", "_g", "_r"]
for bgr in range(3):
    colorArray = numpy.array(bgr_array[:,:,bgr])
    csvname = csv_name + fnamelist[bgr] + ".csv"
    csvpath = os.path.join(output_path, csvname)
    numpy.savetxt(csvpath, colorArray, fmt = "%.0f", delimiter = ",")

