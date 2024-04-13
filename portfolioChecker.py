#17th jan 2024
#Kentel LTD
import requests
import json
import time
import os
import yfinance as yf
import trader
import redis
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

red= redis.Redis()

baseURL= "http://127.0.0.1:3000"
dataURL = "/secret/kentel/portfolioNotifier"


class portfolios:
    def __init__(self):
        self.portfolios = []

    def fetch(self,page=0):
        p ="efeakaroz"
        
        r = requests.post(baseURL+dataURL,headers={"User-Agent":"sagent"},data={
                "passpharase":p,
                "page":page
            })
        data=  json.loads(r.content)["n"]
        for d in data:
            self.portfolios.append(d)
        if len(data) != 0:
            self.fetch(page=page+1)
if __name__ == "__main__":
    p = portfolios()
    p.fetch()
    allPortfolio = p.portfolios
    for p in allPortfolio:
        email = p["email"]
        port = p["portfolioD"]["items"]
        tickersToNotify =[]
        for i in port:
            ticker=i["ticker"]
            price=i["cost"]
            try:
                priceNow = yf.Ticker(ticker).info["currentPrice"]
            except:
                continue
            change= (priceNow-price)*100/price#change as percent
            try:
                acc = float(red.get(t).decode())*100
            except:
                acc = 0
            #Signals: BUY SELL, score: 0-1, price: float
        

            signal,score,price,change ,warn = trader.DailySignal(ticker)
            score= score*100
            notify = False
            try:
                oldSignal = json.loads(red.get(ticker).decode())
                singal_old = oldSignal["signal"]
                score_old = oldSignal["score"]
                acc_old = oldSignal["accuracy"]
                if singal_old != signal and score>90:
                    notify = True
            except:
                notify = False
                oldSignal = {
                    "price":priceNow,
                    "signal":signal,
                    "score":score,
                    "checkedAt":time.time(),
                    "accuracy":acc,

                }
                red.set(ticker,json.dumps(oldSignal),ex=172800)

            if notify:
                tickersToNotify.append({"ticker":ticker,"signal":signal,"score":score,"acc":acc})

        content = ""
        if len(tickersToNotify)>0:
            for t in tickersToNotify:
                line = f"<p style='font-weight:400;font-size:20px'>{t['ticker']} | <a style='color:green'>{t['score']}% {t['signal']}</a> | <a>{t['acc']} Accuracy</a></p>"
                content = content+line
            now = datetime.now()
            datestring = f"{now.month}/{now.day}/{now.year}"
            mailHTML = open("templates/email/scan.html","r").read().replace("-date-",datestring).replace("-content-",content)

            m =email
            msg = MIMEMultipart()
            msg.set_unixfrom('author')
            msg['From'] = 'sales@kentel.dev'
            msg['To'] = m
            msg['Subject'] = 'Check out your portfolio, we detected AI signal changes'
            message = content
            msg.attach(MIMEText(message,"html"))

            mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
            mailserver.ehlo()
            mailserver.login('sales@kentel.dev', 'greenanarchist')

            mailserver.sendmail('sales@kentel.dev',m,msg.as_string())

            mailserver.quit()



