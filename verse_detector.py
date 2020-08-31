# Python program to locate verses in Quran images
# using a verse template (template matching)
import cv2 
import numpy as np

THRESHOLD = 0.7
  
# Read the main image (source)
img_rgb = cv2.imread('./source_img/0006.jpg')
  
# Convert it to grayscale 
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 
  
# Read the template 
template = cv2.imread('./template_img/verse_template.jpg',0) 
  
# Store width and height of template in w and h 
w, h = template.shape[::-1] 
  
# Perform match operations. 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 
  
# Store the coordinates of matched area in a numpy array 
loc = np.where( res >= THRESHOLD)  
print(loc)

# Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]): 
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 17, 255), 2) 
  
# Show the final image with the matched area. 
cv2.imshow('Detected',img_rgb) 
cv2.waitKey()