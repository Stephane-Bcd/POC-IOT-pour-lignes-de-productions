import pymongo
import json
import os


project_fullpath = os.environ['PROJECTPATH']

with open(project_fullpath+'/generated_data.txt') as json_file:
    data = json.load(json_file)
    
    clients_to_ignore = ["Client1"]

    databases = {}
    connection = pymongo.MongoClient("mongodb://localhost:27017/")

    for client in data:
        if client not in clients_to_ignore:
            databases[client] = {}
            databases[client]["database"] = connection[client]
            databases[client]["capturescol"]  =  databases[client]["database"]["captures"]
            databases[client]["capturescol"].drop() 
            databases[client]["capturescol"]  =  databases[client]["database"]["captures"]

            for room in data[client]:
                for sensor_idx, sensor in enumerate(data[client][room], start=0):
                    for capture in data[client][room][sensor_idx]["generated_data"]:
                        document = capture
                        print(document)
                        databases[client]["capturescol"].insert_one(document)
                




print ( connection.list_database_names())
