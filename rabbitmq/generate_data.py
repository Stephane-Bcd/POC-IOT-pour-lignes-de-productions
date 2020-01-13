import pika
import random
import json
import time
from datetime import datetime, timedelta
import os
import math

'''
    Function to connect to rabbitmq
'''
def rabbitmq_connection(adress = "localhost", port = 5672, vhost = "Client1", user = "rabbitmq", pswd = 'rabbitmq'):
    credentials = pika.PlainCredentials(user, pswd)
    parameters = pika.ConnectionParameters(adress,
                                           port,
                                           vhost,
                                           credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    return channel, connection

'''
    Function to post a message on an eschange
'''
def pub_msg(channel, exchange= "Client1-Maison1", routing_key = "", msg='Hello World!'):
    properties = pika.BasicProperties(content_type="application/json", content_encoding="utf8")
    channel.basic_publish(exchange=exchange,
            routing_key=routing_key,
            body=msg,
            properties=properties
        )
'''
    Function to generate random date
'''
def gen_datetime(min_year=2018, max_year=datetime.now().year-1):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    generated_datetime = start + (end - start) * random.random()
    formatted_date = generated_datetime.strftime("%d/%m/%Y %H:%M:%S")
    return formatted_date, math.floor(generated_datetime.timestamp())

'''
    Function to generate random data for a specific sensot
'''
def gen_data (sensor_type, sensor_name, nb):
    
    returned_data = []

    for i in range (0,nb):
        date, timestamp = gen_datetime()

        if sensor_type in ["OuverturePorteEntree","Ampoule","OuverturePorteFenetre","Presence"]:
            if i==0:
                val = random.choice([0, 1])
            returned_data.append({"NomCapteur": sensor_name, "DateCapture": date,"ValeurCapture":  math.floor(val), "TimestampCapture": timestamp})
        elif sensor_type == "Temperature":
            returned_data.append({"NomCapteur": sensor_name, "DateCapture": date, "ValeurCapture":  math.floor(random.uniform(-10.0, 35.0)*100)/100, "TimestampCapture": timestamp})
        elif sensor_type == "Chauffage":
            if i==0:
                val = random.choice(["Confort", "Confort -1 C", "Confort -2 C", "Eco", "Hors gel", "Arret"])
            returned_data.append({"NomCapteur": sensor_name, "DateCapture": date, "ValeurCapture":  val, "TimestampCapture": timestamp})
        elif sensor_type in ["PuissanceCapt","PriseElec"]:
            if i==0:
                val = random.choice([True,False])
            if val:
                val2 = random.uniform(1, 6)
            else:
                val2 = 0
            returned_data.append({"NomCapteur": sensor_name, "DateCapture": date, "ValeurCapture":  math.floor(val2), "TimestampCapture": timestamp})

    return returned_data


'''
    MAIN GENERATION CODE
'''


# Both clients sensors data initialisation

client1_data = {
    "Entree": [
        {
            "sensor_name": None,
            "sensor_type": "OuverturePorteEntree",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Ampoule",
            "generated_data": []
        }
    ],
    "Salon": [
        {
            "sensor_name": None,
            "sensor_type": "OuverturePorteFenetre",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "OuverturePorteFenetre",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Ampoule",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Ampoule",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Presence",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Temperature",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Chauffage",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Chauffage",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "PuissanceCapt",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "PuissanceCapt",
            "generated_data": []
        }
    ],
    "Chambre": [
        {
            "sensor_name": None,
            "sensor_type": "OuverturePorteFenetre",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "OuverturePorteFenetre",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Ampoule",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Presence",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Temperature",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Chauffage",
            "generated_data": []
        }
    ],
    "Cuisine": [
        {
            "sensor_name": None,
            "sensor_type": "Presence",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Temperature",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Chauffage",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "PriseElec",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "PuissanceCapt",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "PuissanceCapt",
            "generated_data": []
        }
    ],
    "Salle de bains": [
        {
            "sensor_name": None,
            "sensor_type": "PuissanceCapt",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Chauffage",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Ampoule",
            "generated_data": []
        }
    ]
}

client2_data = {
    "Chambre": [
        {
            "sensor_name": None,
            "sensor_type": "Ampoule",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Presence",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Temperature",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Chauffage",
            "generated_data": []
        }
    ],
    "Salon": [
        {
            "sensor_name": None,
            "sensor_type": "Ampoule",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Presence",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Temperature",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Chauffage",
            "generated_data": []
        }
    ],
    "Cuisine": [
        {
            "sensor_name": None,
            "sensor_type": "Ampoule",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Presence",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Temperature",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Chauffage",
            "generated_data": []
        }
    ],
    "Salle de bains":[
        {
            "sensor_name": None,
            "sensor_type": "PuissanceCapt",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Chauffage",
            "generated_data": []
        },
        {
            "sensor_name": None,
            "sensor_type": "Ampoule",
            "generated_data": []
        }
    ]
}

data = {
    "Client1": client1_data,
    "Client2": client2_data
}


'''

    Set all names and generate data for Client1 and Client2

'''

captures_by_sensor = 90
verbose = False
clients_to_ignore = []

print("generate_data.py: generating names and data")

tmp_sensor_names_counters = {}

for client in data:
    if client not in clients_to_ignore:
        client_data = data[client]
        for room in client_data:
            room_sensors = client_data[room]
            
            for sensor_idx, sensor in enumerate(room_sensors, start=0):

                sensor_type = sensor["sensor_type"]

                if not sensor_type in tmp_sensor_names_counters:
                    tmp_sensor_names_counters[sensor_type] = 0
                
                sensor_name = sensor_type + str(tmp_sensor_names_counters[sensor_type])
                tmp_sensor_names_counters[sensor_type]+=1
                
                data[client][room][sensor_idx]["sensor_name"] = sensor_name
                data[client][room][sensor_idx]["generated_data"] = gen_data(sensor_type, sensor_name, captures_by_sensor)




#Saving all data in file and print it on console
if verbose: print (tmp_sensor_names_counters)
if verbose: print(json.dumps(data, indent=4, sort_keys=True))


project_fullpath = os.environ['PROJECTPATH']
f= open(project_fullpath+"/generated_data.txt","w+")
f.write(json.dumps(data, indent=4, sort_keys=True))
f.close()





'''
    Send all data to rabbitmq

'''
print("generate_data.py: sending all data to rabbitmq")

for client in data:
    client_data = data[client]

    # Connecting to rabbitmq
    channel, connection = rabbitmq_connection(vhost = client)

    for room in client_data:
        room_sensors = client_data[room]
        for sensor_idx, sensor in enumerate(room_sensors, start=0):
            sensor_data = sensor["generated_data"]
            for capture in sensor_data:
                pub_msg(channel, exchange= client+"-Maison1", msg=str(json.dumps(capture)))

    # Disconnecting from Rabbitmq
    connection.close()


print("generate_data.py: finished successfully")











