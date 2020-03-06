import sys
import os
import hashlib

def hashfile(path,blocksize=1024):
	afile = open(path,'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)
	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	afile.close()
	return hasher.hexdigest()

def displayChecksum(path):
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
				print(path)
				print(hash_file)
				print('')
		
def main():
	try:
		displayChecksum(sys.argv[1])
	except ValueError:
		print("Invalid type of input")
	except Exception as E:
		print("Error: Invalid input",E)

if __name__ == "__main__":
    main()