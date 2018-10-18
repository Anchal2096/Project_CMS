# This file contains information about different servers

# local machine server
local_SVR = {
    'name': "mongodb://localhost:27017"
}

# MongoDB Atlas cloud server
cloud_SVR = {
    'DEV': "mongodb+srv://Dev_Vrat:mongo_cloud_space_owner@projects-fwo0r.mongodb.net/",
    'ABHISHEK': "mongodb://localhost:27017",
    'ANCHAL': "mongodb://localhost:27017",
    'USER' : "mongodb://localhost:27017"
}

# password recovery sender's details
# try with your own email id and your password
"""
Currently working with only gmail.
Hopefully we'll be adding other servers too....
And don't forget to replace this starred password with your own.
"""
sender = "atrivedi397@gmail.com"
sender_passwd = "*********"

"""
general command to connect from the cloud server
1) Short SRV connection string, supported: shell 3.6+)
"mongodb+srv://projects-fwo0r.mongodb.net/test" --username <USERNAME>

2) Standard connection string, supported: shell 3.4+)
"mongodb://projects-shard-00-00-fwo0r.mongodb.net:27017,
projects-shard-00-01-fwo0r.mongodb.net:27017,
projects-shard-00-02-fwo0r.mongodb.net:27017/
test?replicaSet=Projects-shard-0" --ssl --authenticationDatabase admin 
--username <USERNAME> --password <PASSWORD>
"""
