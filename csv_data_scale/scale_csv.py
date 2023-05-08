#!/usr/bin/env python3
# Purpose: Scale the coordinates of the Aya in the Quran images with a factor.
# Author: Abdallah Abdelazim
# Features:
# - Scale the coordinates of the Aya in the Quran images with a factor.
# - The input CSV file 'data.csv' is expected to be in the same folder as this script.
# - The output CSV file is saved to 'data_output.csv'.
# Pre-requisites:
# - Python 3.6 or higher.
#
import os
import csv

# Set the factor to multiply x and y values by
factor = 0.6

script_folder = os.path.dirname(__file__)
input_file = os.path.join(script_folder, "data.csv")
output_file = os.path.join(script_folder, "data_output.csv")

# Open the input and output CSV files
with open(input_file, mode='r') as input_file, open(output_file, mode='w', newline='') as output_file:

    # Create CSV reader and writer objects
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    # Read and write the header row
    header_row = next(csv_reader)
    csv_writer.writerow(header_row)

    # Loop through each row in the input CSV file
    for row in csv_reader:

        # Extract the "page", "x", and "y" values from the row
        aya_id = row[0]
        page = row[1]
        x = int(row[2])
        y = int(row[3])

        # Multiply the "x" and "y" values by the factor
        x *= factor
        y *= factor

        # Write the updated values to the output CSV file
        csv_writer.writerow([aya_id, page, int(x), int(y)])
    
    print("Done!")

