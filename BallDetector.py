from sklearn import tree

def ballDetector(weight,surface):
    features=[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[96,0],[41,1],[56,0]]

    lables=[1,1,2,1,2,1,2,2,1,2]
    classi= tree.DecisionTreeClassifier()
    classi.fit(features,lables)
    result=classi.predict([[weight,surface]])
    if result==1:
        print("Your object looks like Tennis ball")
    elif result==2:
        print("Your object looks like Cricket ball")

def main():
    print("Enter weight of the ball")
    ballweight=input()
    print("What is the surface of your object,rough or smooth?")
    surface=input()
    if surface.lower()=="rough":
        surface=1
    elif surface.lower()=="smooth":
        surface=0
    else:
        print("Surface value is not valid")
        exit()
    ballDetector(ballweight,surface)

if __name__ == "__main__":
    main()