import cv2
import pickle
import numpy as np
from keras.models import model_from_json
import time

def preProcess(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255
    return img

cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,480)

model = model_from_json(open("model_trained_new_mnist.json","r").read())
model.load_weights("model_training_mnist.h5")

pTime = 0

while True:
    
    
    success,frame = cap.read()
    img = np.asarray(frame)# frameyi arraya çevirir
    img = cv2.resize(img,(28,28))
    img = preProcess(img)
    img = img.reshape(1,28,28,1)
    
    # predict
    predictions = model.predict(img)
    predict = np.argmax(predictions)
    print("accuracy: ",predictions[0][predict])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    if predictions[0][predict] > 0.5:
        cv2.putText(frame,"fps: {} prediction: ".format(str(int(fps)))+str(predict),(50,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0),1)

    
    cv2.imshow("Rakam sınıflandırma",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break
    