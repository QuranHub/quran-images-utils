#!/bin/sh
# A shell script to modify & prepare the Quran images for use in apps or websites.
# Author : Abdallah Abdelazim

# Crop the images to remove the blank spaces at the four sides
echo "STEP 1: cropping the images"
python3 crop.py

# Remove the images white background
echo "STEP 2: remove the images white background"
python3 remove_white_bg.py

# Resize & scale down the images in order to reduce its file size
echo "STEP 3: resize the images"
python3 resize.py

# Finally, optimize & compress the images to further reduce their file sizes
echo "STEP 4: optimize the images"
./optimize.sh
