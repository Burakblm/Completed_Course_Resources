import cv2
import matplotlib.pyplot as plt

def image_pyramid(image,scale =1.5,minSize=(22)):
    
    yield image
    
    while True:
        
        w = int(image.shape[1]/scale)
        image = cv2.resize(image,dsize=(w,w))
        
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break
        
        yield image

# img = cv2.imread("cat.jpg")
# im = image_pyramid(img,minSize=(10,10))
# for i,image in enumerate(im):
#     print(i)
#     if i == 9:
#         plt.imshow(image)