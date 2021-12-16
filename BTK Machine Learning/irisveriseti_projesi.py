# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:01:45 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import metrics

#2.veri onisleme

#2.1.veri yukleme
veriler = pd.read_excel("Iris.xls")

x = veriler.iloc[:,0:4].values # bağımsız değişkenler
y = veriler.iloc[:,4:].values  # bağımlı değişken

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.40, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)


# Logistic Regression (lojistik regresyon)
from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train)
y_pred_lr = logr.predict(X_test)
cm = confusion_matrix(y_pred_lr,y_test)
print(cm)
y_proba = logr.predict_proba(X_test)
fpr , tpr , thold = metrics.roc_curve(y_test,y_proba[:,0],pos_label="Iris-setosa")
print("false positif rate = ",fpr)
print("ture positif rate = ",tpr)
print(thold)





















