import connexion
import six

from TimeSeriesIoT import util

import pymongo
from bson.json_util import dumps
from datetime import datetime

def connect_to_collection(address="172.19.0.3", port="27017", db="Client2", col="captures"):
    myclient = pymongo.MongoClient("mongodb://"+address+":"+port+"/")
    mydb = myclient[db]
    mycol = mydb[col]
    return mycol

def get_sensor_captures(mycol=connect_to_collection(), sensor_name="Temperature5"):
    myquery = {"NomCapteur": sensor_name}

    mydoc = mycol.find(myquery).sort("TimestampCapture", 1) #tri en descendant
    
    return dumps(mydoc)

def get_last_sensor_capture(mycol=connect_to_collection(), sensor_name="Temperature5"):
    myquery = {"NomCapteur": sensor_name}

    mydoc = mycol.find(myquery).sort("TimestampCapture", -1) #tri en descendant
    
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

    return dumps(mydoc)

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
 
    return dumps(mydoc)

def create_indexes(col=connect_to_collection()):
    resp = col.create_index([ 
        ("TimestampCapture", -1),
        ("NomCapteur", -1),
        ("DateCapture", -1)
    ])


def allrecords_get():  # noqa: E501
    """Retourne toutes les captures des capteurs

    Optional extended description in CommonMark or HTML. # noqa: E501


    :rtype: List[int]
    """
    return get_sensor_captures()


def last_sensor_id_get(sensor_id):  # noqa: E501
    """Calculer la dernière valeur

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param sensor_id: String Id of the sensor to get
    :type sensor_id: str

    :rtype: List[int]
    """
    return get_last_sensor_capture(sensor_name=sensor_id)


def mean_sensor_id_get(sensor_id, start_date=1484275868, end_date=1578883868 ):  # noqa: E501
	"""Calculer la moyenne d&#x27;un capteur entre deux dates

	Optional extended description in CommonMark or HTML. # noqa: E501

	:param sensor_id: String Id of the sensor to get
	:type sensor_id: str
	:param start_date: Integer/timestamp of the start date
	:type start_date: int
	:param end_date: Integer/timestamp of the end date
	:type end_date: int

	:rtype: List[int]
	"""

	#create_indexes()

	return get_avg_in_period(sensor_name=sensor_id, start=datetime.fromtimestamp(start_date), end=datetime.fromtimestamp(end_date))

#print(mean_sensor_id_get(sensor_id="Temperature3"))


def min_sensor_id_get(sensor_id, start_date=1484275868, end_date=1578883868):  # noqa: E501
    """Calculer la valeur minimale d&#x27;un capteur entre deux dates

    Optional extended description in CommonMark or HTML. # noqa: E501

    :param sensor_id: String Id of the sensor to get
    :type sensor_id: str
    :param start_date: Integer/timestamp of the start date
    :type start_date: int
    :param end_date: Integer/timestamp of the end date
    :type end_date: int

    :rtype: List[int]
    """
    return get_min_in_period(sensor_name=sensor_id, start=datetime.fromtimestamp(start_date), end=datetime.fromtimestamp(end_date))
