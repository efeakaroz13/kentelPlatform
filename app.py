#Kentel.dev with alpha logo on it
#16TH of dec
#Practice makes perfect.
from flask import Flask,render_template,request,redirect,send_file,make_response,jsonify
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
filters = db["Filters"]
mode = "test"
base = "http://127.0.0.1:3000"
red = redis.Redis()

@app.route("/")
def index():
    email  =request.cookies.get("e")
    password = request.cookies.get("p")
    try:
        psha256 = haslib.sha256()
        psha256.update(password.encode())
        password =psha256.hexdigest()
        
        u = users.find({"email":email,"password":password})[0]
        if u["emailVerified"]:
            return render_template("home.html",data=u)
        else:
            return redirect("/verify/email")
    except:
        pass
    
    agent =uaparse(str(request.headers.get("User-Agent")))
    device = agent.device.family
    osinfo = agent.os.family

    referer = request.headers.get("Referer")
    try:
        acceptLang = request.headers.get("Accept-Language")
        acceptLang.split(";")[0].split(",")[0]
    except:
        acceptLang = None
    data = {

        "device":str(device),
        "os":str(osinfo),
        "time":time.time(),
        "ipaddr":request.environ.get('HTTP_X_REAL_IP', request.remote_addr),
        "host":request.headers.get("Host"),
        "_id":generate_id(50),
        "referer":referer,
        "language":acceptLang
    }
    try:
        l = logs.find({"ipaddr":request.environ.get('HTTP_X_REAL_IP', request.remote_addr)})[0]
        if l["time"]<time.time()-345600:
            pass 
        else:
            return render_template("index.html")
    except:
        pass 
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

            try:
                u_e = users.find({"email":email})[0]
            
                return redirect("/signup?err=There is an user signed up  with this email")
            except:
                pass
            
            password =request.form.get("password")
            psha256 = haslib.sha256()
            psha256.update(password.encode())
            password = psha256.hexdigest()
            #hashing all passwords
            plan = request.cookies.get("plan")
            fullName = request.form.get("fullName")
            #giftCode = request.forrm.get("giftCode")
            data = {

                "email":email,
                "password":password,
                "fullName":fullName,
                "sentIssues":[],
                "openedIssues":[],
                "stripeScc":False,
                "plan":plan,
                "giftCode":None,
                "emailVerified":False,
                "newbie":True,
                "beta":False,
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
            try:
                u = users.find({"email":email})[0]
            except:
                return render_template("forgot_password.html",mode="email",err="The user does not exist")
            
            response = make_response(redirect("/forgot_password/code"))
            response.set_cookie("e",email)
            return response
        return render_template("forgot_password.html",mode="email")

    @app.route("/forgot_password/code",methods=["POST","GET"])
    def forgotpasswordAPI():
        if request.method == "POST":
            email =request.cookies.get("e")
            password = request.form.get("password")
            codeForm = request.form.get("code")
            codeCookie = request.cookies.get("code")
            sha = hashlib.sha256()
            sha.update(codeForm.encode())
            codeForm = sha.hexdigest()
            
            if codeCookie == codeForm:
                psha = hashlib.sha256()
                psha.update(password.encode())
                password = psha.hexdigest()
            else:
                return render_template("forgot_password.html",mode="code", err="Code doesn't match the original.")
            try:
                u=users.find({"email":email})[0]
            except:
                return render_template("forgot_password.html",mode="code",err="There is no such user with the email given.")
            users.update_one({"_id":u["_id"]},{"$set":{"password":password}})
            return render_template("success.html",red="/login",msg="Your password has reset successfully")
            
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
    @app.route("/verify/email",methods=["POST","GET"])
    def verifyEmail():
        if request.method == "POST":
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            try:
                u = users.find({"email":email,"password":password})[0]
            except:
                return redirect("/login")

            codeForm = request.form.get("code")
            codeRedis = red.get(email+"_code").decode()
            if codeForm == codeRedis:
                #code verified
                u["emailVerified"] = True

                users.update_one({"_id":u["_id"]},{"$set":u})
                return redirect("/")
            else:
                return render_template("verify.html",msg="Wrong Code.")
                #wrong code, or expired.
            
        if request.method == "GET":
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            try:
                u = users.find({"email":email,"password":password})[0]
            except:
                return redirect("/")
            if u["emailVerified"]:
                return redirect("/")
            verificationCode = random.randint(10000,100000)
            red.set(email+"_code",str(verificationCode),ex=600)
            Mailer.code(verificationCode,email)
            return render_template("verify.html")

    @app.route("/newbie/remove")
    def newbieRemove():
        email = request.cookies.get("e")
        password = request.cookies.get("p")
        try:
            u = users.find({"email":email,"password":password})[0]
        except:
            return redirect("/login")
        if u["newbie"]:
            users.update_one({"_id":u["_id"]},{"$set":{"newbie":False}})
        return redirect("/")
    
            
    




class APIs:
    @app.route("/api/login",methods=["POST"])
    def apiLogin():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            hashP = hashlib.sha256()
            hasP.update(password.encode())
            password=hashP.hexdigest()
            try:
                u = users.find({"email":email,"password":password})[0]
            except:
                return {"err":"Check your credentials."},401
            
            return u,200
        
    @app.route("/api/register",methods=["POST"])
    def apiRegister():
         if True:
            email = request.form.get("email")
            try:
                ue = users.find({"email":email})[0]
                return {"err":"This user already exists"},409
            except:
                pass
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
                "giftCode":None,
                "newbie":True,
                "emailVerified":False,
                "time":time.time(),
                "_id":generate_id(20)
            }
            users.insert_one(data)
            return data,200
    @app.route("/api/verify/email",methods=["POST","PUT"])
    def apiVerifyEmail():
        
        email = request.form.get("email")
        password = request.form.get("hash")
        try:
            u = users.find({"email":email,"password":password})[0]
        except:
            return {"err":"Verification Failed"},403
        if u["emailVerified"]:
            return {"err":"Email already verified"},401

        if request.method == "PUT":
            code = request.form.get("code")
            codeServer = red.get(email+"_code").decode()
            if code == codeServer:
                u["emailVerified"] = True              
                return {"msg":"Email verified"},200
            else:
                
                return {"err":"Codes does not match."},401
        
        verificationCode = random.randint(10000,100000)
        red.set(email+"_code",str(verificationCode),ex=600)
        Mailer.code(verificationCode,email)
        return {"msg":"Code sent"},200
    @app.route("/api/list/filters")
    def listFiltersAPI():
        f= []
        allFilters = filters.find({})
        for _ in allFilters:
            del _["_id"]
            f.append(_)
        
        return {"f":f}
    @app.route("/api/exchanges")
    def exchanges():
        return {"ex":["NASDAQ"]}

    @app.route("/set/cookie")
    def setcookieWithJS():
        f = request.args.get("redirect")
        if f != None:
            response = make_response(redirect(f))
        else:
            response = make_response({})
        key = request.args.get("key")
        value = request.args.get("value")
        exp = request.args.get("exp")
        if exp == None:
            exp = "365"
        try:
            exp = int(exp)
        except:
            return {"err":"expire invalid."}
        expire_date = datetime.datetime.now()
        expire_date = expire_date + datetime.timedelta(days=exp)
        response.set_cookie(key,value,expires=expire_date)

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
