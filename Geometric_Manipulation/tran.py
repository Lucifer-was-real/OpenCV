#Basic Image Manipulation
#Translation
import matplotlib.pyplot as plt
import cv2
import numpy as np
image = cv2.imread("lenna.png")
tx = 100
ty = 0
M = np.float32([[1, 0, tx], [0, 1, ty]])
M
rows, cols, _ = image.shape
#new_image = cv2.warpAffine(image, M, (cols, rows))
new_image = cv2.warpAffine(image, M, (cols + tx, rows + ty))
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()
