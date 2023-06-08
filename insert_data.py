import os
from dotenv import load_dotenv
import random
import time
from mysql.connector import (connection)


load_dotenv()

user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
database = os.environ.get("DATABASE")


station_dict = {
    "1":	"Khu Khot",
    "2":	"Yaek Kor Por Aor",
    "3":	"Royal Thai Air Force Museum",
    "4":	"Bhumibol Adulyadej Hospital",
    "5":	"Saphan Mai",
    "6":	"Sai Yud",
    "7":	"Phahon Yothin 59",
    "8":	"Wat Phra Sri Mahathat",
    "9":	"11th Infantry Regiment",
    "10":	"BangBua",
    "11":	"Royal Forest Department",
    "12":	"Kasetsart University",
    "13":	"Sena Nikhom",
    "14":	"Ratchayothin",
    "15":	"Phahon Yothin 24",
    "16":	"Ha Yaek Lat Phrao",
    "17":	"Mo Chit",
    "18":	"Saphan Khwai",
    "19":	"Ari",
    "20":	"Sanam Pao",
    "21":	"Victory Monument",
    "22":	"Phaya Thai",
    "23":	"Ratchathewi",
    "24":	"Siam",
}

card_types = ["student", "adult", "elder"]


insert_sql = """
INSERT INTO fares (
    passenger_id,
    card_type,
    origin_id,
    origin_name,
    destination_id,
    destination_name)
    VALUES (
    %(passenger_id)s,
    %(card_type)s,
    %(origin_id)s,
    %(origin_name)s,
    %(destination_id)s,
    %(destination_name)s
    )
"""


conn = connection.MySQLConnection(
    user=user,
    password=password,
    host=host,
    database=database
)
cur = conn.cursor()

i = 3
while i < 11:
    stations = random.sample(list(station_dict.items()), 2)
    card_type = random.choices(card_types, weights=[30,55,15])

    insert_data = {
    "passenger_id": i,
    "card_type": card_type[0],
    "origin_id": stations[0][0],
    "origin_name": stations[0][1],
    "destination_id": stations[1][0],
    "destination_name": stations[1][1]
    }
    
    cur.execute(insert_sql, insert_data)
    conn.commit()
    
    time.sleep(30)
    i += 1

cur.close()
conn.close()