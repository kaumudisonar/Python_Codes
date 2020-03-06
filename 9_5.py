import sys
import os

def main():
	name = sys.argv[1]
	str1 = sys.argv[2]	
	wordstring =sys.argv[2]
	lst =wordstring.split()
	wordfreq = []
	for w in lst:
		wordfreq.append(lst.count(w))
	print("Frequencies is " +str(wordfreq))


if __name__ == "__main__":
    main()