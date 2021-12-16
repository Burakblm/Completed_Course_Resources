import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('odev_tenis.csv')

gorunum = veriler.iloc[:,0:1].values

from sklearn import preprocessing

ohe = preprocessing.OneHotEncoder()
gorunum = ohe.fit_transform(gorunum).toarray()
print(gorunum)


ruzgar = veriler.iloc[:,3:4].values
le = preprocessing.LabelEncoder()

ruzgar[:,0] = le.fit_transform(ruzgar)

print(ruzgar)




