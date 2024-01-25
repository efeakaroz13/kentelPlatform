import yfinance as yf
import json
import os
import time
import datetime

data=json.loads(open("logs/18thjan.json","r").read())
issues = data["issues"]
calculated = {
    
}

counter = -1
for i in issues:
    counter +=1
    if counter == 400:
        break
    if i["exchange"] == "BIST":
        continue
    stockList = i["stockList"]

    today = datetime.datetime.today()
    issueDate = datetime.datetime.fromtimestamp(i["time"])

    if (today-issueDate).days>21:
        thirtyDaysLater = issueDate + datetime.timedelta(days=20)
        totalChange = 0
        numberOfStocks= 0
        stockCounter =0
        for s in stockList:
            if s["ticker"] == "THRN" or s["ticker"] == "OSTK":
                continue
            price = s["price"]
            company = yf.Ticker(s["ticker"])
            try:
                priceData=company.history(start=issueDate.strftime("%Y-%m-%d"),end=thirtyDaysLater.strftime("%Y-%m-%d"))
                #lastPrice = priceData['Close'].iloc[-1]
                #for max:
                lastPrice = max(priceData["Close"])
                change = (lastPrice-price)*100/price

                totalChange+=change
                numberOfStocks+=1
                stockCounter+=1
            except :
                pass

            
        averageChange=round(totalChange/numberOfStocks,2)
        calculated[str(i["issueNumber"])]=averageChange
        print(f"Issue #{i['issueNumber']}@{i['exchange']} - ",averageChange,"%"," | ",stockCounter)
        open("stats.json","w").write(json.dumps(calculated,indent=4))
    else:
        pass

