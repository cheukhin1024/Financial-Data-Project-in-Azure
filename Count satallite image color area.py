import cv2
import numpy as np

# load image
img = cv2.imread(r"C:\Users\Administrator\Downloads\ms image.PNG")

# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)

# create mask for green color in hsv
lower = (36, 25, 25)
upper = (70, 255,255)
mask = cv2.inRange(hsv, lower, upper)

# count non-zero pixels in mask
count=np.count_nonzero(mask)
print('count:', count)

# save output
cv2.imwrite('ms image_mask.PNG', mask)

# Display various images to see the steps
cv2.imshow('mask',mask)
cv2.waitKey(0)
