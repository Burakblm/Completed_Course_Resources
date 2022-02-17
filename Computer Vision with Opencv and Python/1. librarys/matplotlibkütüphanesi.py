import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([4,5,5,6,7.3,8.9,12.2,13,24])

plt.figure()
# color cizimin renginini belirler
# alpha parametresi saydamlığı ayarlar
# label parametresi çizilen şekile başlık veremeyi sağlar
plt.plot(x,y,color="red",alpha=0.99,label="line")
plt.scatter(x,y,color="blue",alpha=0.5,label="scatter")
plt.title("matplotlib")# görüntüye başlık eklemeye yarar
plt.xlabel("X") # grafiğin x eksenini isimlendirmeye yarar
plt.ylabel("Y") # grafiğin y eksenini isimlendirmeye yarar
plt.grid() # çizilen grafiğe ızgaralar eklemeyi sağlar
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12]) # grafiğimizn eksen aralıklarını el ile boyutlandırmayı sağlar
plt.legend()
plt.show()

fig,axes = plt.subplots(2,1,figsize=(9,7))
fig.subplots_adjust(hspace=0.5)

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]
axes[0].scatter(x,y)
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")

axes[1].scatter(y,x)
axes[1].set_title("sub-2")
axes[1].set_ylabel("sub-2 y")
axes[1].set_xlabel("sub-2 x")



# random resim
plt.figure() # içerisini dolduracağımız figürü oluşturuyoruz
img = np.random.random((50,50))
plt.imshow(img,cmap="gray") # 0(siyah) - 1(beyaz) -> 0.5(gri)
plt.axis("on") # şekilin kenralarındai sayıların gösterilmesinin sağlar(off) olursa sayılar gösterilmez
plt.show()

