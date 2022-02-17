import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread("image_name.png",0)
img = np.float32(img)

print(img.shape)
plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off")

# haris corner detection
dst = cv2.cornerHarris(img,blockSize=2,ksize=3,k=0.004)
plt.figure(),plt.imshow(dst,cmap="gray"),plt.axis("off")

#cv2.imwrite("foto.png",dst)

dst = cv2.dilate(dst,None)
img[dst>0.2*dst.max()] = 1
plt.figure(),plt.imshow(dst,cmap="gray"),plt.axis("off")

# shi tomasi detection
img = cv2.imread("image_name.png",0)
img = cv2.resize(img,(400,400))
img = np.float32(img)

corners = cv2.goodFeaturesToTrack(img,120,0.01,10)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),5,(125,255,125),cv2.FILLED)
    
plt.imshow(img)
plt.axis("off")
