import cv2
import numpy as np
import matplotlib.pyplot as plt
# resim içe aktarma
img = cv2.imread("Lenna.png")
plt.imshow(img)
plt.axis("on")

width = 400
height = 500

pts1 = np.float32([[50,50],[60,430],[440,30],[455,154]])

pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])
# transform matrisi oluşturuyoruz
matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))
plt.imshow(imgOutput)
