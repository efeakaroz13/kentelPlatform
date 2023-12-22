import requests 
from bs4 import BeautifulSoup
import json 


output = []


exclude = ['SPGC', 'SRM', 'LQR', 'FTEL', 'MIRA', 'CTNT', 'HRYU', 'PXDT', 'PRZO', 'SRFM', 'ELWS', 'WRNT', 'TSBX', 'BGLC', 'APGE', 'SGMT', 'PWM', 'INTS', 'VTMX', 'FIHL', 'KGS', 'SVV', 'GENK', 'AZTR', 'BOF', 'CAVA', 'ATMU', 'ATS', 'CWD', 'SGE', 'SLRN', 'KVUE', 'TRNR', 'JYD', 'UCAR', 'WLGS', 'TCJH', 'TPET', 'GDTC', 'VCIG', 'GDHG', 'ARBB', 'ISPR', 'MGIH', 'MWG', 'HSHP', 'HKIT', 'SFWL', 'SYT', 'CHSN', 'HLP', 'ZJYL', 'YGF', 'BANL', 'CETY', 'MGRX', 'OMH', 'ICG', 'IZM', 'AESI', 'AIXI', 'BABY', 'BMR', 'NFTG', 'ENLT', 'MLYS', 'HSAI', 'LSDI', 'NXT', 'LICN', 'ASST', 'GPCR', 'BREA', 'TXO', 'GNLX', 'QSG', 'CVKD', 'MGOL', 'SKWD', 'ATLX', 'LIPO', 'RAYA', 'JEWL', 'ACRV', 'CMND', 'ATAT', 'ASPI', 'SNAL', 'MBLY', 'PRME', 'CTM', 'LASE', 'LPTV', 'KNW', 'CRBG', 'THRD', 'LNKB', 'YOSH', 'ATXG', 'HPCO']

def scrape(content):
    soup = BeautifulSoup(content,"html.parser")
    tickers = []
    primaryLinks = soup.find_all("a",{"class":"screener-link-primary"})
    for p in primaryLinks:
        tickers.append(p.get_text())

    return tickers 

firstPage = requests.get("https://finviz.com/screener.ashx?v=111&f=exch_nasd",headers={"User-Agent":"Mozilla Firefox"})
tickers = scrape(firstPage.content)
for t in tickers:
    output.append(t)

for i in range(1,200):
    pageNum = i*20+1 
    page = requests.get(f"https://finviz.com/screener.ashx?v=111&f=exch_nasd&r={pageNum}",headers={"User-Agent":"Mozilla Firefox"})
    tickers = scrape(page.content)
    for t in tickers:
        if t not in exclude:
            output.append(t)
data = {"list":output}
open("../NASDAQ/1.json","w").write(json.dumps(data,indent=4))


