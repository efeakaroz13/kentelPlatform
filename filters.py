import requests
from bs4 import BeautifulSoup

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
