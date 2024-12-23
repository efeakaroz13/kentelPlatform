import json 
import pymongo 

mongo = pymongo.MongoClient("mongodb://efeakaroz13:****@185.235.77.16:27017")
db = mongo["KentelPlatform"]
issues = db["Issues"]


data = json.loads(open("managedData.json","r").read())
allKeys = list(data.keys())
newdata = {

}

issueTimes = {

}

allIssues = issues.find({})
for i in allIssues:
    timeit = i["time"]
    try:
        issueNumber = i["issueNumber"]
    except:
        continue
    issueTimes[str(issueNumber)] = timeit



for k1 in allKeys:
    newdata[k1] = []
    k1d= data[k1]
    for k2 in k1d:
        temp = []
        for k3 in k2:
            temp.append(issueTimes[str(k3)])
        newdata[k1].append(temp)

open("newdata.json","w").write(json.dumps(newdata,indent=4))
