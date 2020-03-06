import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class PlayDetector():
    
    #Step 1: load the data
    data=pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")
    
    #Step 2: clean,manipulate and prepare the data
    #features=['Wether','Temperature']
    whether=data.Whether
    temp=data.Temperature
    play=data.Play
    
    #Creating label encoder
    le=preprocessing.LabelEncoder()
    
    #Convert values into numbers
    whether_encoded=le.fit_transform(whether)
    tempreture_encoded=le.fit_transform(temp)
    label_encoded=le.fit_transform(play)
    
    #Combine features into single list
    features=list(zip(whether_encoded,tempreture_encoded))
    
    #split data
    train_data,test_data,train_target,test_target=train_test_split(features,label_encoded,test_size=0.20)
    
    #Step 3: Decide the algorithm
    model=KNeighborsClassifier(n_neighbors=4)
    
    #Step 4: Train the algorithm
    model.fit(train_data,train_target)
    
    #Step 5: Test the algorithm
    results=model.predict(test_data)
    accuracy=accuracy_score(results,test_target) 
    print(accuracy*100,"%")
    
def main():
    accuracy=PlayDetector()
    

if __name__== "__main__":
    main()