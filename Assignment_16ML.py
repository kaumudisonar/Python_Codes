# Advertisement Agency

import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error,mean_absolute_error
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from seaborn import countplot

class AdvertiseAgencyPredictor():
    
    #Step 1: load the data
    adv_data=pd.read_csv('Advertising.csv')
    
    #Step 2: clean,manipulate and prepare the data
    feature_names=['TV','radio']
    x_features=adv_data[feature_names]
    y_target="sales"

    #Plot the points for TV
    figure()
    adv_data["TV"].plot.hist().set_title("tv test")
    show()
    #Plot the points for Radio
    figure()
    adv_data["radio"].plot.hist().set_title("radio test")
    show()
    
    # split data
    train_data,test_data,train_target,test_target=train_test_split(x_features,y_target,test_size=0.40)
    
    # # Step 3: Decide the algorithm
    model=LinearRegression()
    
    # Step 4: Train the algorithm
    model.fit(train_data,train_target)
    # print(model.intercept_)
    # print(model.coef_)
    # zip(feature_names, model.coef_)
    
    #Step 5: Test the algorithm
    #make predictions on the testing set
    y_pred = model.predict(test_data)
    #compute the RMSE of our predictions
    print("MAE is",mean_absolute_error(y_pred,test_target))
    print("MSE is ",mean_squared_error(y_pred,test_target))
    print("RMSE is",np.sqrt(mean_squared_error(y_pred,test_target)))
    
    
    
def main():
    AdvertiseAgencyPredictor()
    

if __name__== "__main__":
    main()