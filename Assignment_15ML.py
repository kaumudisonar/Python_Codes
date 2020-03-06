# Classifier : K Nearest Neighbour
# DataSet : Wine Predictor Dataset
# Features : Alcohol,
 # Malic acid ,
 # Ash,
 # Alcalinity of ash ,
 # Magnesium ,
 # Total phenols ,
 # Flavanoids ,
 # Nonflavanoid phenols ,
 # Proanthocyanins ,
 # Color intensity,
 # Hue ,
 # OD280/OD315 of diluted wines ,
 # Proline
# Labels : Class 1, Class 2, Class 3
# Training Dataset : 70% of 178 Entries
# Testing Dataset : 30% of 178 Entries

import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import accuracy_score

class WinePredictor():
    
    #Step 1: load the data
    wine=datasets.load_wine()
    
    #Step 2: clean,manipulate and prepare the data
    #df=pd.DataFrame(data.data,columns=data.feature_names)
    
    
    # split data
    train_data,test_data,train_target,test_target=train_test_split(wine.data,wine.target,test_size=0.20)
    
    # Step 3: Decide the algorithm
    model=KNeighborsClassifier(n_neighbors=3)
    
    # Step 4: Train the algorithm
    model.fit(train_data,train_target)
    
    # Step 5: Test the algorithm
    results=model.predict(test_data)
    accuracy=accuracy_score(results,test_target) 
    print(accuracy*100,"%")
    
def main():
    WinePredictor()
    

if __name__== "__main__":
    main()