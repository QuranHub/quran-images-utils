#!/usr/bin/env python3 
# Purpose: Prepare the Quran images.
# Author: Abdallah Abdelazim
# Features:
# - Crop the images to remove the borders.
# - Resize & optimize the images to decrease the image size.
# - The input images are expected to be in the images folder.
# - Save the output images in the output folder.
# - The input & output images are named as 001.jpg, 002.jpg, etc.
# Pre-requisites:
# - Python 3.6 or higher.
# - Pillow package (pip install pillow).
#
import os
from PIL import Image
from pathlib import Path
import subprocess

# Define the input and output folder paths
script_folder = os.path.dirname(__file__)
input_folder = os.path.join(script_folder, "images")
output_folder = os.path.join(script_folder, "output")

# Define the crop offsets (pixels) for pages
# (left, right, top, bottom)
first_two_pages_offsets = (126, 126, 208, 208)
even_pages_offsets = (195, 129, 143, 143)
odd_pages_offsets = (128, 196, 143, 143)

# Define the resize ratio for pages
resize_ratio = 0.5

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Loop through all the image files in the input folder
# The image file name is expected to be like 001.jpg, 002.jpg, etc.
for i in range(1, 605):
    # Construct the input and output file paths
    input_file = os.path.join(input_folder, f"{i:03}.jpg")
    output_file = os.path.join(output_folder, f"{i:03}.jpg")
    
    # Open the image file
    image = Image.open(input_file)

    # Get the dimensions of the image
    width, height = image.size

    # Determine the offsets to use based on whether the page is even or odd
    if i == 1 or i == 2:
        left_offset, right_offset, top_offset, bottom_offset = first_two_pages_offsets
    elif i % 2 == 0:
        left_offset, right_offset, top_offset, bottom_offset = even_pages_offsets
    else:
        left_offset, right_offset, top_offset, bottom_offset = odd_pages_offsets

    # Calculate the new image dimensions
    new_width = int((width - (left_offset + right_offset)) * resize_ratio)
    new_height = int((height - (top_offset + bottom_offset)) * resize_ratio)

    # Crop the image
    cropped_image = image.crop((left_offset, top_offset, width - right_offset, height - bottom_offset))

    # Resize the cropped image to ensure that all the final output images are of the same size
    cropped_image = cropped_image.resize((new_width, new_height))

    # Save the cropped image
    cropped_image.save(output_file, optimize=True, quality=85)

    print(f"Prepared {i} of 604")

print("Done preparing images")

