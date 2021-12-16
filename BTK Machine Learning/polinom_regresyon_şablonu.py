# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:49:12 2021

@author: ASUS
"""
# veri yükleme
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('maaslar.csv')

# data frame dilimleme(slice)
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]

# numpy dizi(array) dönüşümü
X = x.values
Y = y.values

# linear regression
# doğrusal model oluşturma
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)



# polynomial regression
# doğrusal olmayan (nonlinear model) oluşturma
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=3)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,Y)

# görseleştirme
plt.scatter(X,Y,color="red")
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color="blue")
plt.show()

plt.scatter(X,Y , color= "red")
plt.plot(X,lin_reg.predict(X), color="blue")
plt.show()

# tahmin (predict)
print(lin_reg2.predict(poly_reg.fit_transform([[10]])))
















