# Python program to remove the white background from the images in a given
# directory & make them transparent PNGs.
# Based on the following ST answer: https://stackoverflow.com/a/765774/8555796
from PIL import Image
from os import makedirs, listdir
from os.path import exists, isfile, join, splitext

# Images source & output directories
SRC_DIR = '/home/abdallah/Projects/quran-images/kfgqpc-quran-hafs-wasat/'
OUT_DIR = '/home/abdallah/Projects/quran-images/kfgqpc-quran-hafs-wasat-mod/'

if not exists(OUT_DIR):
    makedirs(OUT_DIR)

files = [f for f in listdir(SRC_DIR) if isfile(join(SRC_DIR, f))]

for f in files:
    img = Image.open(join(SRC_DIR, f))
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    newImg = join(OUT_DIR, splitext(f)[0] + '.png')
    img.save(newImg, "PNG")
    print('Saved {}'.format(newImg))