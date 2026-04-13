# Image as Numbers

import numpy as np
import cv2
import urllib.request

# Step 1: Fetch image from internet
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg"
resp = urllib.request.urlopen(url)
image_data = np.asarray(bytearray(resp.read()), dtype=np.uint8)

# Step 2: Decode image
img = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

# Step 3: Print shape
print("Image Shape (Height, Width, Channels):", img.shape)

# Step 4: Print pixel values (sample)
print("\nSample Pixel Values:")
print(img[0:5, 0:5])  # first 5x5 pixels

# Step 5: Explain channels
print("\nChannels Explanation:")
print("This image has", img.shape[2], "channels (BGR format in OpenCV)")