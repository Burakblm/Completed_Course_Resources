# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 11:16:43 2021

@author: ASUS
"""
#1.kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('veriler.csv')

x = veriler.iloc[:,1:4].values # bağımsız değişkenler
y = veriler.iloc[:,4:].values  # bağımlı değişken

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

# buradan itibaren sınıflandırma algoritmaları başlar

# 1. Logistic Regression
from sklearn.linear_model import LogisticRegression
logr = LogisticRegression(random_state=0)
logr.fit(X_train,y_train) # fit metodu model eğitimi
y_pred_lr = logr.predict(X_test) # modelin tahim için kullanılması
print(y_pred_lr)
print(y_test)
# karmaşıklık matrisi 
cm = confusion_matrix(y_pred_lr,y_test)
print("Logistic Regression")
print(cm)


# 2. KNN algoritması 
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1,metric="minkowski")
knn.fit(X_train,y_train) # modelin eğitilmesi
y_pred_knn = knn.predict(X_test) # modelin tahmin için kullanılması
# karmaşıklık matrisi
cm2= confusion_matrix(y_test,y_pred_knn)
print("K neighbors classifier")
print(cm2)



# 3. SVC (SVM classifier)
from sklearn.svm import SVC
svc = SVC(kernel="rbf")
svc.fit(X_train,y_train) # model eğitilmesi
y_pred_svc = svc.predict(X_test) # modelin tahmin için kullanılması
# karmaşıklık matrisi
cm3 = confusion_matrix(y_pred_svc,y_test)
print("Support Vector Classifier")
print(cm3)



# 4. Naive Bayes
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train,y_train) # modelin eğitilmesi
y_pred = gnb.predict(X_test) # modelin tahmin için kullanılması
# karmaşıklık matrisi
cm3 = confusion_matrix(y_test,y_pred)
print("Gaussian Naive Bayes Classifier")
print(cm)



# 5. Decision Tree
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion="entropy")
dtc.fit(X_train,y_train) # modelin eğitilmesi
y_pred = dtc.predict(X_test) # modelin tahmin için kullanılması
# karmaşıklık matrisi
cm3 = confusion_matrix(y_test,y_pred)
print("Decision Tree Classifier")
print(cm)



# 6. Random Forest
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=20, criterion="entropy")
rfc.fit(X_train,y_train) # modelin eğitilmesi
y_pred = rfc.predict(X_test) # modelin tahmin için kullanılması
y_proba = rfc.predict_proba(X_test)
# karmaşıklık matrisi
cm3 = confusion_matrix(y_test, y_pred)           
print("Random Forest Classifier")
print(cm3)


# 7. ROC , TPR , FPR değerleri
print(y_test)
print(y_proba)
print(y_proba[:,0])
from sklearn import metrics
fpr , tpr , thold = metrics.roc_curve(y_test,y_proba[:,0],pos_label="e")
print("False Positive Rate\n",fpr)
print("True Positive Rate \n",tpr)








