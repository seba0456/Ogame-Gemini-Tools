from configparser import ConfigParser
from ogame import OGame
from ogame.constants import destination, coordinates, ships, mission, speed, buildings, status, fleet, resources
from threading import Thread, Event
import datetime
import time
import random
from time import sleep
from tqdm import tqdm
from ogame.constants import resources
from inspect import currentframe, getframeinfo
cfg = ConfigParser()
cfg.read('config.ini')
#login
login = str(cfg.get('login','login'))
print("Login:",login)
password = str(cfg.get('login','password'))
print("Password:",'*' * len(password))
universe = str(cfg.get('login','universe'))
print("Universe:",universe)
#login to Ogame
print("Bot is starting...")
print('―' * 10)
bot = OGame(universe,login,password)
print("Login was successful!")
print('―' * 10)
#planet
planet_id = int(cfg.get('planet','planet_id'))
galactic = bot.celestial_coordinates(planet_id)
source_system = int(cfg.get('planet','source_system'))
target_system_range = int(cfg.get('planet','target_system_range'))
min_system = source_system - target_system_range
max_system = source_system + target_system_range + 1
num_range = range(min_system,max_system)
num_list = list(num_range)
print("The source planet is: ", source_system,".")
print("Expeditions will be sent to systems: ",num_list,".")
#fleet
cruiser=int(cfg.get('fleet','KR'))
battleship=int(cfg.get('fleet','OW'))
reaper=int(cfg.get('fleet','RO'))
explorer=int(cfg.get('fleet','PI'))
small_transporter=int(cfg.get('fleet','MT'))
large_transporter=int(cfg.get('fleet','DT'))
espionage_probe=int(cfg.get('fleet','EP'))
light_fighter=int(cfg.get('fleet','LM'))
destroyer=int(cfg.get('fleet','NI'))
EXP_MAX=int(cfg.get('fleet','EXP_MAX'))
print("Expeditions will be sent ",EXP_MAX, "times.")
#settings
bot_continue_anyway=int(cfg.get('settings','continue_anyway'))
progress_bar_enable=int(cfg.get('settings','enable_progress_bar'))
#functions
#sleep function
def sleep_until(target, delay=0):
    now = datetime.datetime.now()
    delta = target - now

    if delta > datetime.timedelta(0):
            if progress_bar_enable == 1:
                for i in tqdm(range (int(delta.total_seconds() + delay)), colour="WHITE"):
                    sleep(1)
            else:
                time.sleep(delta.total_seconds() + delay)
    print('―' * 10)
    time.sleep(random.randint(2,5))
    return True
