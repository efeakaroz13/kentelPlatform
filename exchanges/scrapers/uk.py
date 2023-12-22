#Author: Efe Akaroz, All rights reserved @2023
#Date:28th of Agust

import requests
from bs4 import BeautifulSoup
import json 

page = requests.get("http://www.stockchallenge.co.uk/ftse.php")

soup = BeautifulSoup(page.content,"html.parser")
allTr = soup.find_all("table")[0].find_all("tr")

output = []
for tr in allTr:
    try:
        allTd = tr.find_all("td")
        ticker = allTd[1].get_text()
        if len(ticker) > 1:
            output.append(ticker+".L")
            print(ticker)
        
    except:
        pass


open("../FTSE/1.json","w").write(json.dumps({"list":output},indent=4))
