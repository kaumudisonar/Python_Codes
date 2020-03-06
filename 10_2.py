# 2. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.
 # Usage : DirectoryRename.py “Demo” “.txt” “.doc”
 
 
from sys import *
import os

def directoryExtension(path,extn,extn2):

    flag = os.path.isabs(path)
    if flag==False:
        flag = os.path.abspath(path)
    exist = os.path.isdir(path)
    if exist:
        for Folders,subfolders,files in os.walk(path):
            for flen in files:
                if flen.endswith(extn):
                    base = os.path.splitext(flen)[1]
                    flen.replace(base,extn2)
                   
    else:
        print("It is not a director")

def main():
    print("Developed by Rucha Sonar")
    print("Application name",argv[0])

    if (len(argv)!=4):
        print("Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1]=="-H"):
        print("This script is for available directory contents in the machine")
        exit()
        

    if (argv[1] == "-u") or (argv[1]=="-U"):
        print("Usage of the script is :")
        print("Usage : Application_Name and Absolute path of directory")
        exit()
    # try:
    directoryExtension(argv[1],argv[2],argv[3])
    # except ValueError:
        # print("Invalid Datatype of error")
    # except Exception:
        # print("Invalid input",Exception)

if __name__ == "__main__":
    main()
 