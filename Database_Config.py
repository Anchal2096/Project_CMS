# Database connectivity establishment
import sys
import tkinter.messagebox as tm
from pymongo import *
from pymongo.errors import ConnectionFailure

# Connection of database server is global so that every function can use it

# Getting connection to database server
if_connected = MongoClient("localhost", 27017)

"""If connected then proceed further otherwise 
   connection failure is displayed in as a message 
   (except will run) and program will exit with code 1
"""
try:
    if_connected.admin.command("ismaster")
except ConnectionFailure:
    tm.showerror("DataBase Server not connected", ConnectionFailure)
    sys.exit(1)

# setting a database handler (database object kind of thing)
# you can change this database accordingly
db = if_connected["University"]
