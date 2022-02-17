import cv2
import matplotlib.pyplot as plt

# içe aktar
einstein = cv2.imread("einstein.jpg",0)
plt.figure(),plt.imshow(einstein,cmap="gray"),plt.axis("off")

# sınıflandırıcı
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#face_cascade = cv2.CascadeClassifier("cascade.xml")
face_rect = face_cascade.detectMultiScale(einstein)

for (x,y,w,h) in face_rect:
    cv2.rectangle(einstein,(x,y),(x+w,y+h),(255,255,255),2)
plt.figure(),plt.imshow(einstein,cmap="gray"),plt.axis("off")


# barcelona

# içe aktar
barcelona = cv2.imread("barcelona.jpg",0)
plt.figure(),plt.imshow(barcelona,cmap="gray"),plt.axis("off")

face_rect = face_cascade.detectMultiScale(barcelona,minNeighbors = 5)

for (x,y,w,h) in face_rect:
    cv2.rectangle(barcelona,(x,y),(x+w,y+h),(255,255,255),2)
plt.figure(),plt.imshow(barcelona,cmap="gray"),plt.axis("off")




# video

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read() # ret değişkeninde görüntünün alınıp alınmadığı kontrol edilir
    
    if ret: # eğer görüntü alınmışsa kodları çalıştırır
        
        face_rect = face_cascade.detectMultiScale(frame,minNeighbors = 20)
        
        for (x,y,w,h) in face_rect:
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
        
        cv2.imshow("face detect",frame)
        
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break # q ya basıldığında söngüyü kırar
    
cap.release()
cv2.destroyAllWindows() # açık olan tüm pencelereleri kapatır
