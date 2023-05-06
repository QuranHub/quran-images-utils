import os
from PIL import Image

# Define the input and output folder paths
input_folder = "hafs-wasat-kfgqpc-original"
output_folder = "hafs-wasat-kfgqpc-prepared"

# Define the offsets for even and odd pages
even_offsets = (129, 197, 141, 143)
odd_offsets = (129, 197, 141, 143)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Loop through all the image files in the input folder
for i in range(1, 605):
    # Construct the input and output file paths
    input_file = os.path.join(input_folder, f"{i:03}.jpg")
    output_file = os.path.join(output_folder, f"{i:03}.jpg")
    
    # Open the image file
    image = Image.open(input_file)

    # Get the dimensions of the image
    width, height = image.size

    # Determine the offsets to use based on whether the page is even or odd
    if i % 2 == 0:
        left_offset, right_offset, top_offset, bottom_offset = even_offsets
    else:
        left_offset, right_offset, top_offset, bottom_offset = odd_offsets

    # Calculate the new image dimensions
    new_width = width - (left_offset + right_offset)
    new_height = height - (top_offset + bottom_offset)

    # Crop the image
    cropped_image = image.crop((left_offset, top_offset, width - right_offset, height - bottom_offset))

    # Resize the cropped image to ensure that all the final output images are of the same size
    cropped_image = cropped_image.resize((new_width, new_height))

    # Save the cropped image
    cropped_image.save(output_file)

    print(f"Prepared {i} of 604")