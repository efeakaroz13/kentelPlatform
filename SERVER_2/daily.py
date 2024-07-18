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

r=redis.Redis()
server = "secondary"
base = "https://kentel.dev"

stripe.api_key = "sk_test_51KNGcuEz0P2Wm1hTXPKe291k3qbGjhJqxaryuuNe2J0mSFhiZrI69LYIbWIAYIbGT3LYPOc4MyTAnkGmtleJobxh00LPcn5oI7"

def generate_id(charNumber):
    alphabet = "thequickbrownfoxjumpedoverthelazydog"
    a = []
    for _ in alphabet:
        a.append(_)
    output = ""
    for i in range(charNumber):
        intorchar = random.randint(0,1)
        if intorchar == 1:
            #char
            selectedChar = random.choice(a)
            upperOrLower = random.randint(0,1)
            if upperOrLower == 1:
                selectedChar = selectedChar.upper()
            output += selectedChar

        if intorchar == 0:
            num = random.randint(0,9)
            num = str(num)
            output+=num

    return output

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

def send(mails,content):

    #There is a person identifier image that let's us see if the person opened the email or not.
    #For that, you need to send the user ID to the HTML content.
    mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
    mailserver.ehlo()
    mailserver.login('sales@kentel.dev', 'efeAkaroz123!')
    for m in mails:
        

        id_ = m["_id"]
        content.replace("-id-",id_)
        m = m["email"]
        msg = MIMEMultipart()
        msg.set_unixfrom('author')
        msg['From'] = 'Kentel <sales@kentel.dev>'
        msg['To'] = m
        msg['Subject'] = 'Daily Insight'
        message = content

        msg.attach(MIMEText(message,"html"))

        

        mailserver.sendmail('sales@kentel.dev',m,msg.as_string())

    mailserver.quit()
    return 0




if __name__ == "__main__":
    # if server == "main":
    #     pass
    # else:
    #     os.system("rm models/*")
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
        try:
            
            signal,score,price,change ,warn = trader.DailySignal(s["ticker"])
        except:
            time.sleep(5)
            try:
                signal,score,price,change ,warn = trader.DailySignal(s["ticker"])
            except Exception as e:
                print(f"[{time.ctime(time.time())}]",e,flush=True)
                continue
        score = round(score*100,2)
        acc= float(r.get(s["ticker"]).decode())*100
        if acc<72:
            continue
        acc=  round(acc,2)
        if signal == "BUY" and score>98:
            d = {
                "comp":s,
                "signal":signal,
                "score":score,
                "price":price,
                "acc":acc,
                "warning":warn


            }
            notifications.append(d)

    #print(notifications)
    data = {
        "d":{
            "notifications":notifications,
            "time":time.time(),
            "_id":generate_id(45),
            "exchange":"SERVER2_DAILY_NASDAQ"
        },
        "passpharase":"efeakaroz"

    }
    now = datetime.now()
    datestring = f"{now.month}/{now.day}/{now.year}"
    content = ""
    try:
        signal,score,price,change ,warn = trader.DailySignal("^NDX")
        score = round(score*100,2)
        acc= float(r.get('^NDX').decode())*100


        acc=  round(acc,2)
        if signal == "BUY":
            contentIndexFund = f"""<br><br>
            <div style='color:green;font-size:13px'>Nasdaq 100:{score}% Buy score</div>
            <p>*:experienced rapid change</p>
            """
        elif signal == "SELL":
            contentIndexFund = f"""<br><br>
            <div style='color:red;font-size:13px'>Nasdaq 100:{score}% Sell score</div>
            <p>*:experienced rapid change</p>
            """
    except:
        contentIndexFund = ""


    for n in notifications:
        color = ""
        try:
            if n["warning"]:
                color = "color:yellow"
        except:
            color = None
        ticker = n['comp']['ticker']
        if color:
            ticker=ticker+"*"
        line = f"<p style='font-weight:400;font-size:20px;'>{ticker} | <a style='color:green'>{n['score']}% {n['signal']}</a> | <a>{n['acc']} Accuracy</a> | <a>${n['price']}</a></p>"
        content = content+line

    content +=contentIndexFund
    if True:
        mailHTML = open("templates/email/scan.html","r").read().replace("-date-",datestring).replace("-content-",content).replace("-number-",str(len(notifications))).replace("-preview-","Stay informed with your daily stock report from Kentel! Discover valuable insights and predictions to navigate the stock market effectively.")
        upload= requests.post(f"{base}/secret/kentel/issueUpload",data=json.dumps(data),headers={"User-Agent":"sagent",'Content-type':'application/json', 'Accept':'application/json'})
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
        time.sleep(100)


