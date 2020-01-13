
import random
import json
import time
from datetime import datetime, timedelta

def gen_datetime(min_year=2018, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    generated_datetime = start + (end - start) * random.random()
    formatted_date = generated_datetime.strftime("%d/%m/%Y %H:%M:%S")
    return formatted_date, generated_datetime.timestamp()

# print(gen_datetime())

print(datetime(2019, 1, 1, 00, 00, 00).timestamp())
