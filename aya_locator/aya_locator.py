import cv2
import numpy as np

# Load the input image and the template image
input_image = cv2.imread('page_resized.jpg')
template = cv2.imread('template_resized.jpg')

# Get the height and width of the template image
template_height, template_width = template.shape[:2]

# Set a threshold for the correlation coefficient
threshold = 0.6

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

# Print the coordinates of the distinct occurrences
for loc in distinct_locations:
    print(f"Distinct occurrence at ({loc[0]}, {loc[1]})")

# Draw a rectangle around the matched region for each occurrence of the template image
for loc in distinct_locations:
    x, y = loc
    cv2.rectangle(input_image, (x, y), (x + template_width, y + template_height), (0, 0, 255), 2)

# Display the input image with the matched regions highlighted
cv2.imshow('Matched regions', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()