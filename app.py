#Kentel.dev with alpha logo on it
#16TH of dec
#Practice makes perfect.
from flask import Flask,render_template,request,redirect,send_file,make_response,jsonify,abort
import stripe
import os
import pymongo
import time
import stripe
import redis
import hashlib
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
from filters import FinLister
import pymongo
import pprint
import socket


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
issues = None
filters = None

if ip_address !="185.235.77.16":


    client = pymongo.MongoClient(host="mongodb://efeakaroz13:greenanarchist@185.235.77.16:27017") # server.local_bind_port is assigned local port

    dbS = client["KentelPlatform"]
    issues = dbS["Issues"]
    filters = dbS["filters"]

## TODO
## Make least amount of database calls with redis


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mongo = pymongo.MongoClient()
db = mongo["KentelPlatform"]
profitMarginalDB = mongo["profitmarginal_com"]

if issues !=None:
    pass
else:
    issues = db["Issues"]
if filters != None:
    pass
else:
    filters = db["filters"]

users = db["Users"]

logs = db["logs"]

portfolios = db["Portfolios"]
forms = db["forms"]
admin = db["admin"]
blog = db["blog"]
pmMailingList = profitMarginalDB["mailingList"]
mode = "test"
base = "https://kentel.dev"
affiliates = db["affiliates"]
gifts = db["gifts"]
red = redis.Redis()

plans = ["standardM","basicM"]
stripe.api_key = "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"


@app.route("/")
def index():
    email  =request.cookies.get("e")
    password = request.cookies.get("p")
    try:


        try:
            u = json.loads(red.get(email))

            if u["password"] == password:
                pass
            else:
                return redirect("/login?err=Check your credentials")
        except:

            u = users.find({"email":email,"password":password})[0]
            red.set(u["_id"],json.dumps(u))
            red.set(u["email"],json.dumps(u))



        if u["plan"] == "basicM":
            """
            today = datetime.datetime.today()
            day = datetime.datetime(today.year,today.month,today.day)

            try:
                issueFind = issues.find({"time":{"$gt":day.timestamp()},"exchange":"NASDAQ"})[0]
            except:
                issueFind = None
            """
            #The opening scan of the day, but I prefered to load the last at the opening of the stock market
            #14.30 in UTC
            """
                                                try:

                                                    issueToReturn = issues.find({"exchange":"SERVER2_DAILY_NASDAQ"})[-1]
                                                except:
                                                    issueToReturn = None """

        if u["emailVerified"]:
            if u["giftCode"]:
                #do this for gifted:
                msg = request.args.get("msg")
                try:
                    filtersList = json.loads(red.get("filters"))
                except:
                    filtersList = filters.find({})
                return render_template("home.html",data=u,msg=msg,active="home",title="",filters=filtersList)
            else:
                cusid = u["customer_id"]
                ut = u["time"]
                hasPassed = time.time()-ut
                try:
                    req = json.loads(red.get(cusid))
                except:

                    req = stripe.Subscription.list(customer=u["customer_id"])["data"]
                    if hasPassed>=86400*14:
                        red.set(cusid,json.dumps(req),ex=86400)


                if len(req) == 0:
                    return redirect("/checkout")
                else:
                    if  req[0]["plan"]["active"]:
                        msg = request.args.get("msg")
                        filtersList = filters.find({})
                        return render_template("home.html",data=u,msg=msg,active="home",title="",filters=filtersList)
                    else:
                        return redirect("/not_paid")
        else:
            return redirect("/verify/email")
    except Exception as e:
        print(e)


    # agent =uaparse(str(request.headers.get("User-Agent")))
    # device = agent.device.family
    # osinfo = agent.os.family

    # referer = request.headers.get("Referer")
    # try:
    #     acceptLang = request.headers.get("Accept-Language")
    #     acceptLang.split(";")[0].split(",")[0]
    # except:
    #     acceptLang = None
    # data = {

    #     "device":str(device),
    #     "os":str(osinfo),
    #     "time":time.time(),
    #     "ipaddr":request.environ.get('HTTP_X_REAL_IP', request.remote_addr),
    #     "host":request.headers.get("Host"),
    #     "_id":generate_id(50),
    #     "referer":referer,
    #     "language":acceptLang
    # }
    # try:
    #     l = logs.find({"ipaddr":request.environ.get('HTTP_X_REAL_IP', request.remote_addr)})[0]
    #     if l["time"]<time.time()-345600:
    #         pass
    #     else:
    #         return render_template("index.html")
    # except:
    #     pass
    # if agent.is_bot == False:
    #     logs.insert_one(data)

    response =  make_response(render_template("index.html"))
    ref=request.cookies.get("ref")
    if ref == None:
        ref= request.headers.get("Referer")
        if ref!=None:
            expire_date = datetime.datetime.now()
            expire_date = expire_date + datetime.timedelta(days=900)
            response.set_cookie("ref",ref,expires=expire_date)
            pass# set ref cookie.

    secfetch = request.headers.get("Sec-Fetch-Dest")
    if secfetch == "iframe":
        return render_template("iframe.html")
    return response


