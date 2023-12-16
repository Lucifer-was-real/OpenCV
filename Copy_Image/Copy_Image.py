#Basic Image Manipulation
import matplotlib.pyplot as plt
import cv2
import numpy as np
baboon = cv2.imread("baboon.png")
A = baboon
id(A)==id(baboon)
id(A)
plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(cv2.cvtColor(baboon, cv2.COLOR_BGR2RGB))
plt.title("baboon")
plt.subplot(122)
plt.imshow(cv2.cvtColor(A, cv2.COLOR_BGR2RGB))
plt.title("array A")
plt.show()
