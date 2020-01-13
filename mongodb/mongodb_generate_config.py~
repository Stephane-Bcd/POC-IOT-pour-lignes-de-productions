import pymongo
import json




project_fullpath = "/media/stephane/DATA/ESILV/A5/Dev Apps et Web services pour l'IOT/TP/Fichiers TP/Dev app & web service for IOT - Fil rouge"

with open(project_fullpath+'/generated_data.txt') as json_file:
    data = json.load(json_file)

    databases = {}
    connection = pymongo.MongoClient("mongodb://localhost:27017/")

    for client in data:
        databases[client] = {}
        databases[client]["database"] = connection[client]
        databases[client]["metadatacol"]  =  databases[client]["database"]["metadata"]

        for room in data[client]:
            for sensor in data[client][room]:
                document = {"TypeCapteur": sensor["sensor_type"], "NomCapteur": sensor["sensor_name"], "NomPiece": room, "NomMaison": "Maison1"}
                print(document)
                databases[client]["metadatacol"].insert_one(document)
                




print ( connection.list_database_names())
