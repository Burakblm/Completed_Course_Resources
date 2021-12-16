# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:44:23 2021

@author: ASUS
"""
import pandas as pd
url = "http://bilkav.com/satislar.csv"
veriler = pd.read_csv(url)
veriler = veriler.values
X = veriler[:,0:1]
y = veriler[:,1]


from sklearn.model_selection import train_test_split
X_train , X_test,y_train,y_test = train_test_split(X,y,test_size=0.33)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)
print(lr.predict(X_test))

import pickle
dosya = "model.kayıt"
# dump fonksiyonu modeli kayıt etmeye yarar
pickle.dump(lr,open(dosya,"wb"))

# load fonksiyonu kayıtlı modeli yüklemeye yarar
yuklenen =pickle.load(open(dosya,"rb"))
print(yuklenen.predict(X_test))











