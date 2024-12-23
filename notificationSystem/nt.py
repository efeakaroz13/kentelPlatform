#orangepi
from trader import DailySignal
import hashlib
import requests
from bs4 import BeautifulSoup
import os
import time
import json
import trader
from colorama import Fore
import redis
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



finvizFilters = [
    "https://finviz.com/screener.ashx?v=111&f=cap_microover,fa_curratio_o1.5,fa_estltgrowth_u10,fa_roe_o15,ta_beta_o1.5,ta_sma20_pa&ft=4",#Don't have an idea about what is it, just saw it on youtube
    "https://finviz.com/screener.ashx?v=111&f=fa_debteq_u1,fa_roe_o20,sh_avgvol_o100,ta_highlow50d_nh,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4&r=41"#same again,
    "https://finviz.com/screener.ashx?v=111&f=fa_debteq_u1,fa_roe_o20,sh_avgvol_o100,ta_highlow50d_nh,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4",#Again.

]

class MailingList():
	def __init__(self):
		self.MailingList= []
		self.host = "http://127.0.0.1:3000"
		self.p = "efeakaroz12345"
		
	def download(self,page=0):


		req =requests.post(f"{self.host}/secret/kentel/mailingL",headers={"User-Agent":"sagent"},data={"passpharase":self.p,"page":str(page)})
		out = json.loads(req.content)["m"]
		print(out)
		for o in out:
			self.MailingList.append(o)
		if len(out) != 0:
			self.download(page=page+1)

		else:
			self.writeOut()

	def writeOut(self):
		open("mailingList.json","w").write(json.dumps({"m":self.MailingList}))
# Run this 2 hours before the business hours.
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
#MailingList().download(page=0)
if __name__ == "__main__":

	lister = FinLister(finvizFilters[0])
	data = lister.fetch()
	stocks = lister.stocks
	notificationList = [] 
	for s in stocks:
		signal1,score1,cprice1,change1 ,warn = trader.DailySignal(s["ticker"])
		if score1<0.95:
			continue

		try:
			acc= float(r.get(s["ticker"]).decode())*100
			if acc < 74:
				continue
		except:
			acc = 0.0
		if signal1 == "BUY":
			#print(Fore.GREEN)

			#print(signal1,"  ",score1*100,"%  ",s["ticker"],"  ",acc)
			#print(Fore.RESET) 
			s["signal"] = signal1
			s["score"] = score1*100
			try:
				s["acc"] = acc
			except:
				s["acc"] = 0
			notificationList.append(s)
	emailHTMLStart = """
	<html lang="en">
	<head>
	<title>Here is your daily stock report </title>

	</head>
	<body>
	<a href="https://kentel.dev"><img src="https://kentel.dev/static/img/logo_.png"></a>
	<style>
	body{
	font-family: "Gill Sans", "Gill Sans MT", Calibri, sans-serif;
	font-size:23px;
	}
	</style>


	<p>Buy Signals From AI</p>

	"""

	for n in notificationList:
		emailHTMLStart += f"<details><summary>{n['ticker']} -  {n['signal']} {round(n['score'],2)}%</summary> <p>Price:{n['price']}, Comp:{n['company']}</p></details>"
		emailHTMLStart += "Kentel © 2023 All rights reserved. </body></html>"
		#print(emailHTMLStart)

		mailList= json.loads(open("mailingList.json","r").read())["m"]
		for m in mailList:
			m=m["email"]
			if "@" not in m:
				continue #In case of any errors in the mailing llist file.
			msg = MIMEMultipart()
			msg.set_unixfrom('author')
			msg['From'] = 'sales@kentel.dev'
			msg['To'] = m
			msg['Subject'] = 'Here is your daily stock report'
			message = emailHTMLStart
			msg.attach(MIMEText(message,"html"))

			mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
			mailserver.ehlo()
			mailserver.login('sales@kentel.dev', '****')

			mailserver.sendmail('sales@kentel.dev',m,msg.as_string())

			mailserver.quit()


