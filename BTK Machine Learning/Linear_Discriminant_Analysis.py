# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:07:28 2021

@author: ASUS
"""

# BOYUT İNDİRGEME

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('Wine.csv')


x = veriler.iloc[:,0:13].values
y = veriler.iloc[:,13].values

# eğitim ve test kümelerinin bölünmesi
from sklearn.model_selection import train_test_split
X_train, X_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=0)
# ölçekleme
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_train2 = pca.fit_transform(X_train)
X_test2 = pca.transform(X_test)

# PCA dönüşümünden önce gelen LR
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)

# PCA dönüşümünden sonra gelen LR
classifier2 = LogisticRegression(random_state=0)
classifier2.fit(X_train2,y_train)

y_pred1 = classifier.predict(X_test)
y_pred2 = classifier2.predict(X_test2)

from sklearn.metrics import confusion_matrix
print("gercek / PCA'siz")
cm = confusion_matrix(y_test,y_pred1)
print(cm)

print("gercek / PCA ile")
cm2 = confusion_matrix(y_test,y_pred2)
print(cm2)

print("pcasiz ve pcali ")
cm2 = confusion_matrix(y_pred1,y_pred2)
print(cm2)




from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components=2)
X_train_lda = lda.fit_transform(X_train,y_train)
X_test_lda = lda.transform(X_test)
# LDA dönüşümünden sonra

classifier_lda = LogisticRegression(random_state=0)
classifier_lda.fit(X_train_lda,y_train)

# LDA verisini tahmin et
y_pred_lda = classifier_lda.predict(X_test_lda)

print("gercek / LDA li")
cm4 = confusion_matrix(y_pred1,y_pred_lda)
print(cm4)








