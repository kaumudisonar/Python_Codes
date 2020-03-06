#Dot error is still pending

from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score


print("Fetures of iris dataset is :",iris.feature_names)
print("Target of iris dataset is :",iris.target_names)

#index's needs to remove
test_index=[1,51,101]

#to split data using delete method from np
#To remove test data from training data set
train_target=np.delete(iris.target,test_index)
train_data=np.delete(iris.data,test_index,axis=0)

#To get the testing data on train_data
test_target=iris.target[test_index]
test_data=iris.data[test_index]

clf=tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)
predict=clf.predict(test_data)

accuracy=accuracy_score(test_target,predict)

print(accuracy*100,"%")

#####################################################################################################
#To split data using sklearn inbuilt method

from sklearn.model_selection import train_test_split
iris=load_iris()

data=iris.data
target=iris.target
#To split data using split method from sklearn
train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.5)

clf=tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)
predict=clf.predict(test_data)

accuracy=accuracy_score(test_target,predict)

print(accuracy*100,"%")


# #Visualization
# from sklearn.externals.six import StringIO
# import pydot
# import os
# os.environ["PATH"] += os.pathsep + 'C:/Users/sonali/Desktop/Rucha_Official/Python/Python37/Lib/site-packages/graphviz'

# dot_data=StringIO()
# tree.export_graphviz(clf,out_file=dot_data,feature_names=iris.feature_names,class_names=iris.target_names,filled=True,rounded=True,impurity=False)
# graph=pydot.graph_from_dot_data(dot_data.getvalue())
# graph[0].write_pdf("IRISDecisionTree.pdf")



