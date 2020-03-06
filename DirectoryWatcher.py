from sys import *
import os

def DirectoryWatcher(path):

    flag = os.path.isabs(path)
    if flag == False:
        path=os.path.abspath(path)
    exists = os.path.isdir(path)

    if exists:
        for folders,subfolders,files in os.walk(path):
            print("Current folder is",folders)
            for fldr in subfolders:
                print("Subfolder of" + folders + "is",fldr)
            for fi in files:
                print("Files inside"+folders+ "is",fi)
    else:
        "Invalid Path"

def main():
    print("Developed by Rucha Sonar")
    print("Application name",argv[0])

    if (len(argv)!=2):
        print("Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1]=="-H"):
        print("This script is for available directory contents in the machine")
        exit()

    if (argv[1] == "-u") or (argv[1]=="-U"):
        print("Usage of the script is :")
        print("Usage : Application_Name and Absolute path of directory")
        exit()
    try:
        DirectoryWatcher(argv[1])
    except ValueError:
        print("Invalid Datatype of error")
    except Exception:
        print("Invalid input")

if __name__ == "__main__":
    main()