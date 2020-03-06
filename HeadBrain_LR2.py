# Classifier : Linear Regression
# DataSet : Head Brain Dataset
# Features : Gender, Age, Head size, Brain weight
# Labels : -
# Training Dataset : 237

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def headBrainPredictor():
    data=pd.read_csv("MarvellousHeadBrain.csv")
    print("Size of data set is ,",data.shape)
    X=data['Head Size(cm^3)'].values
    Y=data['Brain Weight(grams)'].values
    
    #Calculate mean that is xbar and ybar
    mean_x=np.mean(X)
    mean_y=np.mean(Y)
    print("Mean of X and Y is ,",mean_x,mean_y)
    
    #Calculate slope of the line which is
    #y= m*x + c in which we have to find m=((x-xbar)*(y-ybar))/(x-xbar)**2
    numerator=0
    denomenator=0
    for i in range(len(X)):
        numerator+=((X[i]-mean_x)*(Y[i]-mean_y))
        denomenator+=(X[i]-mean_x)**2
    m=numerator/denomenator
    print("Slope of the line is ,",m)
    
    #Find the value of y intercept
    c = mean_y - (m * mean_x)
    print("Y intercept of the line is,",c)

    max_x=np.max(X)+100
    min_x=np.min(X)-100
    
    #display plotting of above points 
    x=np.linspace(min_x,max_x,len(X))
    y= c+ (m*x)
    
    plt.plot(x,y,color='#58b970',label='Regression Line')
    plt.scatter(X,Y,color='#58b970',label='Regression Line')
    plt.xlabel('Head Size(cm^3)')
    plt.ylabel('Brain Weight(grams)')
    plt.legend()
    plt.show()
    
    #Find goodness of fit i.e R Square
    ss_t=0
    ss_r=0
    
    for i in range(len(X)):
        y_pred=c + (m * X[i])
        ss_t+=(Y[i]-mean_y)**2
        ss_r+=(Y[i]-y_pred)**2
    r2=1-(ss_r/ss_t)
    print("R Square value is,",r2)

def main():
    headBrainPredictor()



if __name__ == "__main__":
    main()