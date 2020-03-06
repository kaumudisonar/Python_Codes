import sys
import os

def isOpen(path):
    fobj=open(path,"r")
    print(fobj.read())

def main():
    isOpen(sys.argv[1])

if __name__ == "__main__":
    main()