# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 00:58:29 2021

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

# # görseleştirme
# plt.scatter(X,Y,color="red")
# plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color="blue")
# plt.show()

# plt.scatter(X,Y , color= "red")
# plt.plot(X,lin_reg.predict(X), color="blue")
# plt.show()

# tahmin (predict)

# print("polinomal regresyon = ",lin_reg2.predict(poly_reg.fit_transform([[10]])))



from sklearn.preprocessing import StandardScaler
sc1  = StandardScaler()
x_olcekli = sc1.fit_transform(X)
    
sc2  = StandardScaler()
y_olcekli = sc1.fit_transform(Y)
    
from sklearn.svm import SVR
    
svr_reg = SVR(kernel="rbf")
svr_reg.fit(x_olcekli,y_olcekli)
    
# plt.scatter(x_olcekli,y_olcekli,color="red")
# plt.plot(x_olcekli,svr_reg.predict(x_olcekli),color="blue")
# plt.show()
print("support vector regression = ", svr_reg.predict([[12]]))


from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)
# plt.scatter(X, Y,color="red")
# plt.plot(X,r_dt.predict(X),color="blue")
print("Decision tree = ",r_dt.predict([[7.45]]))
        
plt.show()


from sklearn.ensemble import RandomForestRegressor

rf_reg = RandomForestRegressor(n_estimators=10, random_state=0)
rf_reg.fit(X,Y)
print(rf_reg.predict([[7]]))
print(lin_reg.predict([[7]]))
plt.scatter(X, Y,color="red")
plt.plot(X, lin_reg.predict(X))
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color="blue")
plt.plot(X,r_dt.predict(X),color="pink")


from sklearn.metrics import r2_score


print("random forest R2 square değeri : \n",r2_score(Y,rf_reg.predict(X)))
print("Decision tree R2 square değeri : \n",r2_score(Y,r_dt.predict(X)))
print("linear regression R2 square değeri : \n",r2_score(Y,lin_reg.predict(X)))
print("polynomal regression R2 square değeri : \n",r2_score(Y,lin_reg2.predict(poly_reg.fit_transform(X))))
print("suppor vector regression : \n", r2_score(y_olcekli,svr_reg.predict(x_olcekli)))












