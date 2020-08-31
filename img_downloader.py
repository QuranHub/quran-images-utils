# Python program to download images where image names are number increments
import wget
import os

# Download info
URL = 'https://epub.qurancomplex.gov.sa/issues/hafs/wasat39/files/pages/svg/{}.jpg'
START_COUNT = 4
END_COUNT = 607
DOWNLOAD_DIR = '/home/abdallah/Downloads/kfgqpc-quran-hafs-wasat/'

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

print('Beginning file download with wget module')

for i in range(START_COUNT, END_COUNT):
    print('\nDownload {} started...'.format(i))
    wget.download(URL.format(i), DOWNLOAD_DIR + '{}.jpg'.format(i - START_COUNT + 1))