'''
© Efe Akaroz 2023
This code is copyrighted, using it for profit may cause you legal issues
Agust 28th 2023

'''
import trader 
import json
import sys
import os
from multiprocessing import Process
import time
import redis
import pymongo
import random 

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


red = redis.Redis()
mongo = pymongo.MongoClient(host="mongodb://efeakaroz13:greenanarchist@185.235.77.16:27017")
db = mongo["KentelPlatform"]
issues = db["Issues"]





try:
    exchange = sys.argv[1]
    if exchange == "--help":
        print("InvestingGenius Command Line Help")
        print("command: python3 scanner.py {stockExchangeName(FTSE,NASDAQ,BIST,ASX)} {sessionID(optional)}")

except:
    print("Please provide exchange name(FTSE,BIST,ASX etc.)")
    exit()

try:
    exchanges = os.listdir("exchanges")
    if exchange not in exchanges and exchange != "scrapers":
        raise TypeError("a")
except:
    print("Couldn't find exchange data locally.")
try:
    sessionName = sys.argv[2]
except:
    sessionName = "output"

try:
    lastIssue = issues.find({"exchange":exchange})
    issueArray = []
    for i in lastIssue:
        issueArray.append(i)
    lastIssue = issueArray[-1]["issueNumber"]
except:
    lastIssue = 0

l1 = []
l2 = []
l3 = []
l4 = []

stockList = json.loads(open(f"exchanges/{exchange}/1.json","r").read())["list"]

c=1
for s in stockList:
    if c == 1:
        l1.append(s)
        c=2
        continue
    if c == 2:
        l2.append(s)
        c=3
        continue 
    if c == 3:
        l3.append(s)
        c=4
        continue
    if c == 4:
        l4.append(s)
        c=1
        continue

#Splitted the stock names for different worker processes in multi tasking

def task(tickers,workerID):
    outputData = []

    for t in tickers:
        #UPDATE Accuracy score globally
        try:
            acc = float(red.get(t).decode())*100
        except:
            acc = 0
        #Signals: BUY SELL, score: 0-1, price: float
        try:
            signal,score,price,change,warn = trader.DailySignal(t)
            score = score*100
            data = {
                "ticker":t,
                "score":score,
                "price":price,
                "signal":signal,
                "acc":acc,
                "change":change,
                "warning":warn

            }
            if signal == "BUY" and score>97:

                outputData.append(data)

        except:
            time.sleep(3)
            try:
                signal,score,price,change,warn  = trader.DailySignal(t)
                score = score*100
                data = {
                    "ticker":t,
                    "score":score,
                    "price":price,
                    "signal":signal,
                    "acc":acc,
                    "change":change,
                    "warning":warn
                }
                if signal == "BUY" and score>97:

                    outputData.append(data)
            except Exception as e :
                print(e)
    open(f"temp/{sessionName}{workerID}.json","w").write(json.dumps({"out":outputData},indent=4))

def filters():

    os.system("/home/efeakaroz13/kentelPlatform/env/bin/python3 filterBG.py")

if __name__ == "__main__":
    p1 = Process(target=task,args=(l1,"1"))
    p2 = Process(target=task,args=(l2,"2"))
    p3 = Process(target=task,args=(l3,"3"))
    p4 = Process(target=task,args=(l4,"4"))
    p5 = Process(target=filters)
    

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    finals = []
    ## Compose it all together
    t1 = json.loads(open(f"temp/{sessionName}1.json","r").read())
    t2 = json.loads(open(f"temp/{sessionName}2.json","r").read())
    t3 = json.loads(open(f"temp/{sessionName}3.json","r").read())
    t4 = json.loads(open(f"temp/{sessionName}4.json","r").read())
    for t in t1["out"]:
        finals.append(t)
    for t in t2["out"]:
        finals.append(t)
    for t in t3["out"]:
        finals.append(t)
    for t in t4["out"]:
        finals.append(t)

    
    for i in range(1,5):
        os.system(f"rm temp/{sessionName}{i}.json")
    finals.sort(key=lambda x: x["acc"])
    finals.reverse()
    allF = finals
    finals = finals[:20]
    finals.sort(key=lambda x: x["score"])
    
    issueData={
        "_id":generate_id(20),
        "issueNumber":lastIssue+1,
        "stockList":finals,
        "exchange":exchange,
        "time":time.time(),
        "scannerVersion":1,
        "allF":allF
    }
    issues.insert_one(issueData)
    open(f"temp/{sessionName}.json","w").write(json.dumps({"out":finals},indent=4))


    





