#!/usr/bin/python3
# Python program to resize the Quran images.
# Author : Abdallah Abdelazim
from os import makedirs, listdir
from os.path import exists, isfile, join, splitext

from PIL import Image

# Images source & output directories
SRC_DIR = '/home/abdallah/Desktop/resize_test/'
OUT_DIR = '/home/abdallah/Desktop/resize_test_out/'
# Image new size
SIZE = {
    'page_1_2': (1080, 1462),
    'page_other': (1080, 1612)
}

if not exists(OUT_DIR):
    makedirs(OUT_DIR)

files = [f for f in listdir(SRC_DIR) if isfile(join(SRC_DIR, f))]

for f in files:
    fpath = join(SRC_DIR, f)
    img = Image.open(fpath)

    imageNum = int(splitext(f)[0])
    if imageNum == 1 or imageNum == 2:
        resizedImg = img.resize(SIZE['page_1_2'])
    else:
        resizedImg = img.resize(SIZE['page_other'])

    outpath = join(OUT_DIR, f)
    resizedImg.save(outpath)
    print('Saved {}'.format(f))
