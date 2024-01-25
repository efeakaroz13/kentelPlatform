import os
import json
import yfinance as yf
import datetime
import time
from matplotlib import pyplot as plt


allData = json.loads(open("logs/18thjan.json","r").read())
issues = allData["issues"]
issuesForScan = []
allDates = []
for i in issues:
    issueTime = i["time"]
    if i["exchange"] =="BIST":
        continue
    today = datetime.datetime.today()
    issueDate = datetime.datetime.fromtimestamp(i["time"])
    if (today-issueDate).days>15:
        if issueDate.strftime("%d-%m") not in allDates:
            issuesForScan.append(i)
            allDates.append(issueDate.strftime("%d-%m"))
bestPerformers = json.loads(open("changeFromOld.json","r").read())

for i in issuesForScan:
    issueDate = datetime.datetime.fromtimestamp(i["time"])
    thirtyDaysLater = issueDate + datetime.timedelta(days=14)
    print(issueDate)

    bf = bestPerformers[str(i["issueNumber"])]
    highP2B= 0
    twentyPercentPerformanceHighP2B=0
    ## This is to calculate how many of high p2b ratio stocks performed well after signals
    
    for f in i["allF"]:
        comp = yf.Ticker(f["ticker"])
        try:
            compinfo = comp.info
            priceData=comp.history(start=issueDate.strftime("%Y-%m-%d"),end=thirtyDaysLater.strftime("%Y-%m-%d"))
            price = f["price"]

            lastPrice = max(priceData["Close"])
        except:
            continue

        change = (lastPrice-price)*100/price


        try:
            p2b = compinfo["priceToBook"]
        except:
            continue
        if p2b>12:
            highP2B+=1
        cbf = {}


        if change>20 and p2b>12:
            twentyPercentPerformanceHighP2B+=1
    print(round(100*(twentyPercentPerformanceHighP2B/highP2B),2))


    
"""

performedMorethan10 = []
sectorsForGainers = []
marketCaps= []
priceToBooks = []
debtToEquities = []
numberGainers=0
bestPerformers = json.loads(open("changeFromOld.json","r").read())
for i in issuesForScan:
    print(i["issueNumber"],time.ctime(i["time"]))
    bf = bestPerformers[str(i["issueNumber"])]
    for b in bf:
        if b["localChange"]<25:
            continue

        numberGainers+=1
        comp = yf.Ticker(b["ticker"])
        infocomp= comp.info
        try:
            sectorsForGainers.append(infocomp["sectorDisp"])
        except:
            pass

        try:
            marketCaps.append(infocomp["marketCap"])
        except:
            pass

        try:
            priceToBooks.append(infocomp["priceToBook"])
        except:
            pass
        try:
            debtToEquities.append(infocomp["debtToEquity"])
        except:
            pass




sectorCounter = {}
for s in sectorsForGainers:
    try:
        sectorCounter[s] +=1
    except:
        sectorCounter[s]=1
sectorsList = []
valuesSector = []
for s in list(sectorCounter.keys()):
    sectorsList.append(s)
    valuesSector.append(sectorCounter[s])

print("Price To Book Ratio(Average):")
print(sum(priceToBooks)/len(priceToBooks))
print("Market Cap(Average):")
print(sum(marketCaps)/len(marketCaps))
print(sum(debtToEquities)/len(debtToEquities))

plt.plot(marketCaps)

plt.show()
"""

"""
for i in issuesForScan:
    issueDate = datetime.datetime.fromtimestamp(i["time"])
    thirtyDaysLater = issueDate + datetime.timedelta(days=14)

    allF= i["allF"]
    localBestPerformers = []
    for f in allF:
        if f["acc"]<73:
            continue
        try:

            company = yf.Ticker(f["ticker"])
            priceData=company.history(start=issueDate.strftime("%Y-%m-%d"),end=thirtyDaysLater.strftime("%Y-%m-%d"))
            price = f["price"]

            lastPrice = max(priceData["Close"])
        except Exception as e:
            continue
        #lastPrice = priceData['Close'].iloc[-1]
        #for max:
        
        change = (lastPrice-price)*100/price
        if change>12:
            f["localChange"] = change
            localBestPerformers.append(f)
    bestPerformers[i["issueNumber"]] = localBestPerformers

print(json.dumps(bestPerformers,indent=4))
"""



    
    

    
