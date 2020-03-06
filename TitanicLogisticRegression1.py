# Classifier : Logistic Regression
# DataSet : Titanic Dataset
# Features : Passenger id,Gender, Age, Fare, Class etc
# Labels : - Survived or not , 0 or 1

import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from seaborn import countplot

class TitanicLogistic():
    
    #Step 1: load the data
    titanic_data=pd.read_csv('MarvellousTitanicDataset.csv')
    
    
    #Step 2: Analyse the data
    feature_names=['Age','Fare','Sex','sibsp','Parch','Pclass','Embarked']
    x_features=titanic_data[feature_names]
    y_target="Survived"

    # #Graph for Survived and not Survived passengers
    # countplot(data=titanic_data,x=y_target).set_title("Data for Survived against not Survived passengers")
    # show()
    # #Graph of Fare against Survived and not Survived passengers
    # countplot(data=titanic_data,x=y_target,hue="Fare").set_title("Data for Survived against not Survived passengers")
    # show()
    # #Plot the graph against age
    # figure()
    # titanic_data["Age"].plot.hist().set_title("Age against survive people")
    # show()
    # #Plot the points for sex using count plot
    # countplot(data=titanic_data,x=y_target,hue="Sex").set_title("Gender against survive people")
    # show()
    # #Graph for Survived and not Survived passengers
    # countplot(data=titanic_data,x=y_target,hue="Pclass").set_title("Graph for class wise passengers")
    # show()
    
    #Step 3: clean,manipulate and prepare the data
    titanic_data.drop(["zero","Sex","sibsp","Parch","Embarked"],axis=1,inplace=True)
    print(titanic_data.head())
    
    #Step 4:decide the algorithm,data training and data testing
    x=titanic_data.drop(("Survived"),axis=1)
    y=titanic_data["Survived"]
    
    # split data
    train_data,test_data,train_target,test_target=train_test_split(x,y,test_size=0.40)
    
    # Decide the algorithm
    model=LogisticRegression()
    
    #Train the algorithm
    model.fit(train_data,train_target)
    
    #Step 4:Test the data
    prediction=model.predict(test_data)
    
    #Step 5: Calculate accuracy
    print("Classification report of logistic regression is ,",classification_report(test_target,prediction))
    print("Confusion matrix of logistic regression is ,",confusion_matrix(test_target,prediction))
    print("Accuracy score of logistic regression is ,",accuracy_score(test_target,prediction)*100,"%")
    
def main():
    TitanicLogistic()
    

if __name__== "__main__":
    main()