import time
import os
import pymongo
import redis
from datetime import datetime
from app import base

mongo = pymongo.MongoClient()
db = mongo["KentelPlatform"]
users = db["Users"]
red = redis.Redis()
filters = db["Filters"]



    

