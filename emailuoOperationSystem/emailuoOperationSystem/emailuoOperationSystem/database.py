import pymongo
from bson import ObjectId
#import json

class Database:
    #database operation
    client = pymongo.MongoClient('localhost',27017)

    db = client.emailuoOperation

    server_table = db.serverCollection

    def get_host(self):
        #for item in server_table.find():
            #return item
        return self.server_table.find()

    def add_host(self,host_format):
        #posts = self.db.posts
        add_result = self.server_table.insert_one(host_format)


    def delete_host(self,delete_id):
        try:
            delete_result = self.server_table.remove({"_id":ObjectId(delete_id)})
            return True
        except:
            return False
        # remove({"key":"value"})


    def edit_host(self,modify_id,modify_format):
        edit_result = self.server_table.update(modify_format)
        #