# 2. Design automation script which accept directory name and write names of duplicate files from
# that directory into log file named as Log.txt. Log.txt file should be created into current
# directory.
 # Usage : DirectoryDusplicate.py “Demo” 
 
import logging
#duplicate file remover

import sys
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

def findDups(path):
    dups = {}
    flag =os.path.isabs(path)
    if flag == False:
        path= os.path.abspath(path)
    exist = os.path.isdir(path)
    if exist:
        for folders,subfolders,files in os.walk(path):
            print("Current Directory name is"+folders)
            for flen in files:
                path = os.path.join(folders,flen)
                hash_file = hashfile(path)
                if hash_file in dups:
                    dups[hash_file].append(path)
                else:
                    dups[hash_file]=[path]
        return dups
    else :
        print("error")

def removeDuplicateFiles(dict1):
    results = list(filter(lambda x : len(x)>1 ,dict1.values()))
    icnt=0
    if len(results)>0:
        for result in results:
            for sub in result:
                icnt+=1
                if icnt>=2:
                    os.remove(sub)
            icnt=0
        print("Duplicate files deleted")
    else:
        print("No duplicates found")

def printResults(dict1):
    results=list(filter(lambda x : len(x)>1 , dict1.values()))
    
    if len(results)>0:
        print("Duplicates found")
        print("Following are the duplicates :")
        for result in results:
            for sub in result:
                print(f"%s"+ sub)
    else:
        print("No duplicate found")

def main():
    print("Developed by Kaumudi Sonar")
    if len(sys.argv)!=2:
        print("Please enter exact number of arguments")
        exit()
    if (sys.argv[1]=="-h") or (sys.argv[1]=="-H"):
        print("It is for to delete duplicate files from your machine and display the deleted files on console")
        exit()
    if (sys.argv[1]=="-u") or (sys.argv[1]=="-U"):
        print("Usage : Name of Directory")
        exit()
    try:
        arr={}
        arr = findDups(sys.argv[1])
        removeDuplicateFiles(arr)
        printResults(arr)
    except ValueError:
        print("Invalid type of input")
    except Exception as E:
        print("Error: Invalid input",E)

if __name__ == "__main__":
    main()