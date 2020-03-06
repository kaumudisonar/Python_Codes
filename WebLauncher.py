import sys
import urllib.request as urllib2

print(sys.path)

def isconnected():
    try:
        urllib2.urlopen('http://216.58.192.142',timeout=1)
        return True
    except urllib2.URLError as e:
        return False



def main():

    connected=isconnected()
    if connected:
        print("Connected")
    else:
        print("Not able to connect to internet")



if __name__ == "__main__":
    main()