import matplotlib.pyplot as plt
# opencv kütüphanesini içe aktaralım
import cv2

# numpy kütüphanesini içe aktaralım
import numpy as np

# resmi siyah beyaz olarak içe aktaralım resmi çizdirelim
image = cv2.imread("Pedestrian.jpg",0)
plt.imshow(image,cmap="gray"),plt.title("1"),plt.axis("off"),plt.show()

# resim üzerinde bulunan kenarları tespit edelim ve görselleştirelim edge detection 
med_val = np.mean(image)
low = int(max(0,(1-0.33) * med_val))
high = int(min(255,(1+0.33) * med_val))
blurred_img = cv2.blur(image,ksize=(5,5))
edges = cv2.Canny(image = blurred_img,threshold1=low,threshold2=high)
plt.figure(),plt.imshow(edges,cmap="gray"),plt.title("2"),plt.axis("off"),plt.show()

# yüz tespiti için gerekli haar cascade'i içe aktaralım
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# yüz tespiti yapıp sonuçları görselleştirelim
face_rect = face_cascade.detectMultiScale(image,minNeighbors = 5)
for (x,y,w,h) in face_rect:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),3)
plt.figure(),plt.imshow(image,cmap="gray"),plt.title("3"),plt.axis("off")

# HOG ilklendirelim insan tespiti algoritmamızı çağıralım ve svm'i set edelim
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


# resme insan tespiti algoritmamızı uygulayalım ve görselleştirelim
(rects,weights)= hog.detectMultiScale(image,padding=(8,8),scale = 1.05)
    
for (x,y,w,h) in rects:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    plt.imshow(image)

