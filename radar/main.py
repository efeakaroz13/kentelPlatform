import pymongo
import yfinance as yf
import time
import json
import datetime 

#CONFIGURATION
maxBeta = 1.6
minBeta = 0.6
minMarketCap = 500000000

def getNextItem(item,listItem):
    aboutToBreak = False 
    for l in listItem:
        if aboutToBreak==True :
            return l
        if l == item:
            aboutToBreak = True
def getPinpointData(ticker,timeepoch,issues):
    print(timeepoch)
    stockList = issues.find({"time":timeepoch})[0]["stockList"]
    for s in stockList:
        if s["ticker"] == ticker:
            return s
        
client = pymongo.MongoClient(host="mongodb://efeakaroz13:****@185.235.77.16:27017") 
db = client["KentelPlatform"]
issues = db["Issues"]
allIssues = []
counter = 0
for i in issues.find({"exchange":"NASDAQ"}).sort({"time":-1}):
    if counter == 100:
        break
    allIssues.append(i)
    counter +=1


allIssues.reverse()


consecutiveList = {

}

counter = 0
issueConseq = []
for i in allIssues:
    issueConseq.append(i["time"])

    stocks = i["stockList"]

    for s in stocks:
        ticker = s["ticker"]
        try:
            consecutiveList[ticker]
        except:
            consecutiveList[ticker] = []
        
        consecutiveList[ticker].append(i["time"])

consecutiveList2 = {

}

allConKeys= list(consecutiveList.keys())
for k in allConKeys:
    times = consecutiveList[k]
    locTime = []
    nextItemTemp=None 
    temp =[]
    old = 0
    for t in times:
        if nextItemTemp == t:
            
            locTime.append(t)
            # when consecutiveness happen.

        else:
            if len(locTime)>0:
                temp.append(locTime)
            locTime = []

        nextItem = getNextItem(t,issueConseq)
        nextItemTemp = nextItem
        old =t 
    consecutiveList2[k] = temp
con2Keys = list(consecutiveList2.keys())
consecutiveList3 = {

}
finalOut = {}
for c in con2Keys:
    data = consecutiveList2[c]
    out = []
    for d in data:
        if len(d)>9:
            out.append(d)
    try:
        consecutiveList3[c]
    except:
        if len(out)>0:
            consecutiveList3[c] = []
    if len(out)>0:
        tickerInfo = yf.Ticker(c).info 
        marketCap = tickerInfo["marketCap"]
        beta = tickerInfo["beta"]

        if marketCap>minMarketCap and beta>minBeta and beta<maxBeta:
            try:
                finalOut[c]
            except:
                finalOut[c] = []
            for o in out:
                seqStart = datetime.datetime.fromtimestamp(o[0])
                yesterday = seqStart - datetime.timedelta(days=2)
                tomorrow  = seqStart + datetime.timedelta(days=1)
                yesterday = yesterday.strftime("%Y-%m-%d")
                tomorrow = tomorrow.strftime("%Y-%m-%d")
                historicalData = yf.Ticker(c).history(start=yesterday,end=tomorrow,interval="1d").tail()
                high = (historicalData["High"].astype("float"))
                low = (historicalData["Low"].astype("float"))

                percentChange = round((round((high-low),2)/low)*100,2)
                if abs(percentChange.any())<4:
                    finalOut[c].append(o)

            consecutiveList3[c].append(out)

finalOutKeys = list(finalOut.keys())
finalOut2 = {

}
for f in finalOutKeys:
    data_ = finalOut[f]
    for data in data_:
        seqStart = data[0]
        seqEnd = data[-1]
        seqLen = len(data)
        out = {
            "startPrice":None,
            "endPrice":None,
            "length":seqLen,
            "startTime":seqStart,
            "endTime":seqEnd,
            "acc":0
        }
        startData = getPinpointData(f,seqStart,issues)
        endData = getPinpointData(f,seqEnd,issues)
        startPrice = startData["price"]
        endPrice = endData["price"]
        out["acc"] = startData["acc"]
        out["startPrice"] = startPrice
        out["endPrice"] = endPrice
        try:
            finalOut2[f]
        except:
            finalOut2[f] = []
        finalOut2[f].append(out) 

print(json.dumps(finalOut2,indent=4))
