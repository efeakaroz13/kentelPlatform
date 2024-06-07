import pymongo 
import json
import numpy as np
import matplotlib.pyplot as plt 

a =4

if a==1:
    tofilter = ["CSTR","SILK","SOLO","NAUT","EMBC","FIXX","DOMO"]

    data = json.loads(open("hs.json").read())
    indData = {}
    for d in data:
        ticker = d["ticker"]
        if ticker in tofilter:
            try:
                indData[ticker]
            except:
                indData[ticker] = []
            indData[ticker].append(d["price"])
    for t in tofilter:

        x = indData[t]  # X-axis points
        y = []
        counterx = 0
        for i in indData[t]:
            y.append(counterx)
            counterx+=1
        fig, ax = plt.subplots()
        ax.plot(y, x, **{'color': 'lightsteelblue', 'marker': 'o'})

        plt.title(t)
        plt.show()
        

            

elif a==2:
    # total recommended model
    data = json.loads(open("hs.json").read())
    temp =[]
    tickerRecommendedData = {

    }
    issueC = 1

    for d in data:

        ticker = d["ticker"]
        issue = d["issue"]

        if issue == 1:
            pass 
        else:

            try:
                tickerRecommendedData[ticker]
            except:
                tickerRecommendedData[ticker] = 0

            if ticker in temp:
                tickerRecommendedData[ticker] +=1
            
            temp.append(ticker)



    courses = list(tickerRecommendedData.keys())
    values = list(tickerRecommendedData.values())
    fig = plt.figure()
    plt.bar(courses, values, color ='maroon', 
        width = 0.4)
    plt.show()
elif a == 3:
    #Sequence model
    data = json.loads(open("hs.json").read())
    allIssues = list(data.keys())
    temp = []
    counters = {

    }
    sequenceStart = {

    }
    highlyRecommended = []
    for i in allIssues:
        idata = data[i]

        i = data[i]
        
        if temp !=[]:
            for _ in i:
                ticker = _["ticker"]

                if ticker in temp:
                    try:
                        counters[ticker]+=1
                        
                    except:
                        counters[ticker]=1

                    try:
                        sequenceStart[ticker]
                    except:
                        sequenceStart[ticker] = []

                    try:
                        sequenceStart[ticker].append(_["issue"])
                    except:
                        pass
                        
        
        t2 = []
        for _ in i:
            t2.append(_["ticker"])
        temp = t2 
        acKeys = counters.keys()
        for k in acKeys:
            if k not in temp and counters[k]>3:
                try:
                    sq = sequenceStart[ticker]
                except:
                    sq = []
                highlyRecommended.append({"ticker":k,"occurence":counters[k],"times":sq})
    open("highlyRecommended.json","w").write(json.dumps(highlyRecommended,indent=4))
    a = json.dumps(highlyRecommended,indent=4)

elif a==4:
    highlyRecommended = json.loads(open("highlyRecommended.json","r").read())
    allTickers = highlyRecommended
    managedData = {

    }
    for t in allTickers:
        ticker = t["ticker"]
        occurance = t["occurence"]
        currentIssues= []
        times = t["times"]
        counter = 1
        temp = 0
        temp2 = []
        for t in times:
            
            if t == temp+1:
                counter+=1
                temp2.append(t)
            else:
                if counter > 10 :
                    currentIssues = temp2
                    
                counter = 1
                temp2 = [] 

            temp = t
        try:
            managedData[ticker]
        except:
            managedData[ticker]= []
        if currentIssues not in managedData[ticker]:
            managedData[ticker].append(currentIssues)
    open("managedData.json","w").write(json.dumps(managedData,indent=4))
        





else:
    mongo = pymongo.MongoClient("mongodb://efeakaroz13:greenanarchist@185.235.77.16:27017")
    db = mongo["KentelPlatform"]
    issues = db["Issues"]

    allIssues = issues.find({})
    counter =0 
    highScorers = {}
    for i in allIssues:
        try:
            i["issueNumber"]
        except:
            continue
        highScorers[str(i["issueNumber"])] = []
        try:
            allF = i["allF"]
        except:
            continue
        for f in allF:
            if f["acc"]>70 and f["signal"]=="BUY" and f["score"] >97:
                f["issue"]=i["issueNumber"]
                highScorers[str(i["issueNumber"])].append(f)
        
 

    print(len(highScorers))
    open("hs.json","w").write(json.dumps(highScorers))


