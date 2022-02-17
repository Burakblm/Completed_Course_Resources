import cv2

objectName = "face"

frameWidth = 280
frameHeight = 360

color = (255,0,0)

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cap.set(3,frameWidth)# alınacak görüntünün boyutu
cap.set(4,frameHeight)

# track bar
cv2.namedWindow("Sonuc")
cv2.resizeWindow("Sonuc",frameWidth,frameHeight + 100)

cv2.createTrackbar("Scale","Sonuc",400,1000,nothing)
cv2.createTrackbar("Neighbor","Sonuc",4,50,nothing)

# cascade classifier
cascade = cv2.CascadeClassifier("cascade.xml")

while True:
    
    # read images
    success, img = cap.read()
    
    if success:
        # convert BGR to GRAY
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # detection parameters
        scaleVal = 1 + (cv2.getTrackbarPos("Scale","Sonuc")/1000)
        neighbor = cv2.getTrackbarPos("Neighbor","Sonuc")
        # detection
        rects = cascade.detectMultiScale(gray,scaleVal,neighbor)
        
        for (x,y,w,h) in rects:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            
        cv2.imshow("Sonuc",img)
        
    if cv2.waitKey(1) & 0xFF == ord("q"): break
