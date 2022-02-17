import cv2
import numpy as np
import matplotlib.pyplot as plt

# resim oluşturmak
img = np.zeros((512,512,3),np.uint8)
print(img.shape)

plt.imshow(img)
plt.show()
# çizgi 
# (resim,baslangıc noktası,bitis noktası,renk,kalınlık)
cv2.line(img,(100,100),(100,400),(0,255,0),3)# color BGR=(0,255,0)
plt.imshow(img)
plt.show()

# dikdörtgen
# (resim, baslangıc , bitis, renk)
cv2.rectangle(img,(0,0),(300,300),(255,0,0),cv2.FILLED)# cv2.fılled dikdörtgenin içini dolfurmaya yarar
plt.imshow(img)
plt.show()

# cember
#(resim,merkez,yarıçap,renk)
cv2.circle(img,(420,420),50,(0,0,255))
plt.imshow(img)
plt.show()

# metin
# (resim,baslangıc noktası,font,kalınlıgı,renk)
cv2.putText(img,"Resim",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
plt.imshow(img)
