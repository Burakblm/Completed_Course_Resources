import cv2
import matplotlib.pyplot as plt

# içe aktarma
img = cv2.imread("kedifoto.jpg",0)


# görselleştir
cv2.imshow("ilk resim",img)
k = cv2.waitKey(0) &0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("kedi_gray.jpg",img)
    cv2.destroyAllWindows()

