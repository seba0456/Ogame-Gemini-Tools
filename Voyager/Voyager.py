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
import ujson
from os import path

cfg = ConfigParser()
cfg.read('config.ini')
gal_size = int(cfg.get('misc','gal_size'))+1
USER = str(cfg.get('login','login'))
print("Login:",USER)
PASSWORD = str(cfg.get('login','password'))
print("Password:",'*' * len(PASSWORD))
UNI = str(cfg.get('login','universe'))
print("Universe:",UNI)
smart_wait = int(cfg.get('misc','smart_wait'))
ts = time.time()
timestamp = ts
date_time = datetime.fromtimestamp(timestamp)
archive = str(UNI) + "_" + date_time.strftime("%d_%m_%Y_%H_%M") +".json"
with open(archive, 'w') as f:
    print("The json file is created:", archive)
filename = archive
lst = []

empire = OGame(UNI, USER, PASSWORD)

print("Gathering data, please wait...")
print("0 of ", gal_size-1)

player_number=int(0)
for x in range(1,gal_size):
    for y in tqdm(range(int(1),int(500)), colour="WHITE"):
        try:
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
                    ujson.dump(lst, f)
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
                    ujson.dump(lst, f,indent=2)
        #print("Scanned: ", player_name)
        except:
            sleep(1)
            try:
                empire = OGame(UNI, USER, PASSWORD)
            except:
                print("Unable to log-in!")
        if smart_wait == 1:
            planets_in_system = empire.galaxy(coordinates(x, y))
            if len(planets_in_system) > 4:
                sleep(planets_in_system*round(random.uniform(0.1, 0.2), 2))
            else:
                sleep(round(random.uniform(0.4, 0.6), 2))
        else:
            sleep(round(random.uniform(0.4, 0.8), 2))
    print('_' * 10)
    print(x, "of ",gal_size-1)
    print("Scanned: ", player_number, " players.")
    print('_' * 10)
print('_' * 15)
print("Scanned: ", player_number, " players.")
print('_' * 15)
