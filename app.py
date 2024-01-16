#Kentel.dev with alpha logo on it
#16TH of dec
#Practice makes perfect.
from flask import Flask,render_template,request,redirect,send_file,make_response,jsonify
import stripe
import os
import pymongo
import time
import stripe
import redis
import hashlib
from user_agents import parse as uaparse
import random
from extra import generate_id,Mailer
import datetime
import urllib.parse
import pprint
import json 
from flask_cors import CORS
import requests
import yfinance as yf
import trader

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mongo = pymongo.MongoClient()
db = mongo["KentelPlatform"]
users = db["Users"]
issues = db["issues"]
logs = db["logs"]
filters = db["Filters"]
portfolios = db["Portfolios"]
mode = "test"
base = "http://127.0.0.1:3000"
red = redis.Redis()

plans = ["standardM","basicM"]
stripe.api_key = "sk_test_51KNGcuEz0P2Wm1hTXPKe291k3qbGjhJqxaryuuNe2J0mSFhiZrI69LYIbWIAYIbGT3LYPOc4MyTAnkGmtleJobxh00LPcn5oI7"


@app.route("/")
def index():
    email  =request.cookies.get("e")
    password = request.cookies.get("p")
    try:

        
        u = users.find({"email":email,"password":password})[0]


        if u["emailVerified"]:
            if len(stripe.Subscription.list(customer=u["customer_id"])["data"]) == 0:
                return redirect("/checkout")
            else:
                if  stripe.Subscription.list(customer=u["customer_id"])["data"][0]["plan"]["active"]:
                    msg = request.args.get("msg")
                    return render_template("home.html",data=u,msg=msg,active="home",title="")
                else:
                    return redirect("/not_paid")
        else:
            return redirect("/verify/email")
    except Exception as e:
        print(e)
        
    
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
        err = request.args.get("err")

        plan = request.cookies.get("plan")
        if plan == None:
            return redirect("/")
        if plan not in plans:
            return redirect("/")
        planVisual = ""
        if plan == "basicM":
            planVisual = "Daily Insight"
        if plan == "standardM":
            planVisual = "Standard"

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
            psha256 = hashlib.sha256()
            psha256.update(password.encode())
            password = psha256.hexdigest()
            #hashing all passwords
            fullName = request.form.get("fullName")
            if fullName == None:
                return abort(403)
            cus = stripe.Customer.create(
              name=fullName,
              email=email
            )
            
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
                "_id":generate_id(20),
                "customer_id":cus["id"]
            }

            expire_date = datetime.datetime.now()
            expire_date = expire_date + datetime.timedelta(days=120)
            
            response = make_response(redirect("/"))
            response.set_cookie("e",email,expires=expire_date,secure=False,samesite="Lax")
            response.set_cookie("p",password,expires=expire_date,secure=False,samesite="Lax")
            
            users.insert_one(data)
            return response
        else:
            err = request.args.get("err")
            try:
                err = urllib.parse.unquote(err)
            except:
                err= None
            return render_template("signup.html",planVisual=planVisual,err=err)


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
                return redirect("/login?err=Check credentials")
            response = make_response(redirect("/"))
            expire_date = datetime.datetime.now()
            expire_date = expire_date + datetime.timedelta(days=120)
            response.set_cookie("e",email,expires=expire_date,secure=False,samesite="Lax")
            response.set_cookie("p",password,expires=expire_date,secure=False,samesite="Lax")
            return response
        
            
        if request.method == "GET":
            err =request.args.get("err")
            return render_template("login.html",err=err)
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
            try:
                codeRedis = red.get(email+"_code").decode()
            except:
                return redirect("/login")
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
            try:
                codeRedis = red.get(email+"_code").decode()
            except:
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
            psha256 = hashlib.sha256()
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
    

    @app.route("/api/ux/search")
    def searchRecommender():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
        except:
            return {},401
        query = request.args.get("q")
        if query == None:
            return {"out":[]}
        if len(query)<3:
            return {"out":[]}

        data = open("exchanges/search.json","r").read()
        data = json.loads(data)
        data = data["out"]
        out = []
        query = query.strip().lower()
        for d in data:
            concatted = d["ticker"].lower()+" "+d["name"].lower()
            if query in concatted:
                d["summary"] = d["summary"][:60]+"..."
                out.append(d)


        return {"out":out}
    @app.route("/api/ux/calculate/<ticker>")
    def calculateThis(ticker):
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
        except:
            return {},401
        try:
            signal,score,price,change = trader.DailySignal(ticker)
        except:
            return {"err":"There is an error on our side, AI not available."}
        try:
            acc = float(red.get(ticker).decode())*100
        except:
            acc = 0


        return {"signal":signal,"ticker":ticker,"price":price,"acc":acc,"score":score*100}
    @app.route("/api/v1/stockGraph/<ticker>")
    def stockGraphTicker(ticker):
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
        except:
            return {},401

        try:
            page = requests.get("https://query1.finance.yahoo.com/v8/finance/chart/"+ticker+"?region=US&lang=en-US&includePrePost=false&interval=15m&useYfid=true&range=5d&corsDomain=finance.yahoo.com&.tsrc=finance",headers={"User-Agent":"Mozilla Firefox Macintel"})
            data = json.loads(page.content)

            rd = []
            closes =  data["chart"]["result"][0]["indicators"]["quote"][0]["close"];
            timestamps =  data["chart"]["result"][0]["timestamp"];
            counter = 0
            for c in closes:
                rd.append({"x":timestamps[counter]*1000,"y":c})
                counter +=1
            try:
                compinfo = yf.Ticker(ticker).info
            except Exception as e:

                compinfo = {"e":str(e)}
            return {"out":rd,"compinfo":compinfo}
        except Exception as e:
            return {"e":str(e)}
