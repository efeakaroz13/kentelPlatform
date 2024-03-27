# AN EFE AKAROZ PRODUCT
# UNDER THE COPYRIGHT OF KENTEL LTD
# USING THIS COMMERCIALLY WITHOUT THE PERMISSION OF KENTEL LTD MIGHT CAUSE LEGAL TROUBLES.
import requests
from bs4 import BeautifulSoup
import openai
import undetected_chromedriver as uc 
import asyncio
import bingAI
import string 
import redis
from colorama import Fore
import json 

red = redis.Redis()
printable = set(string.printable)
def upload(content,title,description):
    urlHandle = title.replace(" ","-")
    filter(lambda x: x in printable, urlHandle)
    print("https://kentel.dev/blog/"+urlHandle)
    headers = {
        "Cookie":"ref=https://kentel.dev/settings; allowCookies=1; e=efeakaroz13@gmail.com; p=d92d52be428710fe09ff2e5f8c8d7f15566aaf5b65894fb9dbf67cc432ffb3bb; email=efeakaroz13@gmail.com; password=72b76c04c4e4183c4357156569e3f0d6cc8d311528c2d064a411036c5275140e"
    }
    author= "Efe Akaröz"
    data = {
        "content":content,
        "title":title,
        "description":description,
        "mainImage":"https://kentel.dev/static/images/kentel_300x200.png",
        "url":urlHandle,
        "author":author,
        "category":"blog"
    }
    page = requests.post("https://kentel.dev/godmin/blog",headers=headers,data=data)



try:
    blogPending = json.loads(red.get("blogPending"))
except Exception as e:
    print(e)
    print("Upload titles in order to use the thing")
    exit()

"""
curl 'https://kentel.dev/godmin/blog' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: ref=https://kentel.dev/settings; allowCookies=1; e=efeakaroz13@gmail.com; p=d92d52be428710fe09ff2e5f8c8d7f15566aaf5b65894fb9dbf67cc432ffb3bb; email=efeakaroz13@gmail.com; password=72b76c04c4e4183c4357156569e3f0d6cc8d311528c2d064a411036c5275140e' \
  -H 'Referer: https://kentel.dev/godmin' \
  -H 'Sec-Fetch-Dest: document' \
  -H 'Sec-Fetch-Mode: navigate' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-User: ?1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"'"""

basePrompt = """We're Kentel, a stock market prediction company.Our website is kentel.dev . Our goal is to make technical analysis more accesible and allow people trade without any experience. Our platform has a free trial and they can get daily scans to their email. Our analysis shows that the recommended stocks by our AI is going 12.7% up every 2 weeks. Our platform is helping our users to achieve financial freedom with a tiny cost. Your job is to write a blog post that contains about 300 words and explain the topic and than convince the user to subscribe to Kentel for best trading opportunities. I will give you the topic, you will write a short description and write the description in a <a> tag with the id 'desc'  machine will automatically recognize and post it. Be convincing and warm as possible. Use quotes and don't add nothing else other than the content. Use HTML markup."""
summaryPrompt = "Hello, you are a article summeriser and you are writing SEO optimized web descriptions, your job is to summerize the text we will give with best keywords for search results. Don't add anything extra, just text and don't say anything extra other than the summary."
counter = 0
for t in blogPending:
    t = t["title"]
    print(Fore.YELLOW,"[INFO]",Fore.RESET," Generating {}".format(t))
    out = asyncio.run(bingAI.generate(basePrompt+" Topic:{}".format(t)))
    soup = BeautifulSoup(out,"html.parser")
    content = soup.text 
    print(Fore.YELLOW,"[INFO]",Fore.RESET," Generating Summary")
    summary = asyncio.run(bingAI.generate(summaryPrompt+" Text:{}".format(content)))

    print(Fore.YELLOW,"[INFO]",Fore.RESET," Uploading Article to Kentel.dev")
    upload(out,t,summary)
    blogPending.pop(0)
    red.set("blogPending",json.dumps(blogPending))
    print(Fore.GREEN,"[SCC]",Fore.GREEN," Upload Complete!")
    counter +=1
print(counter,"Articles Have been uploaded to Kentel.dev")







