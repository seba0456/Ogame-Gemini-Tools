from configparser import ConfigParser
from ogame import OGame
from ogame.constants import destination, coordinates, ships, mission, speed, buildings, status, fleet, resources
from bs4 import BeautifulSoup
from threading import Thread, Event
import datetime
import time
import random
import re
from ogame.constants import resources
res = resources(metal=1, crystal=2, deuterium=3)
[1, 2, 3]
cfg = ConfigParser()
cfg.read('config.ini')
#login
login = str(cfg.get('login','login'))
print(login)
password = str(cfg.get('login','password'))
print(password)
universe = str(cfg.get('login','universe'))
print(universe)
#login to Ogame
print("Bot is starting...")
print('―' * 10)
bot = OGame(universe,login,password)
print("Login successful!")
print('―' * 10)
#planet
planet_id = int(cfg.get('planet','planet_id'))
source_system = int(cfg.get('planet','source_system'))
target_system_range = int(cfg.get('planet','target_system_range'))
min_system = source_system - target_system_range
max_system = source_system + target_system_range + 1
num_range = range(min_system,max_system)
num_list = list(num_range)
print("Source planet is: ", source_system,".")
print("Expeditions will be sent in systems: ",num_list,".")
#fleet
heavy_fighter=int(cfg.get('fleet','LM'))
cruiser=int(cfg.get('fleet','KR'))
battleship=int(cfg.get('fleet','OW'))
interceptor=int(cfg.get('fleet','PA'))
bomber=int(cfg.get('fleet','BO'))
destroyer=int(cfg.get('fleet','NI'))
deathstar=int(cfg.get('fleet','GS'))
reaper=int(cfg.get('fleet','RO'))
explorer=int(cfg.get('fleet','PI'))
small_transporter=int(cfg.get('fleet','MT'))
large_transporter=int(cfg.get('fleet','DT'))
espionage_probe=int(cfg.get('fleet','EP'))
light_fighter=int(cfg.get('fleet','LM'))
fuel_usage=int(cfg.get('fleet','required_deuter'))
EXP_MAX=int(cfg.get('fleet','EXP_MAX'))
print("Expeditions will be sent ",EXP_MAX, "times.")
#functions
#print error
def error():
    print("Error, Bot will try to login again")
#sleep function
def sleep_until(target, delay=0):
    now = datetime.datetime.now()
    delta = target - now

    if delta > datetime.timedelta(0):
        time.sleep(delta.total_seconds() + delay)
        return True
#sending expedtions
def bot_expedition(empire, UNI=universe):
    print('―' * 10)
    print("Working, sending expeditions")
    while 1:
        expeditions = []
        # check for available slots
        try:
            expeditions = [fleet for fleet in empire.fleet() if fleet.mission == mission.expedition]
            EXP_NUM = len(expeditions)
            time.sleep(2)

        except:
            print("Error, No available slots...")
            empire.relogin(universe)
            time.sleep(random.randint(3,7))
            continue

        # If available slots
        if EXP_NUM < int(EXP_MAX):
            print("Available slots: (", EXP_MAX - EXP_NUM, " z ", EXP_MAX, ")")

            # check for expedtion fleet
            try:
                print("test")
                available_ships = empire.ships(source_system)

                if available_ships.small_transporter.amount >= small_transporter and available_ships.cruiser.amount >= cruiser and available_ships.heavy_fighter.amount >= heavy_fighter and available_ships.battleship.amount >= battleship and available_ships.interceptor.amount >= interceptor and available_ships.bomber.amount >= bomber and available_ships.destroyer.amount >= destroyer and available_ships.deathstar.amount >= deathstar and available_ships.deathstar.amount >= deathstar and available_ships.reaper.amount >= reaper and available_ships.explorer.amount >= explorer and available_ships.large_transporter.amount >= large_transporter and available_ships.espionage_probe.amount >= espionage_probe:
                    EXP_SQUAD = [ships.small_transporter(small_transporter),ships.cruiser(cruiser),ships.heavy_fighter(heavy_fighter),ships.battleship(battleship),ships.interceptor(interceptor),ships.bomber(bomber),ships.destroyer(destroyer),ships.deathstar(deathstar),ships.reaper(reaper),ships.explorer(explorer),ships.large_transporter(large_transporter),ships.large_transporter(large_transporter)]
                else:
                    print("Not enough ships!")

            except:
                error()
                empire.relogin(universe)
                time.sleep(random.randint(3,7))
                continue

            # sending expedition
            try:
                empire.resources(id)
                res = empire.resources(id)
                deuter_avaliable = res.deuterium
                if deuter_avaliable >= fuel_usage:
                    empire.send_fleet(mission=mission.expedition,id=source_system,where=coordinates(source_system[0], random.choice(num_list), 16),ships=EXP_SQUAD,resources=[0, 0, 0],speed=speed.max,holdingtime=1)
                    print("Expedition has been sent!")
                else:
                    print("Not enough deuterium!")

            except:
                error()
                empire.relogin(universe)
                time.sleep(random.randint(3,7))
                continue
            expeditions = [fleet for fleet in empire.fleet() if fleet.mission == mission.expedition]
            EXP_NUM = len(expeditions)
            if deuter_avaliable < fuel_usage:
                print(f"Not enough deuterium!")
            elif EXP_NUM != EXP_MAX:
                print(f"Available slots")
            time.sleep(random.randint(3,7))

        else:

            # get time to closest fleet return
            closest_time = min([ fleet.arrival for fleet in expeditions])
            print(f"No Available slots: {closest_time}.")

            # sleep to to closest fleet return
            f"[EXP] Usypiam do: {closest_time}."
            sleep_until(closest_time, 5)
expeditions = Thread(target=bot_expedition, args=(bot,))
expeditions.start()