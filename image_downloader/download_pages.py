#!/usr/bin/env python3
# Purpose: Download the Quran pages.
# Author: Abdallah Abdelazim
# Features:
# - Download the Quran pages from a URL containing the page number.
# - The downloaded pages images are named as 001.jpg, 002.jpg, etc.
# - The pages are saved in the 'downloads' sub-folder.
# Pre-requisites:
# - Python 3.6 or higher.
# Notes:
# - You need to replace the URL with the correct URL for the pages with 
# a page number placeholder.
#
import os
import urllib.request

# Create the subfolder if it doesn't exist.
script_folder = os.path.dirname(__file__)
download_folder = os.path.join(script_folder, "downloads")
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Replace the placeholder with a number from 001 to 604.
for i in range(1, 605):
    url = f'https://easyquran.com/wp-content/HafsPages/images/{i:03d}.jpg'  # Format the number with leading zeros.
    filename = f'{i:03d}.jpg'  # Format the number with leading zeros.
    filepath = os.path.join(download_folder, filename)  # Create the full filep
    urllib.request.urlretrieve(url, filepath)  # Download the file.
    print(f'Downloaded {filename} to {filepath}')