#sending expedition
def bot_expedition(empire, UNI=universe):
    print('―' * 10)
    print("Working, sending expeditions")
    while 1:
        cfg = ConfigParser()
        cfg.read('config.ini')
        cruiser=int(cfg.get('fleet','KR'))
        battleship=int(cfg.get('fleet','OW'))
        reaper=int(cfg.get('fleet','RO'))
        explorer=int(cfg.get('fleet','PI'))
        small_transporter=int(cfg.get('fleet','MT'))
        large_transporter=int(cfg.get('fleet','DT'))
        espionage_probe=int(cfg.get('fleet','EP'))
        light_fighter=int(cfg.get('fleet','LM'))
        destroyer=int(cfg.get('fleet','NI'))
        expeditions = []
        # check for available slots
        try:
            expeditions = [fleet for fleet in empire.fleet() if fleet.mission == mission.expedition]
            EXP_NUM = len(expeditions)
            time.sleep(2)

        except Exception as e:
            print("Error, something went wrong:",e)
            empire.relogin(universe)
            time.sleep(random.randint(3,7))
            continue

        # If available slots
        if EXP_NUM < int(EXP_MAX):
            print("Available slots: (", EXP_MAX - EXP_NUM, " of ", EXP_MAX, ")")

            # check for expedition fleet
            try:
                available_ships = empire.ships(planet_id)
                if available_ships.small_transporter.amount >= small_transporter and available_ships.large_transporter.amount >= large_transporter:
                    EXP_SQUAD = [ships.small_transporter(small_transporter),ships.large_transporter(large_transporter), ships.light_fighter(light_fighter), ships.espionage_probe(espionage_probe), ships.cruiser(cruiser), ships.battleship(battleship), ships.reaper(reaper), ships.explorer(explorer),ships.destroyer(destroyer)]
                else:
                    if bot_continue_anyway == 0:
                        if small_transporter !=0:
                            print("Small transporter", available_ships.small_transporter.amount, "of", small_transporter,"(", available_ships.small_transporter.amount - small_transporter, ")")
                        if large_transporter !=0:
                            print("Large transporter", available_ships.large_transporter.amount, "of",small_transporter, "(", available_ships.large_transporter.amount - large_transporter, ")")
                        print("Not enough transporter ships! Program will wait 60-120 seconds.")
                        sleep_time=time.sleep(random.randint(60, 120))
                        print("Waiting:",sleep_time)
                    else:
                        print("Not enough transporter ships! Program will continue anyway!")
                        if available_ships.small_transporter.amount < small_transporter:
                            print("Warning! Not enough: Small transporter",available_ships.small_transporter.amount, "of", small_transporter, "(",available_ships.small_transporter.amount - small_transporter, ")")
                            EXP_SQUAD = [ships.small_transporter(available_ships.small_transporter.amount),ships.large_transporter(large_transporter),ships.light_fighter(light_fighter), ships.espionage_probe(espionage_probe),ships.cruiser(cruiser), ships.battleship(battleship), ships.reaper(reaper),ships.explorer(explorer), ships.destroyer(destroyer)]
                        elif available_ships.large_transporter.amount < large_transporter:
                            print("Warning! Not enough: Large transporter",available_ships.large_transporter.amount, "of", large_transporter, "(",available_ships.large_transporter.amount - large_transporter, ")")
                            EXP_SQUAD = [ships.small_transporter(small_transporter),ships.large_transporter(available_ships.large_transporter.amount),ships.light_fighter(light_fighter),ships.espionage_probe(espionage_probe), ships.cruiser(cruiser), ships.battleship(battleship), ships.reaper(reaper), ships.explorer(explorer), ships.destroyer(destroyer)]
                        elif available_ships.small_transporter.amount < small_transporter and available_ships.large_transporter.amount < large_transporter:
                            print("Warning! Not enough: Small transporter",available_ships.small_transporter.amount, "of", small_transporter, "(",available_ships.small_transporter.amount - small_transporter, ")")
                            print("Warning! Not enough: Large transporter",available_ships.large_transporter.amount, "of", large_transporter, "(",available_ships.large_transporter.amount - large_transporter, ")")
                            EXP_SQUAD = [ships.small_transporter(available_ships.small_transporter.amount),ships.large_transporter(available_ships.large_transporter.amount),ships.light_fighter(light_fighter), ships.espionage_probe(espionage_probe),ships.cruiser(cruiser), ships.battleship(battleship), ships.reaper(reaper),ships.explorer(explorer),ships.destroyer(destroyer)]
                        else:
                            print("Something unexpected happened:( Consider to check out your fleet.")
            except Exception as e:
                print("Error, something went wrong:", e)
                empire.relogin(universe)
                time.sleep(random.randint(3,7))
                continue

            # sending expedition
            try:

                empire.send_fleet(mission=mission.expedition,id=planet_id,where=coordinates(galactic[0], random.choice(num_list), 16),ships=EXP_SQUAD,resources=[0, 0, 0],speed=speed.max,holdingtime=1)
                print(f"Expedition has ben launched!",)


            except Exception as e:
                print("Error, something went wrong:", e)
                empire.relogin(universe)
                time.sleep(random.randint(3,7))
                continue
            expeditions = [fleet for fleet in empire.fleet() if fleet.mission == mission.expedition]
            EXP_NUM = len(expeditions)
            if EXP_NUM != EXP_MAX:
                print(f"Available slots")
            time.sleep(random.randint(3,7))

        else:

            # get time to closest fleet return
            closest_time = min([ fleet.arrival for fleet in expeditions])
            print(f"No Available slots, program will wait until: {closest_time}.")
            time.sleep(random.randint(1, 3))
            # sleep to closest fleet return
            f"[EXP] program will wait until: {closest_time}."
            sleep_until(closest_time, 5)
expeditions = Thread(target=bot_expedition, args=(bot,))
expeditions.start()
