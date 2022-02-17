import numpy as np

# 1*15 boyutunda bir array-dizi
dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)
print("dizi boyutu =",dizi.shape) # arrayin boyutu

dizi2 = dizi.reshape(3,5)

print("şekil: ",dizi2.shape)
print("boyut : ",dizi2.ndim)
print("veri tipi :",dizi2.dtype)
print("boy : ",dizi2.size)


# array type
print("type :",type(dizi2))

# 2 boytulu array
dizi2D = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [8,7,6,5]])
print(dizi2D)

# sıfırlardan oluşan bir array-dizi
sifir_dizi = np.zeros((3,4),dtype="float")
print(sifir_dizi)

# birlerden oluşan array-dizi
bir_dizi = np.ones((3,4))
print(bir_dizi)

# bos array
bos_dizi = np.empty((3,4))
print(bos_dizi)

# arange(X,Y,basamak)
dizi_aralik = np.arange(20,50,5)
print(dizi_aralik)

# linspace(X,Y,basamak)
dizi_bosluk = np.linspace(10,20,5)
print(dizi_bosluk)
print(dizi_bosluk.shape)

# float array
float_array = np.float32([[1,2],[3,4]])
print(float_array)
print(float_array.dtype)

# matematiksel işlemeler
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

# dizi elemanı toplama
print(np.sum(a))

# max değer
print(np.max(a))

# min değer
print(np.min(a))

# mean ortalama 
print(np.mean(a))

# median ortalama
print(np.median(a))

# rastgele sayi üretme [0,1] arasında sürekli uniform 3*3
rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

# indeks
dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])

# dizinin ilk 4 elemanı
print(dizi[0:4])

# dizinin tersi
print(dizi[::-1])

#
dizi2D= np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

# dizinin 1.satır ve 1.sutununda bulunan elemanı
print(dizi2D[1,1])

# 1. sütun ve tüm satırlar
print(dizi2D[:,1])

# 1. satır ve 1,2,3 
print(dizi2D[1,1:4])

# dizinin son satır tüm sütunlar
print(dizi2D[-1,:])

#
dizi2D = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(dizi2D)

# vektör haline getirme
vektor = dizi2D.ravel()
print(vektor)

# maksimum sayını nindeksi
maksimum_sayi_index = vektor.argmax()
print(maksimum_sayi_index)

# diziyi vektöre çevirmenin diğer bi yolu
print(dizi2D.reshape(9))
