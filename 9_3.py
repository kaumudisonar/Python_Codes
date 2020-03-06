import sys
import os
import shutil

def createAndCopyContents(path):
    fobj=open(path,"a")
    print(fobj.write("Good morning"))
    shutil.copyfile("demo.py",sys.argv[1])

def main():
    createAndCopyContents(sys.argv[1])

if __name__ == "__main__":
    main()