class Policies:
    @app.route("/privacy-policy")
    def privacy_policy():
        return render_template("privacy.html")
    @app.route("/terms-and-conditions")
    def terms_and_conditions():
        return render_template("terms.html")


class StripeRoutes:
    @app.route("/checkout")
    def stripecheckout():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
            plan = u["plan"]

        except:
            return redirect("/")
        if plan == "standardM":
            price_id = 'price_1OSLwuEz0P2Wm1hTxf5UXsGK'

            session = stripe.checkout.Session.create(
              success_url=base+'/checkout/success?session_id={CHECKOUT_SESSION_ID}',
              cancel_url=base+'/checkout/canceled',
              mode='subscription',
              line_items=[{
                'price': price_id,
                # For metered billing, do not pass quantity
                'quantity': 1
              }],
              customer=u["customer_id"]
              
            )

            # Redirect to the URL returned on the session


            return redirect(session.url, code=303)
        if plan == "basicM":

            price_id = 'price_1OSMSiEz0P2Wm1hTieKpwDBJ'

            session = stripe.checkout.Session.create(
              success_url=base+'/checkout/success?session_id={CHECKOUT_SESSION_ID}',
              cancel_url=base+'/checkout/canceled',
              mode='subscription',
              line_items=[{
                'price': price_id,
                # For metered billing, do not pass quantity
                'quantity': 1
              }],
              subscription_data={"trial_period_days":7},
              customer=u["customer_id"]
            )

            # Redirect to the URL returned on the session
            return redirect(session.url, code=303)
        #return {}
    @app.route("/checkout/success")
    def checkout_scc():
        session_id = request.args.get("session_id")
        try:
            session = stripe.checkout.Session.retrieve(session_id)
        except:
            return ("/")
        cus_id = session["customer"]

        try:
            
            activeq = stripe.Subscription.list(customer=cus_id)["data"][0]["plan"]["active"]
            if activeq != True:
                return redirect("/not_paid")
            else:

                u = users.find({"customer_id":cus_id})[0]
                email = u["email"]
                password = u["password"]
                response =  redirect("/")
                expire_date = datetime.datetime.now()
                expire_date = expire_date + datetime.timedelta(days=120)
                

                response.set_cookie("e",email,expires=expire_date,secure=False,samesite="Lax")
                response.set_cookie("p",password,expires=expire_date,secure=False,samesite="Lax")
                return response
        except:
            return redirect("/login")

    @app.route("/checkout/canceled")
    def checkout_cancel():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
            activeq = stripe.Subscription.list(customer=u["customer_id"])["data"][0]["plan"]["active"]
            if activeq != True:
                return redirect("/not_paid")

            return render_template("canceled.html",u=u)
        except:
            return redirect("/")
    @app.route("/check_paid")
    def checkpaidUser():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
        except:
            return {},403
        out = (len(stripe.Subscription.list(customer=u["customer_id"])["data"])==0)
        return {"paid":out},200

    @app.route("/not_paid")
    def not_paid():
        response = make_response("<script>alert('You did not make your payments, cant sign you in. Contact support -> efeakaroz@kentel.dev');window.location.assign('/')</script>")
        response.set_cookie("e","")
        response.set_cookie("p","")

        return response


