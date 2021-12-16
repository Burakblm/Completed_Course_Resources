# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:32:30 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

veriler = pd.read_csv("maaslar_yeni.csv")

x = veriler.iloc[:,2:5]
y = veriler.iloc[:,5:]

x_train , x_test ,y_train ,y_test = train_test_split(x,y,test_size=0.33,random_state=0)

# linear regression
lin_reg = LinearRegression()
lin_reg.fit(x,y)
print("linear regression")
print(r2_score(y,lin_reg.predict(x)))

#polynomial regression
poly_reg = PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(x)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
print("polynomial regression")
print(r2_score(y,lin_reg2.predict(poly_reg.fit_transform(x))))

# support vector regression
svr_reg = SVR(kernel="rbf")
svr_reg.fit(x,y)
print("support vector recression")
print(r2_score(y,svr_reg.predict(x)))

# decision tree regression
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(x,y)
print("decision tree regression")
print(r2_score(y,r_dt.predict(x)))


rf_reg = RandomForestRegressor(n_estimators=20, random_state=0)
rf_reg.fit(x,y)
print("random forest regression")
print(r2_score(y,rf_reg.predict(x)))

# 10 yıl tecrubeli ve 100 puan alan ceo
print("\n \n \n")
print("linear regression: ",lin_reg.predict([[10,10,100]]))
print("polynomial regression: ",lin_reg2.predict(poly_reg.fit_transform([[10,10,100]])))
print("support vector regression: ",svr_reg.predict([[10,10,100]]))
print("decision tree regression: ",r_dt.predict([[10,10,100]]))
print("random forest regression: ",rf_reg.predict([[10,10,100]]))
print("\n \n \n")

# 10 yıl tecrubeli ve 100 puan alan müdür

print("\n \n \n")
print("linear regression: ",lin_reg.predict([[7,10,100]]))
print("polynomial regression: ",lin_reg2.predict(poly_reg.fit_transform([[7,10,100]])))
print("support vector regression: ",svr_reg.predict([[7,10,100]]))
print("decision tree regression: ",r_dt.predict([[7,10,100]]))
print("random forest regression: ",rf_reg.predict([[7,10,100]]))
print("\n \n \n")











