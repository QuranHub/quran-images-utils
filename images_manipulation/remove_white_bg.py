#!/usr/bin/python3
# Python program to remove the white background from the images in a specified
# directory & make them transparent PNGs.
# Based on the following ST answer: https://stackoverflow.com/a/765774/8555796
from PIL import Image
from os import makedirs, listdir
from os.path import exists, isfile, join, splitext

# Images source & output directories
SRC_DIR = '/home/abdallah/Projects/quran-images/kfgqpc-quran-hafs-wasat/'
OUT_DIR = '/home/abdallah/Projects/quran-images/hafs-wasat/'

if not exists(OUT_DIR):
    makedirs(OUT_DIR)

files = [f for f in listdir(SRC_DIR) if isfile(join(SRC_DIR, f))]

for f in files:
    img = Image.open(join(SRC_DIR, f))
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] > 230 and item[1] > 230 and item[2] > 230:
            # convert white (& light grey) pixels to transparent ones
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    newImg = join(OUT_DIR, splitext(f)[0] + '.png')
    img.save(newImg, "PNG")
    print('Saved {}'.format(newImg))
