from pymongo import Connection

MONGO_DB_HOST = 'localhost'
MONGO_DB_HOST_PORT = 27017
MONGO_DB_COLLECTION = 'livefeed'

def getConnection(mongoHost = MONGO_DB_HOST, mongoPort = MONGO_DB_HOST_PORT, mongoCollection = MONGO_DB_COLLECTION):
    connection = Connection(mongoHost, mongoPort)
    db = connection[mongoCollection]
    return db                
