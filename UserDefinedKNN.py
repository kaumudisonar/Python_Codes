# Classifier : User Defined K Nearest Neighbour
# DataSet : Iris Dataset
# Features : Sepal Width, Sepal Length, Petal Width, Petal Length
# Labels : Versicolor, Setosa , Virginica
# Training Dataset : 75 Entries
# Testing Dataset : 75 Entries
from scipy.spatial import distance
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def euc(a,b):
    return distance.euclidean(a,b)
    
class userdefineKNN():
    def fit(self,TrainingData,TargetData):
        self.TrainingData=TrainingData
        self.TargetData=TargetData
    
    def predict(self,TestData):
        prediction = []
        for row in TestData:
            label=self.closestNode(row)
            prediction.append(label)
        return prediction
        
    def closestNode(self,row):
        bestdistance=euc(row,self.TrainingData[0])
        bestindex=0
        for i in range(len(self.TrainingData)):
            dist=euc(row,self.TrainingData[i])
            if dist < bestdistance:
                bestdistance=dist
                bestindex=i
        return self.TargetData[bestindex]

def KNeighbour():
    iris=load_iris()
    data=iris.data
    target=iris.target
    data_train,data_test,target_train,target_test=train_test_split(data,target,test_size=0.5)
        
    classifier=userdefineKNN()
    classifier.fit(data_train,target_train)
    prediction=classifier.predict(data_test)
    accuracy=accuracy_score(prediction,target_test)
    return accuracy
        

def main():
    Accuracy=KNeighbour()
    print("Accuracy is ",Accuracy*100,"%")
    


if __name__== "__main__":
    main()