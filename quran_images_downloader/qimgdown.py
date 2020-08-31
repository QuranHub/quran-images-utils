# Python program to download images where image names are number increments
import wget
import os

# Quran images sources
# [1] kfgqpc-quran-hafs-wasat-hq: 'https://epub.qurancomplex.gov.sa/issues/hafs/wasat39/files/pages/svg/{}.jpg'  (4:607)
# [2] kfgqpc-quran-hafs-wasat: 'https://epub.qurancomplex.gov.sa/issues/hafs/wasat39/files/pages/tablet/{}.jpg'  (4:607)
# [3] wasat-otlooha: 'https://quran.gplanet.tech/hafs/images/{}.png   (1:604)

# Download info
URL = 'https://epub.qurancomplex.gov.sa/issues/hafs/wasat39/files/pages/svg/{}.jpg'
START_COUNT = 4
END_COUNT = 607
DOWNLOAD_DIR = '/home/abdallah/Downloads/kfgqpc-quran-hafs-wasat/'

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

print('Beginning file download with wget module')

for i in range(START_COUNT, END_COUNT+1):
    print('\nDownload {} started...'.format(i))
    wget.download(URL.format(i), DOWNLOAD_DIR + '{}.jpg'.format(i - START_COUNT + 1))