#!/usr/bin/python
def Readfilelinebyline(file_name):
    fd=open(file_name)
    line=fd.readline()
    while line!='':
        print(line,end='')
        line=fd.readline()
    fd.close()
def main():
    fname = eval(input('enter filename:'))

     Readfilelinebyline(fname)
if __name__== '__main__':
    main()