## for affiliates and following who is what
@app.route("/<url>")
def affiliateIndex(url):
    try:
        af = json.loads(red.get(f"affiliate_{url}"))
    except:
        try:
            af = affiliates.find({"_id":url})[0]
            red.set("affiliate_{}".format(url),json.dumps(af))
        except:
            return abort(404)
    response = make_response(redirect("/"))

    expire_date = datetime.datetime.now()
    expire_date = expire_date + datetime.timedelta(days=90)
    expire_date2 = expire_date + datetime.timedelta(days=900)
    ref= request.headers.get("Referer")
    if ref!= None:
        response.set_cookie("ref",ref,expires=expire_date2)
    response.set_cookie("af",url,expires=expire_date)
    return response
@app.route("/gift/<giftCode>")
def giftCodeCookieClaim(giftCode):
    try:
        g = gifts.find({"code":giftCode})[0]
    except:
        return abort(404)
    response = make_response(redirect("/"))
    response.set_cookie("gift",giftCode)
    return response


class Auth:
    @app.route("/signup",methods=["POST","GET"])
    def signup():
        err = request.args.get("err")

        plan = request.cookies.get("plan")
        if plan == None:
            return redirect("/#pricing")
        if plan not in plans:
            return redirect("/#pricing")
        planVisual = ""
        if plan == "basicM":
            planVisual = "Daily Insight"
        if plan == "standardM":
            planVisual = "Standard"

        if request.method == "POST":
            captchapid = request.cookies.get("pid")
            if captchapid == None:
                return redirect("/signup?err=Try to reload the page, if the error persists contact efeakaroz@kentel.dev")
            try:
                captchaPidData = json.loads(red.get(f"captcha_{captchapid}"))#for validating the answer and the PID
            except:
                return redirect("/#pricing")
            captchaAnswer = captchaPidData["answer"]


            gcaptcha = request.form.get("captcha")
            if gcaptcha == None or gcaptcha == "":
                return redirect("/signup?err=Solve+the+captcha")
            gcaptcha = gcaptcha.replace("\r","").replace(" ","").strip()
            try:
                gcaptcha = int(gcaptcha)
            except:
                return redirect("/signup?err=Captcha answer should be a number")

            if gcaptcha == captchaAnswer:
                #pass
                pass
            else:
                return redirect("/signup?err=Captcha answer is wrong, please try again ")


            if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
                ip = request.environ['REMOTE_ADDR']
            else:
                ip = request.environ['HTTP_X_FORWARDED_FOR']




            email = request.form.get("email")
            if email == None:
                return abort(404)
            email = email.strip().lower()

            if '@' not in email or '.' not in email:
                return redirect("/signup?err=Email+not+valid")
            try:
                forms.find({"reason":"unsubscribe","email":email})[0]
                return render_template("unsubscribedQuestion.html")
            except:
                pass

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


            cus = stripe.Customer.create(

              email=email
            )
            af= request.cookies.get("af") # affiliate, if there are
            if af:
                if len(af)>20:
                    af=None
            gift = request.cookies.get("gift")
            if gift == None:
                pass
            else:
                try:
                    g = gifts.find({"code":gift})[0]
                    if g["numPeople"]==0:
                        gift= None
                    else:
                        gifts.update_one({"code":gift},{"$set":{"numPeople":g["numPeople"]-1}})
                except:
                    gift = None

            ref = request.cookies.get("ref")

            #giftCode = request.forrm.get("giftCode")
            data = {

                "email":email,
                "password":password,

                "sentIssues":[],
                "openedIssues":[],
                "stripeScc":False,
                "plan":plan,
                "emailVerified":False,
                "newbie":True,
                "beta":False,
                "time":time.time(),
                "_id":generate_id(20),
                "customer_id":cus["id"],
                "af":af,
                "giftCode":gift,
                "ref":ref
            }

            expire_date = datetime.datetime.now()
            expire_date = expire_date + datetime.timedelta(days=120)

            response = make_response(redirect("/"))
            response.set_cookie("e",email,expires=expire_date,secure=False,samesite="Lax")
            response.set_cookie("p",password,expires=expire_date,secure=False,samesite="Lax")

            users.insert_one(data)
            red.set(data["email"],json.dumps(data))
            red.set(data["_id"],json.dumps(data))
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
            if email == None or password == None:
                return redirect("/login")
            email= email.strip().lower()
            p = hashlib.sha256()
            p.update(password.encode())
            password = p.hexdigest()

            try:
                try:
                    u = json.loads(red.get(email))
                    if u["password"] == password:
                        pass
                    else:
                        return redirect("/login?err=Check your credentials")
                except:

                    u = users.find({"email":email,"password":password})[0]
                    red.set(u["_id"],json.dumps(u))
                    red.set(u["email"],json.dumps(u))
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

    @app.route("/forgot-password",methods=["POST","GET"])
    def forgot_password():
        if request.method == "POST":
            email = request.form.get("email")

            try:
                ud = json.loads(red.get(email))
            except:
                try:
                    ud = users.find({"email":email})[0]
                except:
                    return redirect("/forgot-password?err=Couldn't find your account.")
            #send the recovery email
            pid = generate_id(20)
            red.set(f"recovery_{pid}",json.dumps(ud),ex=600)
            Mailer.recovery("https://kentel.dev/email/forgotpassword?pid="+pid,email)
            return redirect("/forgot-password?err=Email Sent for account recovery. Click on the link for deciding your new password. You have 10 minutes to reset your password.")
        if request.method == "GET":
            err = request.args.get("err")

            return render_template("forgotpassword.html",err=err)

    @app.route("/email/forgotpassword",methods=["POST","GET"])
    def emailForgotPassword():
        pid = request.args.get("pid")
        try:
            recoveryData = json.loads(red.get("recovery_"+pid))
        except:
            return abort(403)


        if request.method == "POST":
            password = request.form.get("password")
            p = hashlib.sha256()
            p.update(password.encode())
            p = p.hexdigest()
            recoveryData["password"] = p
            red.set(recoveryData["_id"],json.dumps(recoveryData))
            red.set(recoveryData["email"],json.dumps(recoveryData))
            users.update_one({"_id":recoveryData["_id"]},{"$set":{"password":p}})
            return redirect("/login?err=Password Successfully Updated. Sign in with your new password to continue")
        if request.method == "GET":
            return render_template("passwordReset.html")

    @app.route("/verify/email",methods=["POST","GET"])
    def verifyEmail():
        if request.method == "POST":
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            try:
                try:
                    u = json.loads(red.get(email))
                    if u["password"] == password:
                        pass
                    else:
                        return redirect("/login")
                except:

                    u = users.find({"email":email,"password":password})[0]
                    red.set(u["_id"],json.dumps(u))
                    red.set(u["email"],json.dumps(u))
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
                red.set(u["email"],json.dumps(u))
                red.set(u["_id"],json.dumps(u))
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
            try:
                u = json.loads(red.get(email))
                if u["password"] == password:
                    pass
                else:
                    return redirect("/login")
            except:

                u = users.find({"email":email,"password":password})[0]
                red.set(u["_id"],json.dumps(u))
                red.set(u["email"],json.dumps(u))
        except:
            return redirect("/login")
        if u["newbie"]:
            users.update_one({"_id":u["_id"]},{"$set":{"newbie":False}})
            u["newbie"] = False
            red.set(u["email"],json.dumps(u))
            red.set(u["_id"],json.dumps(u))
        return redirect("/")



