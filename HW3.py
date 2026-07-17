import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('minion.jpg')

B = img[:,:,0]
G = img[:,:,1]
R = img[:,:,2]

gray_simple = ((R + G + B) / 3).astype(np.uint8)
gray_weighted = (0.299 * R + 0.587 * G + 0.114 * B).astype(np.uint8)

# Histogram
hist_simple = cv2.calcHist([gray_simple], [0], None, [256], [0, 256])
hist_weighted = cv2.calcHist([gray_weighted], [0], None, [256], [0, 256])
x = np.arange(256)

plt.figure(figsize=(20, 15   ))

plt.subplot(221)
plt.imshow(gray_simple, cmap="gray")
plt.title("Simple Average Image")
plt.axis("off")

plt.subplot(222)
plt.imshow(gray_weighted, cmap="gray")
plt.title("Weighted Average Image")
plt.axis("off")

plt.subplot(223)
plt.bar(x, hist_simple, width=1.0, color='blue')
plt.title("Histogram - Simple Average")
plt.xlim([0, 256])

plt.subplot(224)
plt.bar(x, hist_weighted, width=1.0, color='blue') 
plt.title("Histogram - Weighted Average")
plt.xlim([0, 256])

plt.tight_layout()
plt.show()  