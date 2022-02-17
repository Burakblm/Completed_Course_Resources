import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread("image_name.jpg",0)
plt.figure(),plt.imshow(img,cmap="gray"),plt.title("1"),plt.axis("off"),plt.show()

edges = cv2.Canny(image = img,threshold1=0,threshold2=255)
plt.figure(),plt.imshow(edges,cmap="gray"),plt.title("2"),plt.axis("off"),plt.show()

# median değeri
med_val = np.median(img)
print(med_val)

med_val = np.mean(img)
print(med_val)

low = int(max(0,(1-0.33) * med_val))
high = int(min(255,(1+0.33) * med_val))
print(low)
print(high)

edges = cv2.Canny(image = img,threshold1=low,threshold2=high)
plt.figure(),plt.imshow(edges,cmap="gray"),plt.title("3"),plt.axis("off"),plt.show()

# blur
blurred_img = cv2.blur(img,ksize=(5,5))
plt.figure(),plt.imshow(blurred_img,cmap="gray"),plt.title("4"),plt.axis("off")

med_val = np.median(blurred_img)
print(med_val)

low = int(max(0,(1-0.33) * med_val))
high = int(min(255,(1+0.33) * med_val))
print(low)
print(high)

edges = cv2.Canny(image = blurred_img,threshold1=low,threshold2=high)
plt.figure(),plt.imshow(edges,cmap="gray"),plt.title("5"),plt.axis("off"),plt.show()

#cv2.imwrite("yenifoto.jpg",edges)
