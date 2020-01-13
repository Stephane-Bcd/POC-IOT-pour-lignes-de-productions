import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Client1"]
mycol = mydb["metadata"]

myquery = {}

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x) 
