import time
import os
import pymongo
import redis
from datetime import datetime
import trader

base = "https://kentel.dev"

red = redis.Redis()
filters = []

try:
    os.listdir("models")
except:
    os.system("mkdir models")


tasks = {
    "dailyInsight":{
        "days":[1,2,3,4,5],
        "time":["13:25"],
        "command":"/home/efeakaroz13/kentelPlatform/env/bin/python3 daily.py"
    },
}

a= True
while a==True:
    t = list(tasks.keys())
    today = datetime.now()

    hour = today.hour
    minute = today.minute
    if hour<10:
        hour = f"0{hour}"
    if minute<10:
        minute = f"0{minute}"
    day  =today.weekday()+1
    stringify = f"{hour}:{minute}"

    for _ in t:
        task = tasks[_]
        if day in task["days"]:
            if stringify in task["time"]:
                print(f"[{time.ctime(time.time())}] Command:{task['command']} is being executed.",flush=True)
                os.system(task["command"])
                print(f"[{time.ctime(time.time())}] Command:{task['command']} has been executed.",flush=True)
        else:
            pass
    time.sleep(24)



