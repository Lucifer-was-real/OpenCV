#Basic Image Manipulation
import matplotlib.pyplot as plt
import cv2
import numpy as np
image = cv2.imread("lenna.png")
new_image = image + 20
#new_image = 10 * image
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()