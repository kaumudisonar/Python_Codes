# 1.Design automation script which accept directory name and display checksum of all files.
 # Usage : DirectoryChecksum.py “Demo” 
 

from sys import *
import os
import hashlib
import string

def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def filesChecksum(path):

    flag = os.path.isabs(path)
    if flag==False:
        flag = os.path.abspath(path)
    exist = os.path.isdir(path)
    if exist:
        for Folders,subfolders,files in os.walk(path):
            for flen in files:
                path = os.path.join(Folders,flen)
                hash = hashfile(path)
                print("file name is" + flen + "and checksum of the file is"+hash)
                   
    else:
        print("It is not a director")

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
    # try:
    filesChecksum(argv[1])
    # except ValueError:
        # print("Invalid Datatype of error")
    # except Exception:
        # print("Invalid input",Exception)

if __name__ == "__main__":
    main()
 