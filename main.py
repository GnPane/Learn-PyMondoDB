import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client["PyTestDB"]
collection = db["Persons"]
