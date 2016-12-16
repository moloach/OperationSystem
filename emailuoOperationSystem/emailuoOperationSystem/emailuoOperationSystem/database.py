#coding=utf-8
import pymongo
import time
from bson import ObjectId
#import json

class Database:
    #database operation
    client = pymongo.MongoClient('localhost',27017,connect = False)

    server_db = client.emailuoOperation

    server_table = server_db.serverCollection

    logging_table = server_db.status
    #records the check status, is a capped collection.

    def get_host(self):
        #return the the all servers info.
        #for item in server_table.find():
            #return item
        return self.server_table.find()

    def get_one_host(self,host_id):
        #return one host info
        return self.server_table.find_one({'_id':ObjectId(host_id)})

    def add_host(self,host_format):
        #posts = self.db.posts
        try:
            add_result = self.server_table.insert_one(host_format)
            return True
        except Exception as e:
            print e

    def delete_host(self,delete_id):
        try:
            self.server_table.delete_one({"_id":ObjectId(delete_id)})
            return True
        except:
            return False
        # remove({"key":"value"})


    def edit_host(self,edit_id,edit_format):
        edit_result = self.server_table.update({'_id':ObjectId(edit_id)},{'$set':edit_format})
        #edit_format must be string type.
        #update({filter},{'$'})

    def save_check_status(self,status_format):
        post_format = {
           "status":status_format,
           "timestamp":time.time()*1000
           }
        self.logging_table.insert_one(post_format)

    def get_logging_status(self):
        return self.logging_table.find()

    def get_last_logging_status(self):
        return self.logging_table.find().sort('timestamp',pymongo.DESCENDING)[0]
            