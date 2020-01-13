import pymongo
import json
import os

def create_indexes(col):
    resp = col.create_index([ 
        ("TypeCapteur", -1),
        ("NomCapteur", -1),
        ("NomLigne", -1),
        ("NomUsine", -1)
    ])


project_fullpath = os.environ['PROJECTPATH']

with open(project_fullpath+'/generated_data.txt') as json_file:
    data = json.load(json_file)

    databases = {}
    connection = pymongo.MongoClient("mongodb://localhost:27017/")

    for client in data:
        databases[client] = {}
        databases[client]["database"] = connection[client]
        databases[client]["metadatacol"]  =  databases[client]["database"]["metadata"]

        for usine in data[client]:
            for sensor in data[client][usine]:
                document = {"TypeCapteur": sensor["sensor_type"], "NomCapteur": sensor["sensor_name"], "NomLigne": sensor["line"], "NomUsine": usine}
                print(document)
                databases[client]["metadatacol"].insert_one(document)
                
        create_indexes(databases[client]["metadatacol"])


# creating weather collection
connection = pymongo.MongoClient("mongodb://localhost:27017/")
weather_db = connection["weather"]
country_col = weather_db["paris"]


# creating csv from FTP server collection
connection = pymongo.MongoClient("mongodb://localhost:27017/")
weather_db = connection["FTP"]
country_col = weather_db["csv"]


print ( connection.list_database_names())
