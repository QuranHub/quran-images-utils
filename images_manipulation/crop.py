#!/usr/bin/python3
# Python program to crop the images with a specified box boundary.
# Author : Abdallah Abdelazim
from PIL import Image
from os import makedirs, listdir
from os.path import exists, isfile, join, splitext

# Images source & output directories
SRC_DIR = '/home/abdallah/Projects/quran-images/hafs-wasat-no-bg/'
OUT_DIR = '/home/abdallah/Projects/quran-images/hafs-wasat-final/'
# cropping boxes (box=(left, upper, right, lower))
CROP_BOXES = {
    'page_1_2': (126, 207, 1812, 2489),
    'page_even': (195, 143, 1809, 2553),
    'page_odd': (128, 143, 1742, 2553)
}

if not exists(OUT_DIR):
    makedirs(OUT_DIR)

files = [f for f in listdir(SRC_DIR) if isfile(join(SRC_DIR, f))]

for f in files:
    fpath = join(SRC_DIR, f)
    img = Image.open(fpath)

    imageNum = int(splitext(f)[0])
    if imageNum == 1 or imageNum == 2:
        croppedImg = img.crop(CROP_BOXES['page_1_2'])
    elif imageNum%2 == 0:
        croppedImg = img.crop(CROP_BOXES['page_even'])
    else:
        croppedImg = img.crop(CROP_BOXES['page_odd'])
    
    outpath = join(OUT_DIR, f)
    croppedImg.save(outpath)
    print('Saved {}'.format(f))