class ErrorHandlers:
    @app.errorhandler(404)
    def page_not_found(e):
        return redirect("/")
    @app.errorhandler(500)
    def page_not_found(e):
        return render_template('500.html'), 500
    @app.errorhandler(403)
    def page_not_found(e):
        return render_template('403.html'), 403

class IssuesDifferentPackages:
    @app.route("/get/last/issue")
    def getLastIssue():
        try:
            email= request.cookies.get("e")
            password = request.cookies.get("p")
            try:
                u = json.loads(red.get(email))
                if u["password"] == password:
                    pass
                else:
                    return redirect("/login?err=Check your credentials")
            except:

                u = users.find({"email":email,"password":password})[0]
                red.set(u["_id"],json.dumps(u))
                red.set(u["email"],json.dumps(u))
        except:
            return redirect("/login")
        if u["plan"] == "standardM":
            print(u["plan"])
            filter_selected = request.args.get("filter")
            if filter_selected == None or filter_selected == "" or filter_selected == "undefinded" or filter_selected == "null" or filter_selected=="defno" or filter_selected=="def":
                try:
                    d = json.loads(red.get("NASDAQ"))
                    try:
                        del d["allF"]
                    except:
                        pass
                    return d
                except:
                    pass
                try:
                    i = issues.find({"exchange":"NASDAQ"})
                    allIssuesArray = []
                    for _ in i:
                        allIssuesArray.append(_)

                    del allIssuesArray[-1]["allF"]
                    return allIssuesArray[-1]
                    #return i

                except Exception as e:
                    print("['/get/last/issue']",e,flush=True)
                    return {"stockList":[]}
            else:
                try:
                    s_f = filters.find({"_id":filter_selected})[0]
                    items = s_f["items"]

                    try:
                        try:
                            sissue = json.loads(red.get("NASDAQ"))
                        except:
                            pass
                            i = issues.find({"exchange":"NASDAQ"})
                            allIssuesArray = []
                            for _ in i:
                                allIssuesArray.append(_)
                            sissue = allIssuesArray[-1]
                        seli = sissue["allF"] # selected issue for filtering

                        #return i

                    except Exception as e:
                        print("['/get/last/issue']",e,flush=True)
                        return {"stockList":[]}
                    filterItemsArray = []
                    for f in items:
                        filterItemsArray.append(f["ticker"])
                    output = []
                    for s in seli:
                        if s["acc"]>73 and s["score"]>97.5 and s["ticker"] in filterItemsArray:
                            #filter has passed.
                            output.append(s)

                    output.sort(key=lambda x:x["score"],reverse=True)
                    sissue["stockList"] = output
                    del sissue["allF"]
                    return sissue



                except Exception as e:
                    print("--- ",e)
                    try:
                        i = issues.find({"exchange":"NASDAQ"})
                        allIssuesArray = []
                        for _ in i:
                            allIssuesArray.append(_)

                        del allIssuesArray[-1]["allF"]
                        return allIssuesArray[-1]
                        #return i

                    except Exception as e:
                        print("['/get/last/issue']",e,flush=True)
                        return {"stockList":[]}
        elif u["plan"] == "basicM":
            try:
                d = json.loads(red.get("SERVER2_DAILY_NASDAQ"))
                return d
            except:
                pass
            try:

                issueToReturn = issues.find({"exchange": "SERVER2_DAILY_NASDAQ"})
                issueToReturn_ = []
                for i in issueToReturn:
                    issueToReturn_.append(i)
                issueToReturn = issueToReturn_[-1]
            except Exception as e:
                issueToReturn = {"e":str(e)}

            return issueToReturn
        else:
            return {"stockList":[]}


