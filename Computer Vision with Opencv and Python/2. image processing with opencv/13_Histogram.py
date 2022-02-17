import cv2
import matplotlib.pyplot as plt
import numpy as np

# import image
img = cv2.imread("image_name.png")
img_vis = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img_vis),plt.axis("off"),plt.title("orginal"),plt.show()

print(img.shape)

img_hist = cv2.calcHist([img],channels=[0],mask=None,histSize= [256],ranges=[0,256])
print(img_hist.shape)
plt.figure(), plt.plot(img_hist)

color = ("b","g","r")
plt.figure()
for i,c in enumerate(color):
    hist = img_hist = cv2.calcHist([img],channels=[i],mask=None,histSize= [256],ranges=[0,256])
    plt.plot(hist,color=c)


#cat image
cat_img = cv2.imread("image_name.jpg")
cat_img_vis = cv2.cvtColor(cat_img, cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(cat_img_vis),plt.show()

print(cat_img.shape)

mask = np.zeros(cat_img.shape[:2],np.uint8)
plt.figure(),plt.imshow(mask,cmap="gray"),plt.show()

mask[100:150,120:150] = 255
plt.figure(),plt.imshow(mask,cmap="gray"),plt.show()

mask_cat_img = cv2.bitwise_and(cat_img_vis,cat_img_vis,mask= mask)
plt.figure(),plt.imshow(mask_cat_img,cmap="gray"),plt.show()


mask_cat_img = cv2.bitwise_and(cat_img,cat_img,mask= mask)
masked_cat_img = cv2.calcHist([mask_cat_img],channels=[0],mask=mask,histSize= [256],ranges=[0,256])
plt.figure(),plt.plot(masked_cat_img),plt.show()

# histogram eşitleme
# kontrast artırma
img = cv2.imread("Lenna.png",0)
plt.figure(),plt.imshow(img,cmap="gray"),plt.show()

img_hist = cv2.calcHist([img],channels=[0],mask=None,histSize= [256],ranges=[0,256])
plt.figure(),plt.plot(img_hist),plt.show()

eq_hist = cv2.equalizeHist(img)
plt.figure(),plt.imshow(eq_hist,cmap="gray")

eq_img_hist = cv2.calcHist([eq_hist],channels=[0],mask=None,histSize= [256],ranges=[0,256])
plt.figure(),plt.plot(img_hist),plt.show()
