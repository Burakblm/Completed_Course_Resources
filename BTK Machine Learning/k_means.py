# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:06:02 2021

@author: ASUS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv("musteriler.csv")

X = veriler.iloc[:,3:].values

x = veriler.iloc[:,3:4].values
y = veriler.iloc[:,4:].values


# K-Means 

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, init = "k-means++")
kmeans.fit(X)
kmeans_tahmin = kmeans.fit_predict(X)
merkezler = kmeans.cluster_centers_# kümelerin merkezlerinin konumunu verir
sonuclar = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=0)
    kmeans.fit(X)
    sonuclar.append(kmeans.inertia_)# verilerin küme sayılarına göre oluşturulan her
    # her gümenin örneklerinin merkezine olan uzaklıklarının toplamını sonuçlarını
    # sonuçlar dizisine atamaya yarar
print(sonuclar)
plt.plot(range(1,11),sonuclar)
plt.show()

kmeans = KMeans(n_clusters=4, init="k-means++", random_state=123)
Y_tahmin = kmeans.fit_predict(X)
print(Y_tahmin)

plt.scatter(X[Y_tahmin==0,0],X[Y_tahmin==0,1],s=30,c="red")
plt.scatter(X[Y_tahmin==1,0],X[Y_tahmin==1,1],s=30,c="blue")
plt.scatter(X[Y_tahmin==2,0],X[Y_tahmin==2,1],s=30,c="green")
plt.scatter(X[Y_tahmin==3,0],X[Y_tahmin==3,1],s=30,c="black")
plt.title("K-Means")
plt.show()




# Hierarchical clustering(hiyerarşik kümeleme)

from sklearn.cluster import AgglomerativeClustering
ac = AgglomerativeClustering(n_clusters=3, affinity="euclidean",linkage = "ward")
Y_tahmin = ac.fit_predict(X)
print(Y_tahmin)
plt.show()

plt.scatter(X[Y_tahmin==0,0],X[Y_tahmin==0,1],s=30,c="red")
plt.scatter(X[Y_tahmin==1,0],X[Y_tahmin==1,1],s=30,c="blue")
plt.scatter(X[Y_tahmin==2,0],X[Y_tahmin==2,1],s=30,c="green")
plt.title("Hierarchical clustering")
plt.show()



import scipy.cluster.hierarchy as sch
dendogram = sch.dendrogram(sch.linkage(X,method="ward"))
plt.show()










