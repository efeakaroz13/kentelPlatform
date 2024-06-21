#Efe akaroz @ 2023

import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymongo import MongoClient
import redis
import time

import json 


def generate_id(charNumber):
    alphabet = "thequickbrownfoxjumpedoverthelazydog"
    a = []
    for _ in alphabet:
        a.append(_)
    output = ""
    for i in range(charNumber):
        intorchar = random.randint(0,1)
        if intorchar == 1:
            #char
            selectedChar = random.choice(a)
            upperOrLower = random.randint(0,1)
            if upperOrLower == 1:
                selectedChar = selectedChar.upper()
            output += selectedChar

        if intorchar == 0:
            num = random.randint(0,9)
            num = str(num)
            output+=num

    return output

class Mailer:
    def code(code,email):
        emailHTMLStart= open("templates/email/code.html","r").read()
        emailHTMLStart = emailHTMLStart.replace("-code-",str(code))
        emailHTMLStart = emailHTMLStart.replace("-date-",time.ctime(time.time()))
        
        
        
        msg = MIMEMultipart()
        msg.set_unixfrom('author')
        msg['From'] = 'Kentel <sales@kentel.dev>'
        msg['To'] = email
        msg['Subject'] = 'Verify your email'
        message = emailHTMLStart
        msg.attach(MIMEText(message,"html"))

        mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
        mailserver.ehlo()
        mailserver.login('sales@kentel.dev', 'efeAkaroz123')

        mailserver.sendmail('sales@kentel.dev',email,msg.as_string())

        mailserver.quit()
        
        return True
    def sorryToSeeYouGo(udata):
        emailHTMLStart= open("templates/email/sorry.html","r").read()


        
        
        
        msg = MIMEMultipart()
        msg.set_unixfrom('author')
        msg['From'] = 'Kentel <sales@kentel.dev>'
        msg['To'] = udata["email"]
        msg['Subject'] = '😿 We are sorry to see you go :('
        message = emailHTMLStart
        msg.attach(MIMEText(message,"html"))

        mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
        mailserver.ehlo()
        mailserver.login('sales@kentel.dev', 'efeAkaroz123')

        mailserver.sendmail('sales@kentel.dev',udata["email"],msg.as_string())

        mailserver.quit()
        
        return True
    def recovery(url,email):
        emailHTMLStart= open("templates/email/recovery.html","r").read()
        emailHTMLStart = emailHTMLStart.replace("-url-",url)
        emailHTMLStart = emailHTMLStart.replace("-preview-","Account Recovery")
        
        
        
        msg = MIMEMultipart()
        msg.set_unixfrom('author')
        msg['From'] = 'Kentel <sales@kentel.dev>'
        msg['To'] = email
        msg['Subject'] = 'Account Recovery'
        message = emailHTMLStart
        msg.attach(MIMEText(message,"html"))

        mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
        mailserver.ehlo()
        mailserver.login('sales@kentel.dev', 'efeAkaroz123')

        mailserver.sendmail('sales@kentel.dev',email,msg.as_string())

        mailserver.quit()
        
        return True

    def profitmarginalMailingList(email):
        redirectID = generate_id(20)
        urlGen = f"https://profitmarginal.com/newsletterComplete/{redirectID}"
        data = {
            "email":email,
            "redirectID":redirectID,
            "time":time.time()

        }
        redis.Redis.set(redirectID+"profitmarginal",json.dumps(data,indent=4))
        html = open("email/profitmarginal.html","r").read().replace("-url-",url)
        msg = MIMEMultipart()
        msg.set_unixfrom('author')
        msg['From'] = 'Profit Marginal <sales@kentel.dev>'
        msg['To'] = email
        msg['Subject'] = 'Best Trading AI Tool - Verify Your Email'
        message = html
        msg.attach(MIMEText(message,"html"))

        mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
        mailserver.ehlo()
        mailserver.login('sales@kentel.dev', 'efeAkaroz123')

        mailserver.sendmail('sales@kentel.dev',email,msg.as_string())

        mailserver.quit()
        
        return True
    


if __name__ == "__main__":
    print(generate_id(25))
