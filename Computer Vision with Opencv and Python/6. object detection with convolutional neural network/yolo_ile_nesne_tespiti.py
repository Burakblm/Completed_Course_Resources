import cv2
import numpy as np
from yolo_model import YOLO
import matplotlib.pyplot as plt
import time


yolo = YOLO(0.6,0.5)

file = "data/coco_classes.txt"


with open(file) as f:
    class_name = f.readlines()

all_classes = [c.strip() for c in class_name]

# path = "images/dog_cat.jpg"

# image = cv2.imread(path)

# plt.figure()
# plt.imshow(image)
# plt.show()


cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,480)

pTime = 0

while True:
    ret , frame = cap.read()
    
    if ret:
        

        pimage = cv2.resize(frame,(416,416))
        pimage = np.array(pimage, dtype="float32")
        pimage /= 255.0
        pimage = np.expand_dims(pimage, axis=0)
        
        # yolo
        boxes, classes, scores = yolo.predict(pimage,frame.shape)
        
        print(boxes)
        print(classes)
        print(scores)
        
        
        cTime = time.time()
        fps = 1/ (cTime - pTime)
        pTime = cTime
        if classes != None:
            
            for box, score, cl in zip(boxes,scores,classes):
                x,y,w,h = box
                
                top = max(0,np.floor(x + 0.5).astype(int))
                left = max(0,np.floor(y + 0.5).astype(int))
                right = max(0,np.floor(x + w + 0.5).astype(int))
                bottom = max(0,np.floor(y + h + 0.5).astype(int))
                
                cv2.rectangle(frame,(top,left),(right, bottom),(255,0,0),2)
                cv2.putText(frame,"{} {}".format(all_classes[cl],score),(top,left-6),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),1,cv2.LINE_AA)
                cv2.putText(frame,"fps:"+str(fps),(40,40),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),1,cv2.LINE_AA)

        cv2.imshow("yolo",frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):break
        
        
cap.release()
cv2.destroyAllWindows()

