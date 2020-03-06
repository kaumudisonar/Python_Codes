import sys
import os

def isExist(path):
    print("inside function")
    print("File Exist :" +str(os.path.exists(path)))

def main():
    print("Inside main",sys.argv[0])

    isExist(sys.argv[1])

if __name__ == "__main__":
    main()