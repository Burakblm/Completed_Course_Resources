import cv2
import matplotlib.pyplot as plt

# karıştırma
img1 = cv2.imread("Lenna.png")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)#opencv de renkler RGB değil BGR olarak aktarır
img2 = cv2.imread("kedifoto.jpg")# bunun için BGR renk skalasından RGB ya dönğştürdük
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)


plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

print(img1.shape)
print(img2.shape)
# fotoğrafları yeniden boyutlandırdık
img1 = cv2.resize(img1,(600,600))
print(img1.shape)

img2 = cv2.resize(img2,(600,600))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#karıştırma

blended = cv2.addWeighted(src1=img1,alpha=0.8,src2=img2,beta=0.6,gamma=0)
plt.figure()
plt.imshow(blended)
