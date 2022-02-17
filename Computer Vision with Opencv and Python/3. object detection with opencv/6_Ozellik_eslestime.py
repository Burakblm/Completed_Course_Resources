import cv2
import matplotlib.pyplot as plt

# ana görüntüyü içe aktar
chos = cv2.imread("cikolatalar.jpg",0)
plt.figure(),plt.imshow(chos,cmap= "gray"),plt.axis("off"),plt.show()

# aranacak olan görüntü
cho = cv2.imread("caremio.jpg",0)
plt.figure(),plt.imshow(cho,cmap= "gray"),plt.axis("off"),plt.show()

# orb tanımlayıcı 
# köşe kenar gibi nesneye ait özellikler
orb = cv2.ORB_create()

# anahtar nokta tespiti
kp1 ,des1 = orb.detectAndCompute(cho,None)
kp2 ,des2 = orb.detectAndCompute(cho,None)

# bf matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

# noktaları eşleştir
matches = bf.match(des1,des2)

# mesafeye göre sırala
matches = sorted(matches,key = lambda x : x.distance)

# eşleşen resimleri görselleştirelim
plt.figure()
img_match = cv2.drawMatches(cho,kp1,chos,kp2,matches[:20],None,flags = 2)
plt.imshow(img_match),plt.axis("off")

# sift
sift = cv2.xfeatures2d.SIFT_create()

# bf
bf = cv2.BFMatcher()

# anahtar tespiti sift ile
kp1 , des1 = sift.detectAndConpute(cho,None)
kp2 , des2 = sift.detectAndConpute(chos,None)

matches = bf.knnMatch(des1,des2,k = 2)

gusel_eslesme = []

for match1, match2 in matches:
    if match1.distance < 0.75*match2.distance:
        gusel_eslesme.append([match1])

plt.figure()
sift_matches = cv2.drawMatchesKnn(cho,kp1,chos,kp2,gusel_eslesme,None,flags=2)
plt.imshow(sift_matches),plt.axis("off")

