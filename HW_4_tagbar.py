import cv2 as cv
import numpy as np

img = cv.imread('minion.jpg', 0)

img_negative = (256 - 1) - img
c_log = 255 / np.log(1 + 1.0 * np.max(img))
img_log = c_log * (np.log(1 + img))
img_log = np.array(img_log, dtype=np.uint8)

def onChange(x):
    if x == 0: 
        x = 1

    _, thresh = cv.threshold(img, x, 255, cv.THRESH_BINARY)
    
    ch2 = img_negative.copy()
    
    ch3 = img_log.copy()
    
    gamma = x / 100.0 
    r_power = img_log / 255.0
    s = 255 * (r_power ** gamma)
    ch4 = np.array(s, dtype=np.uint8)
    
    cv.putText(thresh, f"Binary (Threshold: {x})", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, 255, 2)
    cv.putText(ch2, "Negative", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, 0, 2)
    cv.putText(ch3, "Log Transformed", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, 255, 2)
    cv.putText(ch4, f"Power-law (Gamma: {gamma:.2f})", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, 255, 2)
    
    row1 = np.hstack((thresh, ch2))
    row2 = np.hstack((ch3, ch4))
    grid_all = np.vstack((row1, row2))
    
    cv.imshow('Image Transformations with Trackbar', grid_all)

cv.namedWindow('Image Transformations with Trackbar')
cv.createTrackbar('Value (X)', 'Image Transformations with Trackbar', 20, 255, onChange)

onChange(20)

cv.waitKey(0)
cv.destroyAllWindows()