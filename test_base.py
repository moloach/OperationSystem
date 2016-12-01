import pymongo

client = pymongo.MongoClient('localhost',27017)

db = client.emailuoOperation

pattern = {"hostname":"121.156.11.3"}
data = db.serverCollection.find_one(pattern)
#print(data)

print(db.serverCollection.find_one())

#add elements into the collection
db.serverCollection.update(pattern, {"$set":{"OS":"Windows Server 2008"}})

#query all data in collection
for item in db.serverCollection.find():
    print(item)
