# Image Filter Lab using OpenCV

import cv2
import numpy as np
import urllib.request

# Step 1: Fetch image from internet
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg"
resp = urllib.request.urlopen(url)
image_data = np.asarray(bytearray(resp.read()), dtype=np.uint8)

# Step 2: Decode image
img = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

# Step 3: Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 4: Apply blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 5: Edge detection
edges = cv2.Canny(blur, 100, 200)

# Step 6: Show images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()