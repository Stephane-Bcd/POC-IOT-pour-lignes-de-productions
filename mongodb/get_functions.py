import pymongo
from bson.json_util import dumps
from datetime import datetime

def connect_to_collection(address="localhost", port="27017", db="Client2", col="captures"):
    myclient = pymongo.MongoClient("mongodb://"+address+":"+port+"/")
    mydb = myclient[db]
    mycol = mydb[col]
    return mycol

def get_sensor_captures(mycol=connect_to_collection(), sensor_name="Temperature5"):
    myquery = {"NomCapteur": sensor_name}

    mydoc = mycol.find(myquery).sort("TimestampCapture", 1) #tri en descendant
    
    print("All captures for sensor "+sensor_name+": \n"+str(dumps(mydoc, indent=4, sort_keys=True))+"\n\n") 
    return dumps(mydoc, indent=4, sort_keys=True)

def get_last_sensor_capture(mycol=connect_to_collection(), sensor_name="Temperature5"):
    myquery = {"NomCapteur": sensor_name}

    mydoc = mycol.find(myquery).sort("TimestampCapture", -1) #tri en descendant
    
    print("Last capture for sensor "+sensor_name+": \n"+str(mydoc[0])+"\n\n") 
    return dumps(mydoc[0])

def get_avg_in_period(mycol=connect_to_collection(), sensor_name="Temperature5", start=datetime(2019, 9, 1, 00, 00, 00), end=datetime(2020, 1, 1, 00, 00, 00)):

    start_str = start.strftime("%d/%m/%Y %H:%M:%S")
    end_str = end.strftime("%d/%m/%Y %H:%M:%S")
    start = start.timestamp()
    end = end.timestamp()

    pipeline = [
        {
            "$match": {
                "NomCapteur": sensor_name,
                "TimestampCapture": {
                    "$gte": start,
                    "$lt": end
                }  
            }
        },
        {
            "$group": {
                "_id": "$NomCapteur",
                "average": {
                    "$avg": "$ValeurCapture"
                }
            }
        },
        {"$sort": {"TimestampCapture": -1}}
    ]


    mydoc = mycol.aggregate(pipeline)

    print("Average for sensor "+sensor_name+" between dates "+start_str+" and "+end_str+": \n"+dumps(mydoc, indent=4, sort_keys=True)+"\n\n") 
    return dumps(mydoc, indent=4, sort_keys=True)

def get_min_in_period(mycol=connect_to_collection(), sensor_name="Temperature5", start=datetime(2018, 9, 1, 00, 00, 00), end=datetime(2020, 1, 1, 00, 00, 00)):

    start_str = start.strftime("%d/%m/%Y %H:%M:%S")
    end_str = end.strftime("%d/%m/%Y %H:%M:%S")
    start = start.timestamp()
    end = end.timestamp()

    pipeline = [
        {
            "$match": {
                "NomCapteur": sensor_name,
                "TimestampCapture": {
                    "$gte": start,
                    "$lt": end
                }  
            }
        },
        {
            "$group": {
                "_id": "$NomCapteur",
                "min": {
                    "$min": "$ValeurCapture"
                }
            }
        },
        {"$sort": {"TimestampCapture": -1}}
    ]


    mydoc = mycol.aggregate(pipeline)

    print("Minimum for sensor "+sensor_name+" between dates "+start_str+" and "+end_str+": \n"+dumps(mydoc, indent=4, sort_keys=True)+"\n\n") 
    return dumps(mydoc, indent=4, sort_keys=True)

def create_indexes(col=connect_to_collection()):
    resp = col.create_index([ 
        ("TimestampCapture", -1),
        ("NomCapteur", -1),
        ("DateCapture", -1)
    ])

'''
    TESTS
'''
need_tests = True

if need_tests:
    create_indexes()
    get_sensor_captures()
    get_last_sensor_capture()
    get_avg_in_period()
    get_min_in_period()






