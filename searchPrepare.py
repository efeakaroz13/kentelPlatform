import json
import yfinance as yf

initdata = json.loads(open("exchanges/NASDAQ/1.json").read())["list"]
out = []
for i in initdata:
    try:
        comp = yf.Ticker(i)
        info = comp.info 
        compname = info["shortName"]
        ticker = i 
        try:
            country = info["country"]  
        except:
            country = ""      
        try:
            summary = info["longBusinessSummary"]
        except:
            summary = ""
        data = {
            "name":compname,
            "ticker":ticker,
            "country":country,
            "summary":summary
        }
        print(ticker)
        out.append(data)
    except Exception as e:
        print(e)

open("exchanges/search.json","w").write(json.dumps({"out":out},indent=4))
