
## This file is designed for the main server. Do not use it in a secondary one
import time
import os
import pymongo
import redis
from datetime import datetime
import trader

mongo = pymongo.MongoClient(host="mongodb://efeakaroz13:greenanarchist@45.155.124.85/")
db = mongo["KentelPlatform"]
users = db["Users"]
alarms = db["alarms"]
red = redis.Redis()
filters = []

try:
	os.listdir("models")
except:
	os.system("mkdir models")


tasks = {
	
	"scanner":{
		"days":[1,2,3,4,5],
		"time":["13:50","14:25","15:10","15:35","16:10","16:50","17:30","18:20","19:00","19:40","20:24","21:00"],
		"command":"/home/efeakaroz13/kentelPlatform/env/bin/python3 scanner.py NASDAQ output"
	},
	"maintenance":{
		"days":[6],
		"time":["10:30"],
		"command":"/home/efeakaroz13/kentelPlatform/env/bin/python3 maintenance.py"
	},
	"firstScanner":{
		"days":[7],
		"time":["9:30"],
		"command":"/home/efeakaroz13/kentelPlatform/env/bin/python3 scanner.py NASDAQ output"
	}
	


}

a= True
while a==True:
	t = list(tasks.keys())
	today = datetime.now()

	hour = today.hour
	minute = today.minute
	day  =today.weekday()+1
	stringify = f"{hour}:{minute}"
	for _ in t:
		task = tasks[_]
		if day in task["days"]:
			if stringify in task["time"]:
				os.system(task["command"])
		else:
			pass