class Tutorials:
    @app.route("/tutorials")
    def tutorials():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            try:
                u = json.loads(red.get(email))
                if u["password"] == password:
                    pass
                else:
                    return redirect("/login")
            except:
                u = users.find({"email":email,"password":password})[0]
                red.set(u["email"],json.dumps(u))
                red.set(u["_id"],json.dumps(u))

        except:
            return redirect("/")
        return render_template("tutorials.html",active="tutorials",title="Tutorial Center - ",data=u)
class APIs:
    @app.route("/api/login",methods=["POST"])
    def apiLogin():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            hashP = hashlib.sha256()
            hashP.update(password.encode())
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
            try:
                data = json.loads(red.get(f"stockSignal_{ticker}"))
                return data
            except:
                pass
            signal,score,price,change,warn = trader.DailySignal(ticker)
        except:
            return {"err":"There is an error on our side, AI not available."}
        try:
            acc = float(red.get(ticker).decode())*100
        except:
            acc = 0


        data =  {"signal":signal,"ticker":ticker,"price":price,"acc":acc,"score":score*100,"warn":warn}
        red.set(f"stockSignal_{ticker}",json.dumps(data),ex=150)
        return data
    @app.route("/api/v1/stockGraph/<ticker>")
    def stockGraphTicker(ticker):
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
        except:
            return {},401

        try:
            try:
                data = json.loads(red.get(f"stockData_{ticker}"))
                return data
            except:
                pass
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

            data =  {"out":rd,"compinfo":compinfo}
            red.set(f"stockData_{ticker}",json.dumps(data),ex=360)
            return data,200
        except Exception as e:
            return {"e":str(e)}

    @app.route("/api/indexFunds")
    def indexFundsApi():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            try:
                u =  json.loads(red.get(email))
                if u["password"] != password:
                    return abort(403)
            except:
                u = users.find({"email":email,"password":password})[0]

        except:
            return abort(403)
        d = json.loads(red.get("indexFunds"))
        return d
class Policies:
    @app.route("/privacy-policy")
    def privacy_policy():
        return abort(404)
        return render_template("privacy.html")
    @app.route("/kentel-eula")
    def terms_and_conditions():
        return render_template("eula.html")


class StripeRoutes:
    @app.route("/checkout")
    def stripecheckout():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
            if u["giftCode"] != None:
                return redirect("/")
            plan = u["plan"]

        except:
            return redirect("/")
        if plan == "standardM":
            price_id = 'price_1OzgSUA7lNRXMlNssAE3SPfJ'

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
        if plan == "basicM":

            price_id = 'price_1OzgR9A7lNRXMlNsKMw0CKIP'

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
                orderid = session_id
                totalCost = "00.00"
                if u["plan"] == "standardM":
                    totalCost = "30.00"
                if u["plan"] == "basicM":
                    totalCost = "10.00"

                response =  make_response(render_template("success.html",orderid=orderid,totalCost=totalCost))
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
                try:
                    notf = b["notf"]
                    if notf == False:
                        continue
                    else:
                        pass


                except:
                    pass
                b= {
                    "email":b["email"],
                    "_id":b["_id"]
                }
                mailingList.append(b)
            for s in standard:
                try:
                    notf = s["notf"]
                    if notf == False:
                        continue
                    else:
                        pass

                except:
                    pass

                s= {
                        "email":s["email"],
                        "_id":s["_id"]
                }
                mailingList.append(s)

            mailingList = mailingList[page*50:][:50]
            return {"m":mailingList}
        else:
            return abort(404)



    @app.route("/secret/kentel/portfolioNotifier",methods=["POST"])
    def portfolioNotifierAPISecret():
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
        allPortfolios = portfolios.find({})
        notifiers = []
        for p in allPortfolios:
            pid = p["_id"]
            try:
                u = users.find({"_id":pid})[0]
            except:
                continue
            if u["plan"] == "standardM":
                uda = {
                    "email":u["email"],
                    "portfolioD":p
                }
                try:
                    if u["notPref"]["portfolioNotifications"]:
                        notifiers.append(uda)
                except:
                    pass

        passpharase = request.form.get("passpharase")
        p = hashlib.sha256()
        p.update(passpharase.encode())
        passpharase = p.hexdigest()

        if passpharase == "1047f6357e92f30f4c947aec89da6ae9ac3e09b2cdc6b49a9a781f4de8ab4e97":
            notifiers = notifiers[page*50:][:50]
            return {"n":notifiers}

        else:
            return {},403

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

        page = request.form.get("page")
        if page == None:
            page = 0
        else:
            try:
                page = int(page)
            except:
                page = 0
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
                print(d)
                return {"scc":True},200
            except Exception as e:
                print(e)
                return {"err":"d"},500
        return {"d":"Done"},200

