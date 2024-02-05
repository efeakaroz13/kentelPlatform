
## This file is designed for the main server. Do not use it in a secondary one
import time
import os
import pymongo
import redis
from datetime import datetime

from app import base
import trader

mongo = pymongo.MongoClient()
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
		"time":["14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00"],
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




