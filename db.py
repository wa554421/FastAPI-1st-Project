from pymongo import MongoClient

mongo_uri = "mongodb+srv://waleed:waleed123@newcluster.vlpyfwt.mongodb.net/"

conn = MongoClient(mongo_uri)

database = conn['website']

collection = database['website1']