class UXRoutes:
    @app.route("/notifications",methods=["POST","GET"])
    def notificationSettings():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            try:
                u = json.loads(red.get(email))
                if u["password"] == password:
                    pass
                else:
                    return redirect("/login")
            except:
                u= users.find({"email":email,"password":password})[0]
                red.set(u["email"],json.dumps(u))
                red.set(u["_id"],json.dumps(u))

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
            notfList = ["enabled","disabled"]
            notf = request.form.get("notf")
            nasdaq100 = request.form.get("nasdaq100")
            if nasdaq100 == None or nasdaq100 == "":
                pass
            elif nasdaq100=="enabled":
                try:
                    nasdaq100List= json.loads(red.get("nasdaq100List"))
                    nasdaq100List["list"]


                except:
                    nasdaq100List = {"list":[]}
                if u["_id"] not in nasdaq100List["list"]:
                    nasdaq100List["list"].append(u['_id'])

                red.set("nasdaq100List",json.dumps(nasdaq100List))

            if notf == "" or notf == None:
                return redirect("/notifications")
            if notf in notfList:
                pass
            else:
                return redirect("/")
            if notf  == "enabled":
                notf=True
            if notf == "disabled":
                notf = False

            users.update_one({"_id":u["_id"]},{"$set":{"dailyInsight":notf}})
            u["dailyInsight"] = notf
            red.set(u["email"],json.dumps(u))
            red.set(u["_id"],json.dumps(u))

            return redirect("/notifications?msg=Updated+prefrences")
        return render_template("notifications.html",data=u,title="Notifications - ",active="notifications",prefs=notPref)

    @app.route("/stock/<ticker>")
    def stockView(ticker):


        email = request.cookies.get("e")
        password = request.cookies.get("p")
        try:
            try:
                u = json.loads(red.get(email))
                if u["password"] == password:
                    pass
                else:
                    return redirect("/login?err=Check your credentials")
            except:

                u = users.find({"email":email,"password":password})[0]
                red.set(u["_id"],json.dumps(u))
                red.set(u["email"],json.dumps(u))
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



                price =yf.Ticker(i["ticker"]).info["currentPrice"]
                i["lp"] = round((price-i["cost"])*i["shares"],2)
                i["lpPercent"] = round(i["lp"]*i["shares"]*100/(i["cost"]*i["shares"]),2)
            except Exception as e:

                print("[ERR] AlphaVantage API /portfolio/",e,flush=True)
                i["lp"]="*"
                i["lpPercent"] = "*"
        return render_template("portfolio.html",usrPort=usrPort,active="portfolio",title="Portfolio - ",data=u)

    @app.route("/account")
    def account():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
            cus_id = u["customer_id"]
        except:
            return redirect("/login")
        if u["giftCode"]:
            status = True

        else:
            status = stripe.Subscription.list(customer=cus_id)["data"][0]["plan"]["active"]

        return render_template("account.html",data=u,active="account",title="Account - ",time=time,stripe_status=status)

    @app.route("/settings")
    def settingsUX():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            try:
                u = json.loads(red.get(email))
                if u["password"] == password:
                    pass
                else:
                    return redirect("/login?err=Check your credentials")
            except:

                u = users.find({"email":email,"password":password})[0]
                red.set(u["_id"],json.dumps(u))
                red.set(u["email"],json.dumps(u))
        except:
            return redirect("/")


        return render_template("settings.html",data=u,active="settings",time=time)
    @app.route("/logout")
    def logout():
        response  = make_response(redirect("/"))
        response.set_cookie("e","")
        response.set_cookie("p","")
        return response

    @app.route("/unsubscribe",methods=["POST","GET"])
    def unsubscribeRoute():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
        except:
            return redirect("/login")
        if request.method =="POST":
            reason = request.form.get("reason")
            explain = request.form.get("explain")
            data = {
                "_id":u["_id"],
                "type":"unsubscribe",
                "reason":reason,
                "explanation":explain,
                "usr":u,
                "email":u["email"]
            }
            forms.insert_one(data)
            stripe.Subscription.cancel(stripe.Subscription.list(customer=u["customer_id"])["data"][0]["id"])
            users.delete_one({"_id":u["_id"]})
            Mailer.sorryToSeeYouGo(u)
            return redirect("/")
        return render_template("unsubscribe.html",data=u,active="settings",time=time)

    @app.route("/notanewbie")
    def imnotanewbie():
        try:
            email = request.cookies.get("e")
            password =request.cookies.get("p")
            try:
                u = json.loads(red.get(email))
                if u["password"] == password:
                    pass
                else:
                    return redirect("/login")
            except:

                u = users.find({"email":email,"password":password})[0]
                red.set(u["_id"],json.dumps(u))
                red.set(u["email"],json.dumps(u))
        except:
            return redirect("/")
        users.update_one({"_id":u["_id"]},{"$set":{"newbie":False}})
        u["newbie"] = False
        red.set(u["_id"],json.dumps(u))
        red.set(u["email"],json.dumps(u))

        return redirect("/")

    @app.route("/upgradeplan")
    def upgradePlanPage():
        try:
            email=request.cookies.get("e")
            password = request.cookies.get("p")
            u = users.find({"email":email,"password":password})[0]
        except:
            return redirect("/login")
        if u["plan"] == "standardM":
            return redirect("/settings")
        if u["plan"] == "basicM":
            return render_template("upgradePlan.html",data=u,active="settings")
    @app.route("/upgrade-plan")
    def upgradePlan():

        try:
            email = request.cookies.get("e")
            password =request.cookies.get("p")
            u= users.find({"email":email,"password":password})[0]
        except:
            return redirect("/")
        if u["plan"] == "standardM":
            return redirect("/")
        if u["plan"] == "basicM":
            price_id = 'price_1OzgSUA7lNRXMlNssAE3SPfJ' # for standard.
            sub = stripe.Subscription.list(customer=u["customer_id"])["data"][0]["id"]

            mod = stripe.Subscription.modify(
                sub,
                items=[{"price": price_id}],
            )
            u["plan"]= "standardM"
            red.set(u["email"],json.dumps(u))
            red.set(u["_id"],json.dumps(u))
            users.update_one({"_id":u["_id"]},{"$set":{"plan":"standardM"}})
            return redirect("/settings")
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

