import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)
creditcard=pd.read_csv('creditcard.csv')
print(creditcard.columns)
x=creditcard.drop(['Class','V9','V18','V25'],axis=1)
y=creditcard['Class']

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=66) 
rf = RandomForestClassifier(n_estimators=100,random_state=0)
rf.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(rf.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(rf.score(X_test, y_test))) 
print("Feature importances:\n{}".format(rf.feature_importances_))

rf1 = RandomForestClassifier(max_depth=3, n_estimators=100,
random_state=0)
rf1.fit(X_train, y_train)
print("Accuracy on training set for rf1: {:.3f}".format(rf1.score(X_train, y_train)))
print("Accuracy on test set for rf1: {:.3f}".format(rf1.score(X_test, y_test)))

# def plot_feature_importances_diabetes(model):
    # plt.figure(figsize=(8,6))
    # n_features = 8
    # plt.barh(range(n_features), model.feature_importances_, align='center')
    # diabetes_features = [x for i,x in enumerate(dicreditcardabetes.columns) if i!=8]
    # plt.yticks(np.arange(n_features), diabetes_features)
    # plt.xlabel("Feature importance")
    # plt.ylabel("Feature")
    # plt.ylim(-1, n_features)
    # plt.show()
# plot_feature_importances_diabetes(rf)