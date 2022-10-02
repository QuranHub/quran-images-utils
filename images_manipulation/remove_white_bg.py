#!/usr/bin/python3
# Python program to remove the white background from the images in a specified
# directory & make them transparent PNGs.
# Based on the following ST answer: https://stackoverflow.com/a/765774/8555796
# Author : Abdallah Abdelazim
from os import makedirs, listdir
from os.path import exists, isfile, join, splitext

from PIL import Image

# Images source & output directories
SRC_DIR = '/home/abdallah/Desktop/test_remove_bg/'
OUT_DIR = '/home/abdallah/Desktop/test_remove_bg_out/'

if not exists(OUT_DIR):
    makedirs(OUT_DIR)

files = [f for f in listdir(SRC_DIR) if isfile(join(SRC_DIR, f))]

for f in files:
    img = Image.open(join(SRC_DIR, f))
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    threshold = 15
    for item in datas:
        if item[0] > 175 and item[1] > 175 and item[2] > 175 and \
                abs(item[0] - item[1]) < threshold and \
                abs(item[1] - item[2]) < threshold and \
                abs(item[0] - item[2]) < threshold:
            # convert white (& light grey) pixels to transparent ones
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    newImg = join(OUT_DIR, splitext(f)[0] + '.png')
    img.save(newImg, "PNG")
    print('Saved {}'.format(newImg))
