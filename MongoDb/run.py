from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://Loh:Loh@cluster0.s7j3biq.mongodb.net/Db-San?retryWrites=true&w=majority")

db = cluster["Db-San"]
collection = db["Collection-San"]
#collection.insert_one({
#    "_id":1,
#    "name":"Sania"
#})
print(collection.find_one({
   "_id":1
}))

