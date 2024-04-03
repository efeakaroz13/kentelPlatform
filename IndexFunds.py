from trader import DailySignal
import time 
import redis
import json
red= redis.Redis()



allIndexFunds = ["^NDX","^DJI"]
while True:
    funds = []
    for i in allIndexFunds:
        try:
            s,sc,cprice,_ = DailySignal(i)
            acc = round(float(red.get(i).decode())*100,1)
            print(i,s,round(sc*100,2),f"{round(cprice,2)}$",acc)

            data = {
                "index":i,
                "signal":s,
                "score":round(sc*100,1),
                "acc":acc,
                
            }
            funds.append(data)
            
        except:
            pass
    red.set("indexFunds",json.dumps(funds))
    time.sleep(100)

    