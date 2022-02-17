import cv2
import matplotlib.pyplot as plt

# import image
img = cv2.imread("image_name.png",0)
plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off"),plt.title("original image"),plt.show()

# x gradient
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S, dx=1,dy=0 ,ksize=5)
plt.figure(),plt.imshow(sobelx,cmap="gray"),plt.axis("off"),plt.title("Sobel x"),plt.show()

# y gradient 
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S, dx=0,dy=1 ,ksize=5)
plt.figure(),plt.imshow(sobely,cmap="gray"),plt.axis("off"),plt.title("Sobel y"),plt.show()

# Laplacian gradient
laplacian = cv2.Laplacian(img,ddepth=cv2.CV_16S)
plt.figure(),plt.imshow(laplacian,cmap="gray"),plt.axis("off"),plt.title("laplacian1"),plt.show()

# Laplacian gradient
laplacian = cv2.Laplacian(img,ddepth=cv2.CV_16U)
plt.figure(),plt.imshow(laplacian,cmap="gray"),plt.axis("off"),plt.title("laplacian2"),plt.show()
