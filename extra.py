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
        red = redis.Redis()
        red.set(redirectID+"profitmarginal",json.dumps(data,indent=4))
        html = open("templates/email/profitmarginal.html","r").read().replace("-url-",urlGen)
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
    
    def profitmarginalMailingList_thx(email):
        
        html= f"""
            <!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6; margin: 0; padding: 0; background-color: #f8f9fa;">
    <div style="width: 100%; max-width: 600px; margin: 20px auto; background-color: #fff; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); overflow: hidden;">
        <div style="background-color: #28a745; color: #fff; padding: 20px; text-align: center;">
            <h1>Thank You for Subscribing!</h1>
        </div>
        <div style="padding: 20px;">
            <p>Dear Subscriber,</p>
            <p>
                Welcome to the <strong>Profit Marginal</strong> community! We're thrilled to have you on board. By subscribing to our newsletter, you've taken the first step towards gaining a competitive edge in the stock market.
            </p>
            <p>
                As a subscriber, you'll receive:
            </p>
            <ul>
                <li><strong>Weekly market insights</strong> to keep you informed about the latest trends.</li>
                <li><strong>Exclusive trading tips</strong> to help you make informed decisions.</li>
                <li>Early access to our <strong>cutting-edge AI-driven predictions</strong>.</li>
            </ul>
            <p>
                We're committed to providing you with the tools and knowledge you need to achieve <strong>financial success</strong>. Keep an eye on your inbox for our upcoming newsletters and updates.
            </p>
            <p>
                Thank you for trusting <strong>Profit Marginal</strong> as your go-to source for trading excellence. If you have any questions or feedback, feel free to <a href="mailto:support@profitmarginal.com" style="color: #28a745; text-decoration: none;">contact us</a>.
            </p>
            <p>
                Best Regards,<br>
                The <strong>Profit Marginal</strong> Team
            </p>
        </div>
        <div style="background-color: #f1f1f1; padding: 10px; text-align: center; font-size: 0.9em; color: #555;">
            <p>
                You received this email because you subscribed to our newsletter at <a href="https://www.profitmarginal.com" style="color: #28a745; text-decoration: none;">ProfitMarginal.com</a>. If you no longer wish to receive these emails, you can <a href="https://profitmarginal.com/unsubscribe?email={email}" style="color: #28a745; text-decoration: none;">unsubscribe here</a>.
            </p>
            <p>
                &copy; 2024 ProfitMarginal.com, All rights reserved.
            </p>
        </div>
    </div>
</body>
</html>

    

        """
        

        msg = MIMEMultipart()
        msg.set_unixfrom('author')
        msg['From'] = 'Profit Marginal <sales@kentel.dev>'
        msg['To'] = email
        msg['Subject'] = 'Thank you! - Profit Marginal'
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
