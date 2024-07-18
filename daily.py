#Author: Efe
#Date:7th of Jan 2024
import trader
from multiprocessing import Process
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import stripe
import requests
from bs4 import BeautifulSoup
import redis
import json
import time
import random
from datetime import datetime
import os 
from filters import FinLister

r=redis.Redis()
server = "main"
base = "http://127.0.0.1:3000"

stripe.api_key = "sk_test_51KNGcuEz0P2Wm1hTXPKe291k3qbGjhJqxaryuuNe2J0mSFhiZrI69LYIbWIAYIbGT3LYPOc4MyTAnkGmtleJobxh00LPcn5oI7"



class MailFetcher:
    def __init__(self):
        self.mails = []
    def fetch(self,p=0):

        page = requests.post(f"{base}/secret/kentel/mailingL",headers={
            "User-Agent":"sagent"
            },data={
                "page":p,
                "passpharase":"efeakaroz"
            })
        data = json.loads(page.content)["m"]
        for m in data:
            self.mails.append(m)

        if len(data) == 0 :
            pass
        else:
            self.fetch(p=p+1)

def send(mails,content):
    #There is a person identifier image that let's us see if the person opened the email or not.
    #For that, you need to send the user ID to the HTML content.
    for m in mails:
        id_ = m["_id"]
        content.replace("-id-",id_)
        m = m["email"]
        msg = MIMEMultipart()
        msg.set_unixfrom('author')
        msg['From'] = 'sales@kentel.dev'
        msg['To'] = m
        msg['Subject'] = 'Here is your daily stock report'
        message = content
        msg.attach(MIMEText(message,"html"))

        mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
        mailserver.ehlo()
        mailserver.login('sales@kentel.dev', 'efeAkaroz123!')

        mailserver.sendmail('sales@kentel.dev',m,msg.as_string())

        mailserver.quit()
    return 0
if __name__ == "__main__":
    if server == "main":
        pass
    else:
        os.system("rm models/*")
    mf = MailFetcher()
    mf.fetch()
    mails = mf.mails
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    counter = 1

    for m in mails:
        if counter == 1:
            t1.append(m)
        if counter == 2:
            t2.append(m)
        if counter  == 3:
            t3.append(m)

        if counter == 4:
            t4.append(m)
            counter = 0
        counter +=1




    filter_main = "https://finviz.com/screener.ashx?v=111&f=cap_microover,fa_curratio_o1.5,fa_estltgrowth_u10,fa_roe_o15,ta_beta_o1.5,ta_sma20_pa&ft=4"
    fin = FinLister(filter_main)
    fin.fetch()
    stocks = fin.stocks
    notifications = []
    for s in stocks:

        signal,score,price,change ,warn = trader.DailySignal(s["ticker"])
        score = round(score*100,2)
        acc= float(r.get(s["ticker"]).decode())*100
        if acc<72:
            continue
        acc=  round(acc,2)
        if signal == "BUY" and score>97:
            d = {
                "comp":s,
                "signal":signal,
                "score":score,
                "price":price,
                "acc":acc


            }
            notifications.append(d)

    print(notifications)
    data = {
        "d":{
            "notifications":notifications,
            "time":time.time(),
            "_id":generate_id(45)
        },
        "passpharase":"efeakaroz"

    }
    now = datetime.now()
    datestring = f"{now.month}/{now.day}/{now.year}"
    content = ""
    for n in notifications:
        line = f"<p style='font-weight:400;font-size:20px'>{n['comp']['ticker']} | <a style='color:green'>{n['score']}% {n['signal']}</a> | <a>{n['acc']} Accuracy</a> | <a>{round(n['price'],2)}$</a></p>"
        content = content+line

    mailHTML = open("templates/email/scan.html","r").read().replace("-date-",datestring).replace("-content-",content).replace("-number-",str(len(notifications)))
    upload= requests.post(f"{base}/secret/kentel/issueUpload",data=json.dumps(data),headers={"User-Agent":"sagent"})
    p1= Process(target=send,args=(t1,mailHTML))
    p2= Process(target=send,args=(t2,mailHTML))
    p3= Process(target=send,args=(t3,mailHTML))
    p4= Process(target=send,args=(t4,mailHTML))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()


