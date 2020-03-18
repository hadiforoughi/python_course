import pymongo
from pymongo import MongoClient
client = MongoClient()
db=client.test
users=db.users
user=[{"name":"hadi","password":"hadi1377"},{"name":"ahmad"}]
id=users.insert_many(user).inserted_ids
users.create_index([("name",pymongo.ASCENDING )])
re=users.find({"name":"hadi"}).count()

print(re)