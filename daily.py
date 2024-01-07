#Author: Efe
#Date:7th of Jan 2024
import trader
from multiprocessing import Process
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import stripe
from app import generate_id
import requests
from bs4 import BeautifulSoup
import redis
import json
import time
import random
from datetime import datetime

r=redis.Redis()
server = "main"
base = "http://127.0.0.1:3000"

stripe.api_key = "sk_test_51KNGcuEz0P2Wm1hTXPKe291k3qbGjhJqxaryuuNe2J0mSFhiZrI69LYIbWIAYIbGT3LYPOc4MyTAnkGmtleJobxh00LPcn5oI7"


class FinLister:
    def __init__(self,url):
        if "finviz.com" not in url:
            raise ValueError("This library is built for finviz.com")
        self.url = url
        self.stocks = []
        self.pages = []
    def fetch(self,r="1"):
        page = requests.get(self.url+"&r="+r,headers={"User-Agent":"Mozilla Firefox Macintel Chrome everything"})
        soup = BeautifulSoup(page.content,"html.parser")
        availablePages = soup.find("select",{"id":"pageSelect"})
        if r == "1":
            allOptions = availablePages.find_all("option")
        
            for a in allOptions:
                if a.get("value") != "1":

                    self.pages.append(a.get("value"))
        if r == "1":
            self.pages.reverse()
        allTr = soup.find_all("tr")
        for t in allTr:
            try:
                allTd= t.find_all("td")
                number = allTd[0].get_text()
                ticker = allTd[1].get_text()
                company = allTd[2].get_text()
                sector = allTd[3].get_text()
                industry = allTd[4].get_text()
                country = allTd[5].get_text()
                marketCap = allTd[6].get_text()
                price2Earnings = allTd[7].get_text()
                price = allTd[8].get_text()
                change = allTd[9].get_text()
                volume = allTd[10].get_text()
            except:
                continue

            data = {

                "number":number,
                "ticker":ticker,
                "company":company,
                "sector":sector,
                "industry":industry,
                "country":country,
                "marketCap":marketCap,
                "pe":price2Earnings,
                "price":price,
                "volume":volume
            } 
            #print(data["ticker"])
            
            try:
                int(number)
                self.stocks.append(data)
            except:
                pass
        try:
            lastItem = self.pages[-1]
            self.pages.pop()
            self.fetch(r=lastItem)            
        except:
            return self.stocks


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

        signal,score,price,change = trader.DailySignal(s["ticker"])
        acc= float(r.get(s["ticker"]).decode())*100
        if acc<74:
            continue
        if signal == "BUY" and score>97:
            d = {
                "comp":s,
                "signal":signal,
                "score":score,
                "price":price,
                "acc":acc


            }
            notifications.append(d)
    data = {
        "d":{
            "notifications":notifications,
            "time":time.time(),
            "_id":generate_id(45)
        }
        "passpharase":"efeakaroz"

    }
    now = datetime.now()
    datestring = f"{now.month}/{now.day}/{now.year}"
    mailHTML = open("templates/email/scan.html","r").read().replace("-date-",datestring).replace("-id-",data["_id"])
    upload= requests.post("/secret/kentel/issueUpload",data=json.dumps(data),headers={"User-Agent":"sagent"})



