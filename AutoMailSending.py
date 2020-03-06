import sys
import smtplib
import urllib.request as urllib2

def isConnected():
    try:
        urllib2.urlopen('http://216.58.192.142',timeout =1)
        print("connected")
    except urllib2.URLError as err:
        print("Not connected")


def mailSender(gmail_user,gmail_pwd):
    print("Inside mail sender")
    sent_from = gmail_user
    to = ['rohansonar1@gmail.com']
    body = "This is auto generated mail"
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.login(gmail_user,gmail_pwd)
        server.sendmail(sent_from,to,body)
        server.close()
        
        print("mail sent successfully")
    except Exception as e:
        print(e)


def main():
    gmail_user = 'kaumudisonar@gmail.com'
    gmail_pwd = '*******'
    connected = isConnected()    
    mailSender(gmail_user,gmail_pwd)
    

if __name__ == "__main__":
    main()