import pymongo
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
        post_result = server_table.insert_one(host_format)


    def delete_host(self,delete_id):
        delete_result = server_table.remove(delete_id)



    def modify_host(self,modify_id,modify_format):
        modify_result = server_table.update(modify_format)
        #