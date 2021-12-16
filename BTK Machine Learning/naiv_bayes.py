# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:50:13 2020

@author: sadievrenseker
"""

#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('veriler.csv')


x = veriler.iloc[:,1:4].values
y = veriler.iloc[:,4:].values

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)

y_pred_lr = logr.predict(X_test)
print(y_pred_lr)
print(y_test)

print("LR")
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_pred_lr,y_test)
print(cm)

print("KNN")
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5,metric="minkowski")
knn.fit(X_train,y_train)
y_pred_knn = knn.predict(X_test)

cm2= confusion_matrix(y_test,y_pred_knn)
print(cm2)

print("SVC")
from sklearn.svm import SVC
svc = SVC(kernel="rbf")
svc.fit(X_train,y_train)

y_pred_svc = svc.predict(X_test)
cm3 = confusion_matrix(y_pred_svc,y_test)
print(cm3)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train,y_train)

y_pred = gnb.predict(X_test)
cm3 = confusion_matrix(y_test,y_pred)
print("GNB")
print(cm)


    




