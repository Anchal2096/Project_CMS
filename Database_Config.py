# Database connectivity establishment
import sys
from pymongo import *
from server_list import *
from pymongo.errors import ConnectionFailure

# Connection of database server is global so that every function can use it

# Getting connection to database server
mongo_connection = MongoClient(cloud_SVR['DEV'])

"""If connected then proceed further otherwise 
   connection failure is displayed in as a message 
   ('except' block will run) and program will exit with code 1
"""
try:
    mongo_connection.admin.command("ismaster")
except ConnectionFailure:
    print("DataBase Server not connected", ConnectionFailure)
    sys.exit(1)
