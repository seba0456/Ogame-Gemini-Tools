from ogame import OGame
from ogame.constants import destination, coordinates, ships, mission, speed, buildings, status, fleet
from bs4 import BeautifulSoup
from threading import Thread, Event
import datetime
import time
import random
import re

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
log_in = 'krystian.zyczynski@gmail.com'
haselko = 'P@lonez123'
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
                    available_ships_fs = [ships.large_transporter(2)]
                    #Co idzie na FS
                    FS_SQUAD = available_ships_fs
                    #koordynaty oraz surowce
                    empire.send_fleet(mission=mission.spy,id=EXP_SRC,where=coordinates(dol_gala[0], random.choice(baza_ukl), 16),ships=FS_SQUAD,resources=[100, 100, 100],speed=speed.min)
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

 
