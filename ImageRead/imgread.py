import cv2
import matplotlib.pyplot as plt
img = cv2.imread('lenna.png')
new_image=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,10))
plt.imshow(new_image)
plt.show()
image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(10, 10))
plt.imshow(image_gray, cmap='gray')
plt.show()
cv2.imwrite('lena_gray_cv.jpg', image_gray)