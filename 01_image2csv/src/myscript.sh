#!/bin/sh

dir_path="../input/*"
dirs=`find $dir_path -maxdepth 0 -type f -name *.bmp`

for dir in $dirs;
do
    echo $dir
    python3 ConvertImg2csv.py $dir
done