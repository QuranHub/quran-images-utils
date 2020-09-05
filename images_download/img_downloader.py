#!/usr/bin/python3
# Python program to download images where the images files names are number increments
import wget
from os import makedirs
from os.path import exists, join

# Quran images sources
# [1] kfgqpc-quran-hafs-wasat: 'https://epub.qurancomplex.gov.sa/issues/hafs/wasat39/files/pages/svg/{}.jpg'  (4:607)
# [2] kfgqpc-quran-warsh: 'https://epub.qurancomplex.gov.sa/issues/qiraat/warsh39/files/pages/svg/{}.jpg'  (4:607)
# [3] hafs-otlooha: 'https://quran.gplanet.tech/hafs/images/{}.png'   (1:604)
# [4] warsh-otlooha: 'https://quran.gplanet.tech/warsh/images/{}.png'   (1:604)

# Download info
URL = 'https://epub.qurancomplex.gov.sa/issues/qiraat/warsh39/files/pages/svg/{}.jpg'
START_COUNT = 4
END_COUNT = 607
DOWNLOAD_DIR = '/home/abdallah/Projects/quran-images/kfgqpc-quran-warsh/'

if not exists(DOWNLOAD_DIR):
    makedirs(DOWNLOAD_DIR)

print('Beginning file download')

for i in range(START_COUNT, END_COUNT+1):
    print('\nDownload {} started...'.format(i))
    wget.download(URL.format(i), join(DOWNLOAD_DIR + '{}.jpg'.format(i - START_COUNT + 1)))