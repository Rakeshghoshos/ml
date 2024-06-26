# -*- coding: utf-8 -*-
"""voting_ensemble.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fz7RLqbADmI92w2aHvaJqlPDbHZnksK8
"""

import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix,f1_score
import matplotlib.pyplot as plt

X,y = make_classification(n_samples=1000,n_features=2,n_informative=2,n_redundant=0,random_state=42)

x1 = X[:,0]
x2 = X[:,1]

plt.scatter(x1,x2,c=y)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

cls_log = LogisticRegression()
cls_tree = DecisionTreeClassifier()
cls_knn = KNeighborsClassifier()

cls_log.fit(X_train,y_train)
cls_tree.fit(X_train,y_train)
cls_knn.fit(X_train,y_train)

log_pred = cls_log.predict(X_test)
tree_pred = cls_tree.predict(X_test)
knn_pred = cls_knn.predict(X_test)

print(accuracy_score(y_test,log_pred))
print(accuracy_score(y_test,tree_pred))
print(accuracy_score(y_test,knn_pred))

print(confusion_matrix(y_test,log_pred))
print(confusion_matrix(y_test,tree_pred))
print(confusion_matrix(y_test,knn_pred))

v = VotingClassifier(estimators=[('c1',cls_log),('c2',cls_tree),('c3',cls_knn)])

v.fit(X_train,y_train)

v_predict = v.predict(X_test)

accuracy_score(y_test,v_predict)

confusion_matrix(y_test,v_predict)