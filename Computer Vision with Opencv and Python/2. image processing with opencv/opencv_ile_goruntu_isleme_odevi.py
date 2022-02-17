# opencv kütüphanesini içeri aktaralım
import cv2

#matplotlib kütüphanesini içeri aktaralım
import matplotlib.pyplot as plt

# resmi siyah beyaz olarak içe aktaralım
img = cv2.imread("animals.jpg",0)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# resmi çizdirelim
plt.figure(),plt.imshow(img),plt.show()

# resmin boyutuna bakalım
print(img.shape)

# resmi 4/5 oranında yeniden boyutlandıralım ve resmi çizdirelim
yukseklik = int((img.shape[0]/5)*4)
genislik = int((img.shape[1]/5)*4)
img = cv2.resize(img,(genislik,yukseklik))
plt.figure(),plt.imshow(img)

#orjinal resme bir yazı ekleyelim mesela "kopek" ve resmi çizdirelim
cv2.putText(img,"Kopek",(600,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,150,255))
plt.imshow(img)
plt.show()

# orjinal resmin 50 threshold değeri üzerindekileri beyaz yap altındakileri siyah yapalım
# binray threshold yöntemini kullanalım ve resmi çizdirelim
_,thresh_img = cv2.threshold(img,thresh=50,maxval=255,type=cv2.THRESH_BINARY)
plt.figure(),plt.imshow(thresh_img),plt.show()

# orjinal resme gaussian bulanıklaştırma uygulayalım ve resmi çizdirelim
gb = cv2.GaussianBlur(img,(11,11),sigmaX=7)
plt.figure(),plt.imshow(gb),plt.show()


# orjinal resme laplacian gradyan uygulanalım ve resmi çizdirelim
laplacian = cv2.Laplacian(img,ddepth=cv2.CV_16S)
plt.figure(),plt.imshow(laplacian),plt.show()


#orjinal resmi histogramını çizdirelim
hist_img = cv2.calcHist([img],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.figure(),plt.plot(hist_img),plt.show()
