import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

#the imported dataset does not have the required column names so lets add it

colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
irisdata = pd.read_csv(url, names=colnames)


X = irisdata.drop('Class', axis=1) #x contains all the features
y = irisdata['Class'] #contains the categories

#split my data set into 80% training and 20% test data

from sklearn.model_selection import train_test_split  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

#the SVC algorithm work
from sklearn.svm import SVC  
from sklearn.metrics import classification_report, confusion_matrix

svclassifier = SVC(kernel='rbf')  
svclassifier.fit(X_train, y_train)

print(X_train)

y_pred = svclassifier.predict(X_test)

#evaluating our model for prediction accuracy
df_cm = confusion_matrix(y_test, y_pred)
print(classification_report(y_test, y_pred))