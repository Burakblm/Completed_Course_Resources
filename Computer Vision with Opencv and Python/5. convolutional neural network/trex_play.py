from keras.models import model_from_json
import numpy as np
from PIL import Image
import keyboard
import time
from mss import mss

mon = {"top":388,
       "left":485,
       "width":175,
       "height":93}
sct = mss()

width = 125
height= 50

# model yükeme
model = model_from_json(open("model_new.json","r").read())
model.load_weights("trex_wight_new.h5")

# right = 0, up = 1
labels = ["Right","Up"]

framerate_time = time.time()
counter = 0
i = 0
delay = 0.4
key_down_pressed = False
while True:
    
    img = sct.grab(mon)
    im = Image.frombytes("RGB",img.size,img.rgb)
    im2 = np.array(im.convert("L").resize((width,height)))
    im2 = im2 / 255
    
    X = np.array([im2])
    X = X.reshape(X.shape[0],width,height,1)
    r = model.predict(X)
    
    result = np.argmax(r)
    
    if result == 1:
        keyboard.press(keyboard.KEY_UP)
        time.sleep(0.2)
        print("Right: {}\n Up: {}".format(r[0][0],r[0][1]))
        print("_"*30)
    else:
        print("Right: {}\n Up: {}".format(r[0][0],r[0][1]))
        print("_"*30)
    