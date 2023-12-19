#Kentel.dev with alpha logo on it
#16TH of dec
#Practice makes perfect.
from flask import Flask,render_template,request,redirect,send_file,make_response
import stripe
import os
import pymongo
import time
import redis
import hashlib
from user_agents import parse as uaparse
import random
from extra import generate_id,Mailer
import datetime


app = Flask(__name__)
mongo = pymongo.MongoClient()
db = mongo["KentelPlatform"]
users = db["Users"]
logs = db["logs"]
mode = "test"
base = "http://127.0.0.1:3000"

@app.route("/")
def index():
    email  =request.cookies.get("e")
    password = request.cookies.get("p")
    try:
        psha256 = haslib.sha256()
        psha256.update(password.encode())
        password =psha256.hexdigest()
        
        u = users.find({"email":email,"password":password})[0]
        return render_template("home.html",data=u)
    except:
        pass
    
    agent =uaparse(str(request.headers.get("User-Agent")))
    device = agent.device.family
    osinfo = agent.os.family
    data = {

        "device":str(device),
        "os":str(osinfo),
        "time":time.time(),
        "ipaddr":"127.0.0.1",
        "_id":generate_id(50)
    }
    if agent.is_bot == False:
        logs.insert_one(data)
    
    return render_template("index.html")

class Auth:
    @app.route("/signup",methods=["POST","GET"])
    def signup():
        if request.method == "POST":
            email = request.form.get("email")
            if '@' not in email or '.' not in email:
                return redirect("/signup?err=Email+not+valid")
            
            password =request.form.get("password")
            psha256 = haslib.sha256()
            psha256.update(password.encode())
            password = psha256.hexdigest()
            #hashing all passwords
            
            fullName = request.form.get("fullName")
            #giftCode = request.forrm.get("giftCode")
            data = {

                "email":email,
                "password":password,
                "fullName":fullName,
                "sentIssues":[],
                "openedIssues":[],
                "stripeScc":False,
                "giftCode":None
                "time":time.time(),
                "_id":generate_id(20)
            }

            expire_date = datetime.datetime.now()
            expire_date = expire_date + datetime.timedelta(days=120)
            
            response = make_response(redirect("/"))
            response.set_cookie("e",email,expires=expire_date)
            response.set_cookie("p",password,expires=expire_date)
            
            users.insert_one(data)
            return response
        else:
            err = request.args.get("err")
            return render_template("signup.html",err=err)


    @app.route("/login",methods=["POST","GET"])
    def login():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            p = hashlib.sha256()
            p.update(password.encode())
            password = p.hexdigest()

            try:
                u = users.find({"email":email,"password":password})[0]
            except:
                return redirect("/login?err=Couldn't sign you in!")
            response = make_response(redirect("/"))
            expire_date = datetime.datetime.now()
            expire_date = expire_date + datetime.timedelta(days=120)
            response.set_cookie("e",email,expires=expire_date)
            response.set_cookie("p",password,expires=expire_date)
            return response
        
            
        if request.method == "GET":
            err =request.form.get("err")
            return render_template("signup.html",err=err)
    @app.route("/forgot_password",methods=["POST","GET"])
    def forgotpassword():
        if request.method == "POST":
            email = request.form.get("email")
            response = make_response(redirect("/forgot_password/code"))
            response.set_cookie("e",email)
            return response
        return render_template("forgot_password.html",mode="email")

    @app.route("/forgot_password/code",methods=["POST","GET"])
    def forgotpasswordAPI():
        if request.method == "POST":
            email =request.cookies.get("e")
            codeForm = request.form.get("code")
            codeCookie = request.cookies.get("code")
            
        if request.method == "GET":
            email = request.cookies.get("e")
            if e == None:
                return redirect("/forgot_password")
            code= generate_id(6)
            Mailer.code(code,email)
            sh = hashlib.sha256()
            sh.update(str(code).encode())
           
            code = sh.hexdigest()
            response = make_response(make_response("forgot_password.html",mode="code",email=email))
            code = response.set_cookie("code",code)
            
            
            return response
            
class Policies:
    @app.route("/privacy-policy")
    def privacy_policy():
        return render_template("privacy.html")
    @app.route("/terms-and-conditions")
    def terms_and_conditions():
        return render_template("terms.html")
if __name__ == "__main__":
    app.run(debug=True,port=3000)
