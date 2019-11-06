import pymongo
from pymongo import MongoClient
import jsonReader

MDB_USERNAME = jsonReader.getValue('MDB_USERNAME')
MDB_PASSWORD = jsonReader.getValue('MDB_PASSWORD')

global cluster
cluster = MongoClient(f"mongodb+srv://{MDB_USERNAME}:{MDB_PASSWORD}@cluster0-tmmtg.mongodb.net/test?retryWrites=true&w=majority")

def getCollection(collection):
    global cluster
    collection = (cluster["monkebot"])[collection]
    return collection

# db = cluster["monkebot"]
# collection = db["monkebot"]
# post = {"_id": 0, "name": "tim", "score": 5}
# collection.insert_one(post)
