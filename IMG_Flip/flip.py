import cv2
import matplotlib.pyplot as plt
img = cv2.imread("barbara.png")
im_flip = cv2.flip(img,0)
#im_rotate = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
plt.figure(figsize=(10,10))
plt.imshow(im_flip)
#plt.imshow(im_rotate)
plt.show()
