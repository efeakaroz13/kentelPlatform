#Efe akaroz @ 2023

import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymongo import MongoClient
import redis
import time


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
        msg['From'] = 'sales@kentel.dev'
        msg['To'] = email
        msg['Subject'] = 'Here is your verification code! - Kentel'
        message = emailHTMLStart
        msg.attach(MIMEText(message,"html"))

        mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
        mailserver.ehlo()
        mailserver.login('sales@kentel.dev', 'greenanarchist')

        mailserver.sendmail('sales@kentel.dev',email,msg.as_string())

        mailserver.quit()
        
        return True

if __name__ == "__main__":
    print(generate_id(25))