class InstanceExchange:
    @app.route("/secret/kentel/mailingL",methods=["POST"])
    def mailingListSecretKentel():
        #50 items per page.
        #page 0: 0-50
        page = request.form.get("page")

        if page == None:
            page = 0
        try:
            page = int(page)
        except:
            page = 0 
        identity = request.headers.get("User-Agent")
        if identity == "sagent":
            pass 
        else:
            return abort(404)
        passpharase = request.form.get("passpharase")
        p = hashlib.sha256()
        p.update(passpharase.encode())
        passpharase = p.hexdigest()

        if passpharase == "1047f6357e92f30f4c947aec89da6ae9ac3e09b2cdc6b49a9a781f4de8ab4e97":
            #pass it trough
            mailingList = []
            basicUsers = users.find({"plan":"baicM"})
            standard = users.find({"plan":"standardM"})
            listEnd = (page+1)*50
            listStart = page*50

            for b in basicUsers:
                b= {
                            "email":b["email"],
                            "_id":b["_id"]
                }
                mailingList.append(b)
            for s in standard:
                try:
                    notPref = s["notPref"]
                    if notPref["dailyInsight"]:
                        s= {
                            "email":s["email"],
                            "_id":s["_id"]
                        }
                        mailingList.append(s)
                except:
                    s= {
                            "email":s["email"],
                            "_id":s["_id"]
                    }
                    mailingList.append(s)

            mailingList = mailingList[page*50:][:50]
            return {"m":mailingList}
        else:
            return abort(404)

    @app.route("/secret/kentel/issueUpload",methods=["POST"])
    def issueUploadThing():

        identity = request.headers.get("User-Agent")
        if identity == "sagent":
            pass 
        else:
            return abort(404)
        data= request.json
        passpharase = data["passpharase"]
        p = hashlib.sha256()
        p.update(passpharase.encode())
        passpharase = p.hexdigest()
        mailingList = []
        basicUsers = users.find({"plan":"baicM"})
        standard = users.find({"plan":"standardM"})
        listEnd = (page+1)*50
        listStart = page*50

        for b in basicUsers:
            b= {
                        "email":b["email"],
                        "_id":b["_id"]
            }
            mailingList.append(b)
        for s in standard:
            try:
                notPref = s["notPref"]
                if notPref["dailyInsight"]:
                    s= {
                        "email":s["email"],
                        "_id":s["_id"]
                    }
                    mailingList.append(s)
            except:
                s= {
                        "email":s["email"],
                        "_id":s["_id"]
                }
                mailingList.append(s)
        totalMails = len(mailingList)

        if passpharase == "1047f6357e92f30f4c947aec89da6ae9ac3e09b2cdc6b49a9a781f4de8ab4e97":
            try:
                d = data["d"]
                d["totalMails"] = totalMails
                d["openedMails"] = 0
                issues.insert_one(d)
                return {"scc":True},200
            except:
                return {"err":"d"},500
        return {"d":"Done"},200

