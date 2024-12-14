import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("3x3 logo.png")

# Convert the image to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap="gray")
plt.title("Gray Image")
plt.show()

# Crop a region from the image
cropping = image[100:300, 200:400]
cropping_rgb = cv2.cvtColor(cropping, cv2.COLOR_BGR2RGB)
plt.imshow(cropping_rgb)
plt.title("Cropped Region")
plt.show()

# Rotate the image by 45 degrees
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotate = cv2.warpAffine(image, M, (w, h))
rotate_rgb = cv2.cvtColor(rotate, cv2.COLOR_BGR2RGB)
plt.imshow(rotate_rgb)
plt.title("Rotated Image")
plt.show()

# Increase the brightness of the image
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
bright = cv2.add(image, brightness_matrix)
bright_rgb = cv2.cvtColor(bright, cv2.COLOR_BGR2RGB)
plt.imshow(bright_rgb)
plt.title("Brightened Image")
plt.show()
