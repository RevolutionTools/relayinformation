from pymongo import Connection
from utils import db

def getConnection(mongoHost = MONGO_DB_HOST, mongoPort = MONGO_DB_HOST_PORT, mongoCollection = MONGO_DB_COLLECTION):
    connection = Connection(mongoHost, mongoPort)
    db = connection[mongoCollection]
    return db   

def isEmailinDb(string):  
        emailDB = db.getConnection('localhost', 27017, 'users')
        emailDB.email.update( {"email" : emailDict['email']}, emailDict, upsert = True)

	
