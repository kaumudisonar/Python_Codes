# 4. Design automation script which accept two directory names and one file extension. Copy all
# files with the specified extension from first directory into second directory. Second directory
# should be created at run time.
 # Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
# Demo is name of directory which is existing and contains files in it. We have to create new
# Directory as Temp and copy all files with extension .exe from Demo to Temp

from sys import *
import os
import shutil

def directoryCopy(src,dst,extn,symlinks=False, ignore=None):
     
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        if item.endswith(extn):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):       
                shutil.copytree(s,d,symlinks,ignore)
            else:
                shutil.copy(s,d)
                
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
    directoryCopy(argv[1],argv[2],argv[3])
    # except ValueError:
        # print("Invalid Datatype of error")
    # except Exception:
        # print("Invalid input",Exception)

if __name__ == "__main__":
    main()
 