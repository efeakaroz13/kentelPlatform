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
	"dailyInsight":{
		"days":[1,2,3,4,5],
		"time":["17:10"],
		"command":"python3 daily.py"
	},
	"alarms":{
		"days":[1,2,3,4,5],
		"time":["17:30","18:30","19:30","20:30","21:30","22:30"],
		"command":"python3 alarms.py"
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




