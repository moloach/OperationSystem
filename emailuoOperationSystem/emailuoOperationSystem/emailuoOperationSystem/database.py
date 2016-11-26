import pymongo 

client = pymongo.MongoClient('localhost',27017)
#创建一个数据库客户端实例，连接本地数据库

db = client.mydb
#连接到某一个数据库


