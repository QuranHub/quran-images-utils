#!/usr/bin/env python3
# Purpose: Locate the Aya in the Quran images.
# Author: Abdallah Abdelazim
# Features:
# - Locate the Aya in the Quran images.
# - The input images are expected to be in the 'images' sub-folder.
# - The 'template.jpg' image is expected to be in the same folder as this script.
# - The input & output images are named as 001.jpg, 002.jpg, etc.
# - The output is the coordinates of the Aya in each image.
# - The output is saved to 'data.csv'.
# Pre-requisites:
# - Python 3.6 or higher.
# - OpenCV package (pip install opencv-python).
# - Numpy package (pip install numpy).
#
import os
import cv2
import numpy as np
import csv

def group_and_sort(points, group_y_threshold):
    """
    Groups the given points by y-coordinates with a maximum difference of `group_y_threshold` between each group.
    Within each group, sorts the points by x-coordinate in acending order.
    Returns a list of all points sorted.
    """
    groups = []
    current_group = []

    # Sort points by y-coordinate
    points_sorted = sorted(points, key=lambda p: p[1])

    # Group points by y-coordinate with a maximum difference of group_y_threshold
    for point in points_sorted:
        if not current_group or abs(point[1] - current_group[0][1]) <= group_y_threshold:
            current_group.append(point)
        else:
            groups.append(current_group)
            current_group = [point]
    groups.append(current_group)

    # Sort each group by x-coordinate in ascending order
    for group in groups:
        group.sort(key=lambda p: -p[0])

    # Flatten groups into a single list
    result = [point for group in groups for point in group]

    return result



# Set a threshold for the correlation coefficient (template matching)
threshold = 0.4

# Define the input and output folder paths
script_folder = os.path.dirname(__file__)
images_folder = os.path.join(script_folder, "images")

# Aya templates
# template_1 is for the first two pages
# template_2 is for the rest of the pages
template_1 = cv2.imread(os.path.join(script_folder, "template_1.jpg"))
template_2 = cv2.imread(os.path.join(script_folder, "template_2.jpg"))

# Aya ID counter
aya_id = 1

# Quran aya coordinates
output_data = []

# Total number of ayas in Quran
# Hafs: 6236
total_ayas = 6236

# Show the preview of the input image with the matched location
show_preview = False

# Loop through all the image files in the images folder
# The image file name is expected to be like 001.jpg, 002.jpg, etc.
for i in range(1, 605):

    if i == 1 or i == 2:
        template = template_1
    else:
        template = template_2
        
    # Get the height and width of the template image
    template_height, template_width = template.shape[:2]

    # Load the input image and the template image
    input_image = cv2.imread(os.path.join(images_folder, f"{i:03}.jpg"))

    # Find the location of the template image in the input image
    result = cv2.matchTemplate(input_image, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    # Filter out nearby occurrences
    min_distance = max(template_height, template_width)
    distinct_locations = []
    for loc1 in locations:
        is_distinct = True
        for loc2 in distinct_locations:
            distance = np.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)
            if distance < min_distance:
                is_distinct = False
                break
        if is_distinct:
            distinct_locations.append(loc1)

    sorted_distinct_locations = group_and_sort(distinct_locations, template_height / 2)

    # Print the coordinates of the distinct occurrences
    for loc in sorted_distinct_locations:
        print(f"Aya {aya_id} -> ({loc[0]}, {loc[1]})")
        output_data.append([aya_id, i, loc[0], loc[1]])
        aya_id += 1

    if show_preview:
        # Draw a rectangle around the matched region for each occurrence of the template image
        for loc in sorted_distinct_locations:
            x, y = loc
            cv2.rectangle(input_image, (x, y), (x + template_width, y + template_height), (0, 0, 255), 2)

        # Display the input image with the matched regions highlighted
        cv2.imshow('Matched regions', input_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Check if ther're any missing aya matches
if aya_id - 1 != total_ayas:
    print(f"Error: Missing {total_ayas - (aya_id - 1)} aya matches")
else:
    print("All ayas are matched successfully")

# Save the output data to a CSV file
with open(os.path.join(script_folder, "data.csv"), "w", newline="") as f:
    writer = csv.writer(f)

    # Write header row
    writer.writerow(['aya_id', 'page', 'x', 'y'])

    writer.writerows(output_data)

