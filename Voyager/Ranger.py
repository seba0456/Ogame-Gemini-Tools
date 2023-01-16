import json
from time import sleep
from tqdm import tqdm
from PIL import Image, ImageColor
from configparser import ConfigParser
import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG)
cfg = ConfigParser()
cfg.read('config.ini')
gal_size = int(cfg.get('misc','gal_size'))+1
scan_range= int(cfg.get('ranger','scan_range'))
minimum_rank= int(cfg.get('ranger','minimum_rank'))
results=int(cfg.get('ranger','results'))
maximum_rank=int(cfg.get('ranger','maximum_rank'))
ingore_vacat=int(cfg.get('ranger','ingore_vacat'))
# Opening JSON file
a = 1
while a == 1:
    file = input("Enter .json name:")
    try:
        with open(file, 'r') as f:
            distros_dict = json.load(f)
            a = 0
    except:
        print("Invalid file name, please try again...")
#stats
x=[]
systems = []
planets=0
for gal in range(1,gal_size):
    systems = []
    for y in tqdm(range(6,497)):
        for z in range(1,16):
            pos=[gal,y,z,int(1)]
            pos_check=str(pos)
            for x in distros_dict:
                if str(x["planet_position"]) == pos_check:
                    if x["player_rank"] is not None:
                        if str(x["player_status"]) != "['vacation']":
                            if int(x["player_rank"]) < minimum_rank:
                                planets = planets + 1
                                if int(x["player_rank"]) < maximum_rank:
                                    planets = planets + (maximum_rank - int(x["player_rank"]))
                                #print(int(x["player_rank"]), "so planets are: ", planets, "galaxy is: ", gal, " system is: ", y )
                        elif ingore_vacat==0:
                            if int(x["player_rank"]) < minimum_rank:
                                planets = planets + 1
                                #print(str(x["player_name"])," on vacation")
                                if int(x["player_rank"]) < maximum_rank:
                                    planets = planets + (maximum_rank - int(x["player_rank"]))
                    else:
                        player_rank = None

        #print(y, "has: ",planets)
        systems.append((y, planets))
        planets=0

    sums = []

    for i in range(scan_range, len(systems) - scan_range):
        liczba_planet = systems[i][1]
        for j in range(i - scan_range, i + scan_range + 1):
            liczba_planet += systems[j][1]
        sums.append((systems[i][0], liczba_planet))

    sums.sort(key=lambda x: x[1])
    sleep(0.5)
    print("The smallest crowded systems in galaxy ",gal)
    for i in range(results):
        print(sums[i][0], sums[i][1])
sleep(3)

exec(open('Launch.py').read())
