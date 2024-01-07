'''
© Efe Akaroz 2023
This code is copyrighted, using it for profit may cause you legal issues

'''

import yfinance as yf
import pandas
import datetime
import datetime as dt
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os
import time
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
import joblib
import json 
import redis

red=redis.Redis()


def DailySignal(ticker_name):
    
    company = yf.Ticker(ticker_name)
    
    #currentPrice = company.info["currentPrice"]
    #previousClose = company.info["previousClose"]
    #change = round(((previousClose-currentPrice)/previousClose)*-100,2)
    #yfinance bug
    data = company.history(period='99y')
    data = data.reset_index()
    data = data.dropna()
    try:
        data = data.drop(columns=['Date'])
    except:
        pass
    try:
        data = data.drop(columns=['Dividends','Stock Splits'])
    except:
        pass

    lastDay = data.tail(1)
    cprice = lastDay.iloc[0]["Close"]
    
    allOpens = data["Open"]
    signals = []
    old = 0
    counter = 0
    for a in allOpens:
        try:
            next = allOpens[counter + 1]

            
            if next>a :
                signals.append('BUY')
            elif next<a :
                signals.append('SELL')

            
            else:
                signals.append("HOLD")

        except:
            signals.append("HOLD")
            continue
        counter += 1
        old = a
    data["Signal"] = signals
    
    data.drop(data[data['Signal'] == "HOLD"].index, inplace=True)
    data = data.reset_index()
    data= data.drop(columns=['index'])
    data.to_csv('hello.csv')
    
    startTime = time.time()
    
    
    try:
        model = joblib.load(f'models/{ticker_name}.daily.joblib')
        output = model.predict_proba(lastDay.to_numpy())
        score = max(output[0])
        outputStr = model.predict(lastDay.to_numpy())
    except:
        
        inputData = data.drop(columns=['Signal'])
        outputData = data['Signal']
        x_train, x_test, y_train, y_test = train_test_split(inputData, outputData, test_size=0.1)

        #model = RandomForestClassifier(n_estimators=1500,min_samples_leaf=4)
        model = GradientBoostingClassifier(learning_rate=0.833,min_samples_leaf=35,min_samples_split=5,n_estimators=640)
        model.fit(x_train, y_train)
        predictions = model.predict(x_test)
        trainscore = accuracy_score(y_test, predictions)
        red.set(ticker_name,str(trainscore))
        print("TRAINING:",ticker_name,trainscore)

        joblib.dump(model,f'models/{ticker_name}.daily.joblib')
        output = model.predict_proba(lastDay.to_numpy())
        outputStr = model.predict(lastDay.to_numpy())
        
    endtime = time.time()
    score = max(output[0])
    return outputStr[0],score,cprice,0#change
    #yfinance


if __name__ == "__main__":
    print(DailySignal("AAPL"))
