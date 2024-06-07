import json 
import yfinance as yf
from flask import Flask,render_template,abort,Response
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import datetime
import random
import io
import matplotlib.pyplot as plt
from statistics import mean

data = json.loads(open("newdata.json","r").read())
allTickers = list(data.keys())
def datetime_to_float(d):

    epoch = datetime.datetime.utcfromtimestamp(0)
    total_seconds =  (d - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return total_seconds




def view(ticker):
    try:
        ld = data[ticker]
    except:
        return abort(404)
    oneYearData = yf.Ticker(ticker).history(period="1y",interval="1h")
    print(oneYearData)
    #oneYearData.index = pd.to_datetime(oneYearData["Datetime"], dayfirst=True)
    #plt.plot(oneYearData)
    x=[]#times
    y = []#close price
    x0 = []
    y0=[]
    for i,r in oneYearData.iterrows():
        i = i.tz_convert(None)
        close = r["Close"]
        time = datetime_to_float(i)
        x.append(time)
        y.append(close)
        print(close,time)

    counter = 0
    for _ in x:
        for d1 in ld:
            for d in d1:
                if abs(_-d)<3500:
                    x0.append(d)
                    y0.append(y[counter])


        counter+=1


    

    output = io.BytesIO()
    plt.plot(x, y,c="b",linewidth=0.5)
    # x0 = []
    # y0 = []
    # mdata = mean(y)
    # for d1 in ld:
    #     for d in d1:
    #         #axis.axvline(x=d)
    #         y0.append(mdata)
    #         x0.append(d)
    plt.scatter(x0, y0,)
            
    plt.show()




def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

for d in allTickers:
    print(d)
tickerSelected = input("SELECT TICKER:")
view(tickerSelected)
