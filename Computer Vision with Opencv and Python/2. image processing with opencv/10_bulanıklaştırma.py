import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")# uyarıları engellemek için

# buluring(detayı azaltır ve gürültüyü engeller)
img = cv2.imread("Lenna.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)# resimi standart rgb formatına getiriyoruz

plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("Original"),plt.show()

'''
ortalama bulanıklaştırma yöntemi
'''

dst2 = cv2.blur(img,ksize=(10,10))
plt.figure(),plt.imshow(dst2),plt.axis("off"),plt.title("ortalama blur"),plt.show()

'''
gaussian blur
'''

gb = cv2.GaussianBlur(img,ksize=(11,11),sigmaX =7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("gaussian blur"),plt.show()

'''
medya blur
'''

mb = cv2.medianBlur(img,ksize=5,)
plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("median blur"),plt.show()


def gaussianNoise(image):
    row,col,ch = image.shape
    mean =0
    var = 0.05
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image+gauss
    return noisy

# içe aktar normalize et
img = cv2.imread("Lenna.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255# resimi normalize ediyoruz
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("Original"),plt.show()

gaussianNoisyImage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("gaussian noisy"),plt.show()

gb2 = cv2.GaussianBlur(gaussianNoisyImage,ksize=(3,3),sigmaX =7)
plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("with gaussian blur"),plt.show()


def saltPapperNoise(image):
    row, col ,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy  = np.copy(image)
    
    # salt beyaz
    num_salt = np.ceil(amount * image.size *s_vs_p)
    coords = [np.random.randint(0,i-1,int(num_salt)) for i in image.shape]
    noisy[coords]=1
    
    # papper siyah
    num_papper = np.ceil(amount * image.size *(1 - s_vs_p))
    coords = [np.random.randint(0,i-1,int(num_papper)) for i in image.shape]
    noisy[coords]=0
    
    return noisy

spImage = saltPapperNoise(img)
plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title("SP Image"),plt.show()


mb2 = cv2.medianBlur(spImage.astype(np.float32),ksize=3,)# apImage dizisini float32 formatına çevirdik
plt.figure(),plt.imshow(mb2),plt.axis("off"),plt.title("sp Image median blur"),plt.show()

trial1 = spImage[:50,:50]
plt.imshow(trial1)
plt.show()
trial2 = mb2[:50,:50]
plt.imshow(trial2)
