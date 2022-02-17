import cv2
import time

video_name = "video_kaydı.mp4"

cap = cv2.VideoCapture(video_name)

print("genişlik:",cap.get(3))
print("yükseklik:",cap.get(4))

if cap.isOpened() == False:
    print("hata video açılmadı")
    
 # videoyu okuyoruz eğer bir frame döndğürülüyorsa ret = true olur

while True:
    ret,frame = cap.read() # videodaki her fotoğrafı almamızı sağlıyor
    if ret == True:
        time.sleep(0.01)# bunu kullanmazsak çok hızlı akar
        cv2.imshow("Video",frame)
        
    else:
        break# eğer fotoğraflar bitiyse ret= false dönecek ve while döngüsü kırılacak
        
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release() # stop capture
cv2.destroyAllWindows()
