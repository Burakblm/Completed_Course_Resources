import cv2
import time

#capture 
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)

# video kaydet
# VideoWriter_fourcc = çerçeveleri sıkıştırmak için kullanılır
# 20 parametresi ise framepersecon değeri dir
writer = cv2.VideoWriter("video_kaydı.mp4",cv2.VideoWriter_fourcc(*"DIVX"),30,(width,height))

while True:
    ret,frame = cap.read()
    cv2.imshow("video",frame)
    
    # save( kayıt)
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
