import re

def main():

    str = "Marvellous Infosystems , hello good morning"
    x = re.findall("llo",str)
    print(x)
   
    txt = "The rain in Spain"
    x = re.search("^The.*Spain$", txt)
    if (x):
        print("YES! We have a match!")
    else:
        print("No match") 
    



if __name__ == "__main__":
    main()