class Admin:
    @app.route("/godmin",methods=["POST","GET"])
    def godmin():
        adminPrivillages =["filters","analytics","blog","AI"]
        err = request.args.get("err")
        try:
            email = request.cookies.get("email")
            password = request.cookies.get("password")
            ad = admin.find({"email":email,"password":password})[0]
            return render_template("godmin/home.html",ad=ad)
        except:
            pass
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")
            enc = hashlib.sha256()
            enc.update(password.encode())
            password = enc.hexdigest()
            try:
                ad = admin.find({"email":email,"password":password})[0]
            except:
                return redirect("/godmin?err=Incorrect+credentials")
            response = redirect("/godmin")
            response.set_cookie("email",email,max_age=31560000)
            response.set_cookie("password",password,max_age=31560000)
            return response

        return render_template("godmin/login.html",err=err)
    @app.route("/godmin/filters",methods=["POST","GET"])
    def godminFilters():
        try:
            email =request.cookies.get("email")
            password = request.cookies.get("password")
            ad = admin.find({"email":email,"password":password})[0]
            if "filters" in ad["privillages"]:
                pass
            else:
                return redirect("/godmin")
        except:
            return redirect("/godmin")
        if request.method == "POST":
            url = request.form.get("filterURL")
            recurring = request.form.get("recurring")
            label= request.form.get("label")
            status = request.form.get("status")
            fl = FinLister(url=url)
            fl.fetch()
            stocks = fl.stocks

            data = {
                "_id":generate_id(10),
                "recurring":recurring,
                "label":label,
                "status":status,
                "items":stocks,
                "lastUpdate":time.time(),
                "url":url
            }
            filters.insert_one(data)


            return redirect("/godmin/filters")


        allFilters = []
        for f in filters.find({}):
            allFilters.append(f)

        afDic = {

        }
        for f in allFilters:
            afDic[f['_id']] = f
        import json
        return render_template("godmin/filters.html",allFilters=allFilters,dic=json.dumps(afDic))


    @app.route("/godmin/filter/edit",methods=["POST"])
    def godmingfilterEdit():
        try:
            email = request.cookies.get("email")
            password = request.cookies.get("password")
            ad  = admin.find({"email":email,"password":password})[0]

        except:
            return redirect("/godmin")
        filterID = request.form.get("id")
        url = request.form.get("filterURL")
        recurring = request.form.get("recurring")
        label= request.form.get("label")
        status = request.form.get("status")
        fl = FinLister(url=url)
        fl.fetch()
        stocks = fl.stocks
        data = {

                "recurring":recurring,
                "label":label,
                "status":status,
                "items":stocks,
                "lastUpdate":time.time(),
                "url":url
        }
        try:
            filters.update_one({"_id":filterID},{"$set":data})
        except:
            data["_id"] = generate_id(20)
            filters.insert_one(data)
        return redirect("/godmin/filters")



    @app.route("/godmin/blog",methods=["POST","GET"])
    def godminBlog():
        try:
            email =request.cookies.get("email")
            password = request.cookies.get("password")
            ad = admin.find({"email":email,"password":password})[0]
        except:
            return redirect("/godmin")

        if request.method == "POST":
            content = request.form.get("content")# content in html form
            title = request.form.get("title")
            author = request.form.get("author")
            page_URL = request.form.get("url")
            mainImage = request.form.get("mainImage") # as URL
            description = request.form.get("description")
            category = request.form.get("category")
            filename = generate_id(30)+".html"
            if author == None or author == "":
                author = "Efe Akaröz"

            if content == None or len(content)<30 or title==None or mainImage==None:
                return redirect("/godmin/blog")

            if page_URL == None:
                page_URL = generate_id(13)
            try:
                blog.find({"_id":page_URL})[0]
                page_URL = generate_id(15)
            except:
                pass
            html = """
{% extends "blogs/base.html" %}
{% block body %}
"""+content+"""
{% endblock %}
            """
            open("templates/blogs/{}".format(filename),"w").write(html)
            data= {
                "time":time.time(),
                "author":author,
                "title":title,
                "content":content,
                "_id":page_URL,
                "mainImage":mainImage,
                "visible":True,
                "createdBy":ad["_id"],
                "fileName":filename,
                "category":category,
                "description":description

            }
            blog.insert_one(data)

            return data
        return render_template("godmin/blog.html")
    @app.route("/godmin/affiliates",methods=["GET","POST"])
    def affiliates():
        try:
            email =request.cookies.get("email")
            password = request.cookies.get("password")
            ad = admin.find({"email":email,"password":password})[0]
        except:
            return redirect("/godmin")

        if request.method == "POST":
            label = request.form.get("label")
            url = request.form.get("url")
            if url == None:
                url = ""
            url = url.strip()
            if len(url)<3:
                url = generate_id(6)
            data = {"_id":url,"at":time.time(),"label":label}
            red.set(f"affiliate_{url}",json.dumps(data))
            affiliates.insert_one(data)
            return redirect("/godmin/affiliates")
        af = []
        for a in affiliates.find({}):
            af.append(a)
        return render_template("godmin/affiliates.html",af=af)
    @app.route("/godmin/affiliates/<idaf>")
    def affiliateStatus(idaf):
        try:
            email =request.cookies.get("email")
            password = request.cookies.get("password")
            ad = admin.find({"email":email,"password":password})[0]
        except:
            return redirect("/godmin")

        try:
            afd = json.loads(redis.get(f"affiliate_{idaf}"))
        except:
            try:
                afd = affiliates.find({"_id":idaf})[0]
            except:
                return "Affiliate not found"
        usersWithAffiliates = users.find({"af":afd})
        uwaf = []
        standard = 0
        base = 0
        pro = 0
        allInvoices = []
        totalAmount = 0
        for u in usersWithAffiliates:
            ut = u["time"]
            if time.time()-ut>31536000:
                continue
            inv = stripe.Invoice.list(customer=u)["data"]
            for i in inv:
                amount = i["amount_paid"]
                allInvoices.append(amount/100)
                totalAmount += amount/100
            if u["plan"] == "standardM":
                standard+=1
            if u["plan"] == "proM":
                pro+=1
            if u["plan"] == "basicM":
                base +=1

            uwaf.append(u)
        totalRevenue = standard*60+base*15

        return render_template("godmin/affiliateInspector.html",afd=afd,u=uwaf,standard=standard,base=base,pro=pro,totalRevenue=totalAmount)
    @app.route("/godmin/gifts",methods=["POST","GET"])
    def godminGifts():
        try:
            email =request.cookies.get("email")
            password = request.cookies.get("password")
            ad = admin.find({"email":email,"password":password})[0]
        except:
            return redirect("/godmin")

        if request.method=="GET":
            allGifts = gifts.find({})
            return render_template("godmin/gift.html",ag=allGifts)
        if request.method == "POST":
            code = request.form.get("code")
            if code == None:
                code = ""
            code = code.strip()
            if len(code)<3:
                code = generate_id(10)
            numPeople = request.form.get("peopleNumber")
            if numPeople == None:
                numPeople = 1
            else:
                try:
                    numPeople = int(numPeople)
                except:
                    numPeople= 1
            if numPeople>10:
                numPeople = 10
            data = {
                "numPeople":numPeople,
                "code":code,
                "time":time.time()
            }
            gifts.insert_one(data)
            return redirect("/godmin/gifts")

