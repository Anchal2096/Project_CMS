# Database connectivity establishment
import sys
from pymongo import *
from server_list import *
from pymongo.errors import *

"""
   Application will look to connect to the cloud server(s) first,
   If failed, the connection will be established to a local server.
"""


def check_connection():
    # no of seconds for timeout
    max_timeout = 300
    try:
        print("Connecting to cloud server(s)...")
        # trying to establish connection to 'DEV' cloud server
        # all server configuration mentioned in server_list.py
        mongo_connection = \
            MongoClient(host=cloud_SVR['DEV'],
                        port=27017, connectTimeoutMS=max_timeout,
                        serverSelectionTimeoutMS=max_timeout)
        return mongo_connection

    # when connection (to cloud server) has been refused or failed
    except ConfigurationError:
        print("Connection failed.")
        print("Redirecting to local servers...")
        try:
            # redirect to the local servers
            mongo_connection = \
                MongoClient(host=local_SVR['PC'],
                            port=27017, connectTimeoutMS=max_timeout,
                            serverSelectionTimeoutMS=max_timeout)
            print("Connection established")
            return mongo_connection

        # when connection (to local server) has been refused or failed
        except ServerSelectionTimeoutError:
            print("[local SVR] Connection time out. Server may be offline.")
        except ConnectionFailure:
            print("[local SVR] Connection failure exception has been raised, exiting...")
            exit(1)
        except ConfigurationError:
            print("[local SVR] Configuration error exception has been raised, exiting...")
            exit(1)

    # when connection (to cloud server) has been refused or failed
    except ServerSelectionTimeoutError:
        print("[Cloud SVR] Connection time out. Server may be offline.")
    except ConnectionFailure:
        print("[Cloud SVR] Connection failure exception has been raised, exiting...")
        exit(1)
