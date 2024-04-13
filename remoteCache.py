import redis 
import pymongo 
import json
import time
from multiprocessing import Process


red = redis.Redis()


client = pymongo.MongoClient(host="mongodb://efeakaroz13:greenanarchist@45.155.124.85/") # server.local_bind_port is assigned local port

dbS = client["KentelPlatform"]
issues = dbS["Issues"]
filters = dbS["filters"]

def p1():
    print("Process1 Started")
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

        try:
            fils = filters.find({})

            f = []
            for _ in fils:
                f.append(_)


            red.set("filters",json.dumps(f))
        except Exception as e:
            print(e) 



        time.sleep(200)

def p2():
    print("Process2 Started")
    while True:
        try:
            issueToReturn = issues.find({"exchange": "NASDAQ"})
            issueToReturn_ = []
            for i in issueToReturn:
                issueToReturn_.append(i)
            issueToReturn_.reverse()

            issueToReturn = issueToReturn_[:100]
            red.set("archiveStock",json.dumps(issueToReturn))
        except Exception as e:
            print(e) 

        time.sleep(259200)


if __name__ == "__main__":
    oneP = Process(target=p1)
    secondP = Process(target=p2)
    oneP.start()
    secondP.start()
    oneP.join()
    secondP.join()