class UXRoutes:
    @app.route("/notifications",methods=["POST","GET"])
    def notificationSettings():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u= users.find({"email":email,"password":password})[0]
        except:
            return redirect("/login") 
        try:
            notPref= u["notPref"]
        except:
            notPref = {
                "dailyInsight":True,
                "portfolioNotifications":False
            }
        if request.method == "POST":

            dailyInsight = request.form.get("dailyInsight")
            portfolioNotifications = request.form.get("portfolioNot")

            if dailyInsight == "on":
                dailyInsight = True
            if dailyInsight == "off":
                dailyInsight = False 
            if portfolioNotifications == "off":
                portfolioNotifications = False 
            if portfolioNotifications =="on":
                portfolioNotifications = True 
            nd = {
                "dailyInsight":dailyInsight,
                "portfolioNotifications":portfolioNotifications
            }
            users.update_one({"_id":u["_id"]},{"$set":{"notPref":nd}})
            return redirect("/notifications")
        return render_template("notifications.html",data=u,title="Notifications - ",active="notifications",prefs=notPref)

    @app.route("/stock/<ticker>")
    def stockView(ticker):

        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u= users.find({"email":email,"password":password})[0]
        except:
            return redirect("/login") 

        if u["plan"] == "basicM":
            try:
                remaining = int(red.get(f"search{u['_id']}"))
                remaining -=1
                red.set(f"search{u['_id']}",str(remaining))

            except:
                remaining = 14 
                red.set(f"search{u['_id']}",str(remaining),ex=54000)

        #Dailyscan with API and load graph

        return render_template("stock.html",ticker=ticker,data=u,title=f"{ticker} - ",active="home")


    @app.route("/portfolio")
    def portfolioView():
        try:
            email  =request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
        except:
            return redirect("/login")
        try:
            usrPort = portfolios.find({"_id":u["_id"]})[0]
        except:
            usrPort = {
                "_id":u["_id"],

                "items":[]
            }
        for i in usrPort["items"]:
            try:
                page = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&apikey=BLR59U0EOSMIDDTT&symbol=AAPL&interval=1min")
                data = json.loads(page.content)

                lastRefreshed = data["Meta Data"]["3. Last Refreshed"]
                price =float( data["Time Series (1min)"][lastRefreshed]["4. close"])
                i["lp"] = round((price-i["cost"])*i["shares"],2)
                i["lpPercent"] = round(i["lp"]*i["shares"]*100/(i["cost"]*i["shares"]),2)
            except Exception as e:

                print("[ERR] AlphaVantage API /portfolio/",e,flush=True)
                i["lp"]="*"
                i["lpPercent"] = "*"
        return render_template("portfolio.html",usrPort=usrPort,active="portfolio",title="Portfolio - ",data=u)
class Portfolio:
    @app.route("/api/add2port/<ticker>",methods=["GET"])
    def add2p(ticker):
        try:
            email =  request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
        except:
            return {},401

        quantity = request.args.get("quantity")
        fromPrice = request.args.get("fromPrice")
        if quantity == None or fromPrice == None:
            return {"err":"quantity&fromPrice"}
        try:
            quantity = int(quantity)
            fromPrice = float(fromPrice)
        except:
            return {"err":"needed int or double"},403
        update = False
        try:
            usrPort = portfolios.find({"_id":u["_id"]})[0]
            update=True
        except:
            usrPort = {
                "_id":u["_id"],

                "items":[]
            }

        tickerInItems = False 
        whereAt = 0
        counter = 0

        for i in usrPort["items"]:
            if ticker==i["ticker"]:
                tickerInItems= True
                whereAt = counter
                break
                counter +=1
        if tickerInItems:
            costData = usrPort["items"][whereAt]
        else:
            costData = {
                "cost":0,
                "shares":0,
                "ticker":ticker,
                "addedAt":time.time(),

            }
        if costData["shares"] == 0:
            costData["shares"] = quantity
            costData["cost"] = fromPrice
        else:
            oldCost = costData["cost"]
            oldShareNumber = costData["shares"]
            oldTotalCost = oldCost*oldShareNumber
            newTotalCost = quantity*fromPrice
            allTotalCost = oldTotalCost+newTotalCost
            totalShares = oldShareNumber["shares"]+quantity


            costData["cost"] = allTotalCost/totalShares
            costData["shares"] = totalShares
        if tickerInItems:
            usrPort["items"][whereAt] = costData

        else:
            usrPort["items"].append(costData)


        if update:
            portfolios.update_one({"_id":u["_id"]},{"$set":usrPort})
        else:
            portfolios.insert_one(usrPort)



        return costData,200
if __name__ == "__main__":
    app.run(debug=True,port=3000)
