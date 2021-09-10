import requests
import json
import smtplib
import urllib
import urllib.request
import re
t=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
t=t.json()
btcprice=t["bitcoin"]["usd"]
print("The current price of BTC is "+str(btcprice))
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("btcalerttrigger", "BT(@lerttrigger")
def settriggers():
    a=str(input("Do you want to set an alert? Enter Y/N: "))
    if(a=='Y'):
        target=input("Enter your target price: ")
        send=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=YE4BDPOOVTOCAPMS&field1='+target)
        emails=[]
        nemails=int(input("Enter the number of emails: "))
        print("Enter the emails one by one:")
        n=0
        while(n!=nemails):
            email=str(input(str(n+1)+'. '))
            regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if(re.fullmatch(regex,email)==None):
                print("Not a valid email. Please try again.")
            else:
                exists=requests.get("https://isitarealemail.com/api/email/validate",params = {'email': email})
                exists=exists.json()['status']
                if(exists=="valid" and emails.count(email)==0):
                    print("Email is valid. Let's proceed.")
                    emails.append(email)
                    n+=1
                else:
                    if(emails.count(email)==1):
                        print("Email already exists. Skip this.")
                        n+1
                    else:
                        print("Email not yet exists. Please check again.")
        print("All emails entered. Checking Bitcoin price...")
        while True:
            t=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
            t=t.json()
            btcprice=t["bitcoin"]["usd"]
            if(btcprice==target):
                for dest in emails:
                    message = "Hello! The Bitcoin reached your target price "+str(target)+"!"
                    s.sendmail("btcalerttrigger@gmail.com",dest,message)
                s.quit()
                return("All mails sent.")
    if(a=='N'):
        b=str(input("Do you want to see your trigger history? Enter Y/N: "))
        if(b=='Y'):
            a=requests.get("https://thingspeak.com/channels/1502719/field/1")
            a=a.json()['feeds']
            for i in a:
                timestamp=i['created_at']
                value=i['field1']
                indexT=timestamp.index('T')
                date=timestamp[:indexT]
                time=timestamp[indexT+1:][:-1]
                print("Target of "+str(value)+" added on date "+str(date)+" at time "+str(time)+" GMT.")
            return("Done.")
        if(b=='N'):
            return("Thanks for visiting our app!")
    else:
        print("Invalid input. Please try again.")
        return settriggers()
print(settriggers())
