import sys
import filecmp

def main():

	res =filecmp.cmp(sys.argv[1],sys.argv[2])
	if res:
		print("Success")
	else:
		print("Failure")

if __name__ == "__main__":
    main()