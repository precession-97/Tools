import csv
import numpy
import os
import sys

import cv2    # OpenCV

if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        # 引数から対象画像のパスを取得
        img_path = os.path.join('../input/', args[1])

        bgr_array = cv2.imread(img_path)

        fnamelist = ["_b", "_g", "_r"]
        for bgr in range(3):
            colorArray = numpy.array(bgr_array[:,:,bgr])
            csvname = os.path.splitext(os.path.basename(args[1]))[0] + fnamelist[bgr] + ".csv"
            csvpath = os.path.join('../output/', csvname)
            numpy.savetxt(csvpath, colorArray, fmt = "%.0f", delimiter = ",")
    else:
        print('Arguments are too short')
