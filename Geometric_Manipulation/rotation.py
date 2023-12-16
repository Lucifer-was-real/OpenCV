#Basic Image Manipulation
#Rotation
import matplotlib.pyplot as plt
import cv2
import numpy as np
image = cv2.imread("lenna.png")
theta = 45.0
cols, rows, _ = image.shape
M = cv2.getRotationMatrix2D(center=(cols // 2 - 1, rows // 2 - 1), angle=theta, scale=1)
new_image = cv2.warpAffine(image, M, (cols, rows))
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()