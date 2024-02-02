'''
© Efe Akaroz 2024
This code is copyrighted, using it for profit may cause you legal issues

'''
#Note try to add a feature for adding previous 5 candles as parameters for increasing the accuracy

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


def DailyExperimentalSignal(ticker_name):
    ## DID NOT WORK QUITE LIKE I EXPECTED
    ## REASON: Couldnt set the volume accordingly

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

    
    startTime = time.time()
    
    
    try:
        model = joblib.load(f'models/{ticker_name}.daily.joblib')
        changesArray = []
        for i in range(-99,100):
            if i == 0:
                continue

            opoint5percent = lastDay
            opoint5percent["Close"]=float(lastDay["Close"])*(1+0.0005*i)
            opoint5percent["Open"]=float(lastDay["Open"])*(1+0.0005*i)
            opoint5percent["High"]=float(lastDay["High"])*(1+0.0005*i)
            opoint5percent["Low"]=float(lastDay["Low"])*(1+0.0005*i)
            opoint5percent["Volume"]=float(lastDay["Volume"])*(1+0.0005*i)
            #print("========",0.5*i,"percent change======")
            #print(opoint5percent)
            out=model.predict_proba(opoint5percent.to_numpy())
            if max(out[0])>0.90:
                changesArray.append([opoint5percent,out[0]])
            #print("==================================")
        for c in changesArray:
            print("=========")
            print(c)
            print("=========")

        output = model.predict_proba(lastDay.to_numpy())


        #output[0][1] -> Sell signal
        #output[0][0] -> Buy signal
        print(output[0])
        score = max(output[0])
        outputStr = model.predict(lastDay.to_numpy())

    except Exception as e:
        print(e)
        
        inputData = data.drop(columns=['Signal'])
        outputData = data['Signal']
        x_train, x_test, y_train, y_test = train_test_split(inputData, outputData, test_size=0.1)

        #model = RandomForestClassifier(n_estimators=1500,min_samples_leaf=4)
        model = GradientBoostingClassifier(learning_rate=0.833,min_samples_leaf=35,min_samples_split=5,n_estimators=640)
        model.fit(x_train, y_train)
        predictions = model.predict(x_test)
        trainscore = accuracy_score(y_test, predictions)
        red.set(ticker_name,str(trainscore))


        joblib.dump(model,f'models/{ticker_name}.daily.joblib')
        output = model.predict_proba(lastDay.to_numpy())
        outputStr = model.predict(lastDay.to_numpy())
        
    endtime = time.time()
    score = max(output[0])
    return outputStr[0],score,cprice,0


def ExperimentalData(ticker_name):
    '''
        Will add the previous candle to the data to see how it will behave, this will come with beta, I am hopeful about it.
    '''
if __name__ == "__main__":
    print(DailyExperimentalSignal("AAPL"))
