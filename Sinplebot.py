from ogame import OGame
from ogame.constants import destination, coordinates, ships, mission, speed, buildings, status, fleet
from bs4 import BeautifulSoup
from threading import Thread, Event
import datetime
import time
import random
import re
from ogame.constants import resources
res = resources(metal=1, crystal=2, deuterium=3)
[1, 2, 3]
# funcja wspomagająca usypianie dopóki nie nastąpi czas powrotu expa
def sleep_until(target, delay=0):
    now = datetime.datetime.now()
    delta = target - now

    if delta > datetime.timedelta(0):
        time.sleep(delta.total_seconds() + delay)
        return True

# moduł logowania
print("******************************")
print("Witaj w Atopilot AE 1.3 + Fleetsave by LeafQ")
print("******************************")
log_in = ''
haselko = ''
uniwerka = 'Belinda'


# narzędzie logowania
bot = OGame(uniwerka,log_in,haselko)


print("Pomślnie zalogowano konto:", log_in)
print("Wybrane Uniwersum:", uniwerka)
print("______________________________")

# id obiektu
id = 33651601
dol_gala = bot.celestial_coordinates(id)


#ilosc_exp = input("Ilość ekspedycji w tym samym czasie:")
print("______________________________")
#ilo_mt = input("podaj ilość MT na ekspedycje:")

# zmienne
EXP_MAX = int(5)
EXP_ST = int(200)
EXP_DT = int(200)
EXP_SRC = id
baza_ukl = [394,395,396]
FS_EMPIRE = int(33651601)
FS_ukl = [380]

exp_pio = int(1)

print("Floty wysyłane losowo w układy:", baza_ukl)
print("Zaplanowanych", EXP_MAX, "ekspedycji.")
print("______________________________")

# funkcja wysyłania ekspedycji
def bot_expedition(empire, UNI=uniwerka):
    print("[EXP] Proces wysyłania ekspedycji rozpoczęty.")

    while 1:
        expeditions = []
        
        # sprawdzanie dostępnych slotów ekspedycji (różnica latających i podanych)
        try:
            expeditions = [fleet for fleet in empire.fleet() if fleet.mission == mission.expedition]
            EXP_NUM = len(expeditions)
            time.sleep(2)

        except:
            print("[EXP] Error. Relogowanie...")
            empire.relogin(UNI)
            time.sleep(random.randint(3,7))
            continue

        # jeśli są dostępne sloty
        if EXP_NUM < int(EXP_MAX):
            print("[EXP] Dostępne Sloty ekspedycji.")

            # sprawdzanie dostępności statków
            try:
                available_ships = empire.ships(EXP_SRC)

                if available_ships.small_transporter.amount >= EXP_ST:
                    EXP_SQUAD = [ships.large_transporter(EXP_ST),ships.explorer(exp_pio),ships.battleship(1)]
                else:
                    EXP_SQUAD = [ships.large_transporter(EXP_DT),ships.explorer(exp_pio),ships.battleship(1)]

            except:
                print("[EXP] Error. Relogowanie...")
                empire.relogin(UNI)
                time.sleep(random.randint(3,7))
                continue

            # wysyłanie ekspedycji
            try:
                empire.send_fleet(mission=mission.expedition,id=EXP_SRC,where=coordinates(dol_gala[0], random.choice(baza_ukl), 16),ships=EXP_SQUAD,resources=[0, 0, 0],speed=speed.max,holdingtime=1)
                print(f"[EXP] Ekspedycja wysłana.")

            except:
                print("[EXP] Error. Relogowanie...")
                empire.relogin(UNI)
                time.sleep(random.randint(3,7))
                continue

            print(f"[EXP] Dostępne wolne sloty ekspedycji, losowanie czasu wylotu.")
            time.sleep(random.randint(3,7))

        else:

            
            # znajdź czas powrotu pierwszej ekspedycji
            closest_time = min([ fleet.arrival for fleet in expeditions])
            print(f"[EXP] Brak dostępnych slotów. Ponownie uruchomienie: {closest_time}.")
    
            
            
            
            

             #LeafQMod  
            fleetsavestate=0
                
            atakstate=empire.attacked()
            print(f"[FS]", atakstate)
        if(atakstate==True):
                print(f"[FS] Proces wysyłania fleetsave rozpoczęty.")
                try:
                    shi = empire.ships(FS_EMPIRE)
                    light_fighter_avaible = int(shi.light_fighter.amount)
                    heavy_fighter_avaible = int(shi.heavy_fighter.amount)
                    cruiser_avaible = int(shi.cruiser.amount)
                    battleship_avaible = int(shi.battleship.amount)
                    interceptor_avaible = int(shi.interceptor.amount)
                    bomber_avaible = int(shi.bomber.amount)
                    destroyer_avaible = int(shi.destroyer.amount)
                    deathstar_avaible = int(shi.deathstar.amount)
                    reaper_avaible = int(shi.reaper.amount)
                    explorer_avaible = int(shi.explorer.amount)
                    small_transporter_avaible = int(shi.small_transporter.amount)
                    large_transporter_avaible = int(shi.large_transporter.amount)
                    colonyShip_avaible = int(shi.colonyShip.amount)
                    recycler_avaible = int(shi.recycler.amount)
                    espionage_probe_avaible = int(shi.espionage_probe.amount)
                    solarSatellite_avaible = int(shi.solarSatellite.amount)
                    crawler_avaible = int(shi.crawler.amount)

                    #Co idzie na FS
                    FS_SQUAD = [
                        ships.light_fighter(light_fighter_avaible),
                        ships.heavy_fighter(heavy_fighter_avaible),
                        ships.cruiser(cruiser_avaible),
                        ships.battleship(battleship_avaible),
                        ships.interceptor(interceptor_avaible),
                        ships.bomber(bomber_avaible),
                        ships.explorer(explorer_avaible),
                        ships.small_transporter(small_transporter_avaible),
                        ships.large_transporter(large_transporter_avaible),
                        ships.colonyShip(colonyShip_avaible),
                        ships.espionage_probe(espionage_probe_avaible)]
                    empire.resources(FS_EMPIRE)
                    res = empire.resources(FS_EMPIRE)
                    deuter_avaible = res.deuterium-100000
                    metal_avaible = res.metal
                    crystal_avaible = res.crystal
                    #koordynaty oraz surowce
                    empire.send_fleet(mission=mission.spy,id=EXP_SRC,where=coordinates(dol_gala[0], random.choice(FS_ukl), 16),ships=FS_SQUAD,resources=[metal_avaible, crystal_avaible, deuter_avaible],speed=speed.min)
                    print(f"[FS] Fleetsave zostal pomyslnie wyslany")
                except:
                    print("[FS] Error. Ponawianie FS...")
                    empire.relogin(UNI)
                    time.sleep(random.randint(3,7))
                    continue
        else:
            print(f"[FS] Fleetsave nie jest potrzebny.")
            # uśpienie programu do czasu powrotu pierwszej ekspedycji + 5s opóźnienia dla bezpieczeństwa
            
        f"[EXP] Usypiam do: {closest_time}."
        time.sleep(30)
    
    # uruchamianie procesu wysyłania ekspedycji
expeditions = Thread(target=bot_expedition, args=(bot,))
expeditions.start()

 
