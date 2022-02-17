import cv2
import matplotlib.pyplot as plt
import numpy as np

# resimi içe aktarma
img = cv2.imread("Lenna.png")
# resmin göstrilmesi 
#cv2.imshow("orjinal",img)
plt.imshow(img)
plt.axis("off")
plt.show()

# yatay birleştirme (horizontal)
hor = np.hstack((img,img))
plt.imshow(hor)

# dikey birleştirme (vertical)
ver = np.vstack((img,img))
plt.imshow(ver)
