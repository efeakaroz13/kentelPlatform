from trader import DailySignal
import time 
import redis
import json
from multiprocessing import Process
import os 
from extra import Mailer
import datetime

red= redis.Redis()



allIndexFunds = ["^NDX","^DJI"]
def p1():

    while True:
        today = datetime.datetime.today()
        day = today.weekday()
        marketClosedHours = [2,3,4,5,6,7,8]
        if day != 5 and day != 6 and today.hour not in marketClosedHours:

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
        else:
            time.sleep(2400)
def p2():
    #mailer
    oldScore = 0
    lastSent = 0
    time.sleep(5)
    
    while True:
        today = datetime.datetime.today()
        day = today.weekday()
        marketClosedHours = [2,3,4,5,6,7,8]
        if day != 5 and day != 6 and today.hour not in marketClosedHours:
            try:
                alarmEnabledPeople = json.loads(red.get("nasdaq100List"))["list"]
                print(alarmEnabledPeople)
            except Exception as e:

                alarmEnabledPeople = []
            try:
                ifd = json.loads(red.get("indexFunds"))[0]
                score = ifd["score"]
                signal = ifd["signal"]
            except:
                pass
            if score!= oldScore and score>98 and time.time()-lastSent>3600:
                #alarm situation
                mails = []
                for p in alarmEnabledPeople:
                    try:
                        m = json.loads(red.get(p))["email"]
                        mails.append(m)
                    except:
                        pass 
                for m in mails:
                    print(m)


                lastSent = time.time()

    


            oldScore = ifd["score"]

            time.sleep(40)
        else:
            time.sleep(2400)

if __name__ == "__main__":
    p_1 = Process(target=p1)
    p_2 = Process(target=p2)
    p_1.start()
    p_2.start()
    p_1.join()
    p_2.join()




    