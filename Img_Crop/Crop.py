import cv2
import matplotlib.pyplot as plt
img = cv2.imread("cat.jpg")
crop_image=img[150:150 ,100:300]
#cv2.imshow(crop_image)
plt.figure(figsize=(10,10))
plt.imshow(crop_image)
plt.show()