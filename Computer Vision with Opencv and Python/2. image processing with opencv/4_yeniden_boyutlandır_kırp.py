import cv2
import matplotlib.pyplot as plt

# resimi yüklemek
img = cv2.imread("Lenna.png",1)
print("Resim boytu: ",img.shape)

#cv2.imshow("orijinal",img)
# cv2.imshow() çalışırken hata verdiği için matplotlib kullanıyorum
plt.figure()
plt.imshow(img)
# plt.gray()
plt.axis("off")
plt.show()


#yeniden boyutlandırma için cv2.resize kullanılır
imgResized = cv2.resize(img,(50,50))
print("Resized Img boyutu: ",imgResized.shape)
plt.imshow(imgResized)
#cv2.imshow("yeni resim",imgResized) # yine hata verdi
plt.axis("off")

# kırpma
imgCropped = img[:200,:300] # height, width
#cv2.imshow(imgCropped)
plt.imshow(imgCropped)
