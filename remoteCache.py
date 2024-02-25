import redis 
import pymongo 
import json
import time



red = redis.Redis()


client = pymongo.MongoClient(host="mongodb://efeakaroz13:greenanarchist@160.20.108.219/") # server.local_bind_port is assigned local port

dbS = client["KentelPlatform"]
issues = dbS["Issues"]
filters = dbS["Filters"]

while True:
    try:
        i = issues.find({"exchange":"NASDAQ"})
        allIssuesArray = []
        for _ in i:
            allIssuesArray.append(_)
        
        #del allIssuesArray[-1]["allF"] removed for filtering with caching
        d= allIssuesArray[-1]
        red.set("NASDAQ",json.dumps(d))
    except Exception as e:
        print(e)
    try:
        issueToReturn = issues.find({"exchange": "SERVER2_DAILY_NASDAQ"})
        issueToReturn_ = []
        for i in issueToReturn:
            issueToReturn_.append(i)
        issueToReturn = issueToReturn_[-1]
        red.set("SERVER2_DAILY_NASDAQ",json.dumps(issueToReturn))
    except Exception as e:
        print(e)
    time.sleep(30)