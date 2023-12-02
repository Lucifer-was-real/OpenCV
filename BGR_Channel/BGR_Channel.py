import cv2
import matplotlib.pyplot as plt
baboon=cv2.imread('baboon.png')
blue, green, red = baboon[:, :, 0], baboon[:, :, 1], baboon[:, :, 2]
im_bgr = cv2.vconcat([blue, green, red])
plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(cv2.cvtColor(baboon, cv2.COLOR_BGR2RGB))
plt.title("RGB image")
plt.subplot(122)
plt.imshow(im_bgr,cmap='gray')
plt.title("Different color channels  blue (top), green (middle), red (bottom)  ")
plt.show()