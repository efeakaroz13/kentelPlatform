## Author: Efe Akaroz
## This code belongs to Kentel LTD 


from filters import FinLister
import pymongo
import time 
mongo = pymongo.MongoClient()
db = mongo["KentelPlatform"]
filters= db["filters"]
while True:
    for f in filters.find({}):

        recurring = f["recurring"]

        if recurring == "1H" and time.time()-f["lastUpdate"]>1200:

            fin = FinLister(f["url"])
            fin.fetch()
            stocks = fin.stocks 
            filters.update_one({"_id":f["_id"]},{"$set":{"items":stocks,"lastUpdate":time.time()}})
        if recurring == "once" and time.time()-f["lastUpdate"]>15552000:
            fin = FinLister(f["url"])
            fin.fetch()
            stocks = fin.stocks 
            filters.update_one({"_id":f["_id"]},{"$set":{"items":stocks,"lastUpdate":time.time()}})
    time.sleep(50)


        


