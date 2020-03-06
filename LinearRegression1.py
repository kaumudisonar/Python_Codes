import numpy as np
import matplotlib.pyplot as plt


def Linear():
    x=[1,2,3,4,5]
    y=[3,4,2,4,5]

    #To calculate Xbar and Ybar
    xbar=0
    ybar=0
    for i in range(len(x)):
        xbar=xbar+x[i]
        ybar=ybar+y[i]
    print("values of xbar and ybar is ,",xbar,ybar)
    
    #Mean of the x and y
    mean_x=xbar/len(x)
    mean_y=ybar/len(y)
    print("mean of x and y is ,",mean_x,mean_y)
    
   #Calculate slope of the line which is
    #y= m*x + c in which we have to find m=((x-xbar)*(y-ybar))/(x-xbar)**2
    numerator=0
    denomerator=0
    for i in range(len(x)):
        numerator+=((x[i]-mean_x)*(y[i]-mean_y))
        denomerator+=(x[i]-mean_x)**2
    m=numerator/denomerator
    print("Value of slope is ,",m)

    #to get the value of c the formula will be : c=y-mx
    c = mean_y - (m * mean_x)
    print("Y intercept of regression line is,",c)

    #Display plotting of above points
    plot_x=np.linspace(1,6,len(x))
    plot_y= c + (m * plot_x)
    
    plt.plot(plot_x,plot_y,color='#58b970',label='Regression Line')
    plt.scatter(x,y,color='#ef5423',label='Scattered Plot')
    plt.legend()
    plt.show()



def main():

    print("inside main")
    Linear()





if __name__ == "__main__":
    main()