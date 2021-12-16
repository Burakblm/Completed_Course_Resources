import numpy as np
import pandas as pd
yorumlar = pd.read_csv("Restaurant_Reviews.csv")

from sklearn.metrics import confusion_matrix
import re
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

derlem = []

# preproccesing (önişleme)
for i in range(1000):
    yorum = re.sub("[^a-zA-Z]"," ", yorumlar["Review"][i])
    yorum = yorum.lower()
    yorum = yorum.split()
    yorum = [ps.stem(kelime) for kelime in yorum if not kelime in set(stopwords.words("english"))]
    yorum = " ".join(yorum)
    derlem.append(yorum)

# feauture extraction (öznitelik çıkarımı)
# Bag of Words (BOW)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=2000)
X = cv.fit_transform(derlem).toarray() # bağımsız değişken
y = yorumlar.iloc[:,1].values # bağımlı değişken


# Makine öğrenmesi Kısmı
from sklearn.model_selection import train_test_split
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.20, random_state=0)

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