class Blog:

    @app.route("/tutorials/<url>")
    def tutorialView(url):
        try:
            tutorial = blog.find({"_id":url,"category":"tutorial"})[0]
            filename = tutorial["fileName"]
            return render_template(f"blogs/{filename}")
        except:
            return abort(404)
    @app.route("/blog")
    def blogKentel():
        return render_template("blogView.html")

    @app.route("/api/blog/search")
    def blogSearchApi():
        q = request.args.get("q")
        if q == None:
            return abort(403)
        if len(q)<3:
            return {"err":"too short"},403
        q = q.lower().strip()

        allArticles = []
        for a in blog.find({"visible":True}):
            title = a["title"]
            content = a["content"]
            searchScore = 0
            if q in title.lower():
                searchScore +=1
            if q in content.lower():
                searchScore +=0.5
            a["score"] = searchScore
            print(searchScore)
            if searchScore>0:
                allArticles.append(a)
        allArticles.sort(key= lambda x:x["score"],reverse=True)
        allArticles = allArticles[:20]
        return {"out":allArticles}

    @app.route("/blog/<url>")
    def blogRender(url):

        try:
            try:
                b = blog.find({"_id":url+"\r"})[0]
            except:
                b = blog.find({"_id":url})[0]

            url = "https://kentel.dev/blog/"+url
            title = b["title"]
            description=b["description"]
            return render_template("blogs/"+b["fileName"],data=b,title=title,url=url,description=description)
        except Exception as e:
            print(f"[{time.time()}]",e,flush=True)
            return abort(404)
        return str(url)
class Public:
    @app.route("/about")
    def about():
        return render_template("about.html")
    @app.route("/faq")
    def faq():
        return render_template("faq.html")
    @app.route("/favicon.ico")
    def faviconIco():
        return send_file("static/images/favicon.ico",as_attachment=False)
    @app.route("/robots.txt")
    def robotsTXT():
        return send_file("other/robots.txt",as_attachment=False)
    @app.route("/sitemap.xml")
    def sitemap():
        return send_file("other/sitemap.xml",as_attachment=False)


