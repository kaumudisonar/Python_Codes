#!/usr/bin/python
def main():
    s1=eval(input('Enter 1st string'))
    s2=eval(input('enter string 2 to check'))
    if isrot(s1,s2):
        print('{} is rotation of {} '.format(s1,s2))
    else:
        print('{} isnot a rotation of {}'.format(s1,s2))
        if __name__=='__main__':
            main()

def isrot(s1,s2):
    if len(s1)==len(s2):
        if s2 in s1+s1:
            return True
        return False 
    
