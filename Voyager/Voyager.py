from configparser import ConfigParser
from ogame import OGame
from ogame.constants import destination, coordinates, ships, mission, speed, buildings, status, fleet, resources
from threading import Thread, Event
import datetime
from datetime import datetime
import time
import random
from random import randint
from time import sleep
from tqdm import tqdm
from ogame.constants import resources
from inspect import currentframe, getframeinfo
import json
from ogame import OGame
from ogame.constants import destination, coordinates, ships, mission, speed, buildings, status
from ogame.constants import coordinates, destination
import json
from os import path

cfg = ConfigParser()
cfg.read('config.ini')

USER = str(cfg.get('login','login'))
print("Login:",USER)
PASSWORD = str(cfg.get('login','password'))
print("Password:",'*' * len(PASSWORD))
UNI = str(cfg.get('login','universe'))
print("Universe:",UNI)
ts = time.time()
timestamp = ts
date_time = datetime.fromtimestamp(timestamp)
archive = str(UNI) + "_" + date_time.strftime("%m_%d_%Y_%H_%M") +".json"
with open(archive, 'w') as f:
    print("The json file is created:", archive)
filename = archive
lst = []

empire = OGame(UNI, USER, PASSWORD)

print("Gathering data, please wait...")

player_number=int(0)
for x in range(1,8):
    for y in range(1,499):
        for planet in empire.galaxy(coordinates(x,y)):
            player_number=player_number+1
            player_name=str(planet.player)
            player_rank=planet.rank
            planet_position=str(planet.position)
            planet_name=planet.name
            player_id=planet.player_id
            player_status=str(planet.status)
            does_moon_exist=planet.moon
            player_alliance=planet.alliance

            with open(filename, mode='w') as f:
                json.dump(lst, f)
            with open(filename, mode='w') as f:
                lst.append({'player_name': player_name,
                            'player_rank':player_rank,
                            'player_alliance':player_alliance,
                            'player_status': player_status,
                            'player_id': player_id,
                            'planet_name': planet_name,
                            'planet_position':planet_position,
                            'does_moon_exist':does_moon_exist,
                            })
                json.dump(lst, f,indent=2)
        print("Scanned: ", player_name)
        sleep(0.25)
    print('―' * 10)
    print(x, "of 7")
    print('―' * 10)
print('―' * 10)
print('―' * 15)
print("Scanned: ", player_number)
print('―' * 15)
print('―' * 10)