class Archives:
    @app.route("/archive")
    def archiveViewer():
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            try:
                u = json.loads(red.get(email))
                if u["password"] != password:
                    return redirect("/login?err=Check your credentials")

            except:
                u = users.find({"email":email,"password":password})[0]


        except:
            return redirect("/login?err=You need to be logged in in order to view this page.")
        if u["plan"] != "standardM":
            return redirect("/")

        archiveStock = json.loads(red.get("archiveStock"))

        return render_template("archive.html",active="archive",data=u,title="Archive",archiveStock=archiveStock)
    @app.route("/archive/<issueNumber>")
    def archiveIssueViewer(issueNumber):
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            try:
                u = json.loads(red.get(email))
                if u["password"] != password:
                    return redirect("/login?err=Check your credentials")

            except:
                u = users.find({"email":email,"password":password})[0]


        except:
            return redirect("/login?err=You need to be logged in in order to view this page.")
        try:
            issueNumber = int(issueNumber)
        except:
            return redirect("/archive")

        archiveStock = json.loads(red.get("archiveStock"))

        issue = None
        for r in archiveStock:
            r["issueNumber"] = int(r["issueNumber"])
            if r["issueNumber"] == issueNumber:
                issue = r
                break
        if issue == None:
            return redirect("/archive")


        return render_template("archiveInd.html",data=u,active="archive",r=issue,round=round)
    @app.route("/archive/<issueNumber>/calculatePerformance")
    def archiveCalculatePerformance(issueNumber):
        try:
            email = request.cookies.get("e")
            password = request.cookies.get("p")
            try:
                u = json.loads(red.get(email))
                if u["password"] != password:
                    return redirect("/login?err=Check your credentials")

            except:
                u = users.find({"email":email,"password":password})[0]


        except:
            return redirect("/login?err=You need to be logged in in order to view this page.")
        issueNumber = int(issueNumber)
        archiveStock = json.loads(red.get("archiveStock"))
        r = None
        for r in archiveStock:
            if r["issueNumber"] == issueNumber:
                issue = r
                break
        today = time.time()
        try:
            lastCalculated = r["lastCalculated"]
        except:
            lastCalculated = 0
        if today - lastCalculated > 86000:
            allStocks = r["stockList"]
            for a in allStocks:
                try:
                    ticker = yf.Ticker(a["ticker"]).info
                    cprice = ticker["currentPrice"]
                    a["updatedPrice"] = cprice #for calculating the difference
                    a["updatedChange"] = (a["price"]-cprice)*-100/a["price"]

                except:
                    pass
            return r
        else:
            return {"scc":True}

class Captcha:
    @app.route("/captcha/generate")
    def captchaGenerate():
        captchaJson = json.loads(open("data/captcha.json","r").read())
        pid = generate_id(15)

        num1 = random.randint(1,9)
        num2 = random.randint(1,9)
        whichStat = random.randint(0,1)
        if whichStat == 0:
            num1_ = captchaJson[str(num1)]
            num2_ = str(num2)
        if whichStat == 1:
            num1_ = num1
            num2_ = captchaJson[str(num2)]

        QuestionString = f"What is {num1_} + {num2_}?"
        answer = num1+num2
        data = {
            "question":QuestionString,
            "pid":pid,
            "answer":answer
        }


        red.set("captcha_"+pid,json.dumps(data),ex=500)
        res = {
            "pid":pid,
            "question":QuestionString,

        }
        response = make_response(res)
        response.set_cookie("pid",pid)

        return response


    @app.route("/whatsmyip")
    def whatsmyip():
        if request.environ.get("HTTP_X_FORWARDED_FOR") is None:
            ip=request.environ["REMOTE_ADDR"]
        else:
            ip = request.environ["HTTP_X_FORWARDED_FOR"]
        return str(ip)



class ProfitMarginalAPIs:
    @app.route("/profitmarginal/sendmail",methods=["POST"])
    def profitmarginalSendmail():
        if request.method == "POST":
            email = request.form.get("email")
            try:
                emus = email.split("@")[0]
                emsite = email.split("@")[1]
                if "." in emsite and not (len(emus)<3 or len(emsite)<3):
                    #valid email
                    try:
                        Mailer.profitmarginalMailingList(email)
                    except Exception as e:
                        return {"success":False,"err":str(e)}
                    return {"success":True}
                else:
                    return {"success":False}


            except:
                return abort(403)
            
    @app.route("/profitmarginal/verificationComplete/<userRedirectID>")
    def verificationComplete(userRedirectID):
        red = redis.Redis()
        try:
            data = json.loads(red.get(userRedirectID+"profitmarginal"))
        except:
            return {"Success":False,"err":"URL"}
        email = data["email"]
        timesignup = data["time"]
        currentTime = time.time()
        newdata={
            "firstSignUp":timesignup,
            "verification":currentTime,
            "email":email
        }
        pmMailingList.insert_one(newdata)
        return {"success":True}


if __name__ == "__main__":
    app.run(debug=True,port=3000)
