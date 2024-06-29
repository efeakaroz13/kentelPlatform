import pymongo 
import time
client = pymongo.MongoClient() # server.local_bind_port is assigned local port

db = client["KentelPlatform"]
users = db["Users"]
allU = []
for u in users.find({}):
    print(u["giftCode"],time.ctime(u["time"]))
