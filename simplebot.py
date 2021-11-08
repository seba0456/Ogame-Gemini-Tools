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

# funcja wspomagająca usypianie dopóki nie nastąpi czas powrotu expa
def sleep_until(target, delay=0):
    now = datetime.datetime.now()
    delta = target - now

    if delta > datetime.timedelta(0):
        time.sleep(delta.total_seconds() + delay)
        return True

# moduł logowania
print("******************************")
print("Witaj w Atopilot AE 1.4")
print("******************************")
login = 'twoj@mail.com'
haslo = 'hasło-masło'
uniwersum = 'Belinda'


# narzędzie logowania
bot = OGame(uniwersum,login,haslo)
print("Pomślnie zalogowano konto:", login)
print("Wybrane Uniwersum:", uniwersum)
print("______________________________")

# id obiektu
id = 33640732
dol_gala = bot.celestial_coordinates(id)

# zmienne
EXP_MAX = int(7) #Wpisz tutaj maksymalną liczbę ekspedycji, jaką możesz wysłac
EXP_ST = int(3000) #Wpisz tutaj liczbę małych transportowców
EXP_DT = int(0) #Wpisz tutaj liczbę dużych transportowców 
exp_pio = int(1) #Wpisz tutaj liczbę pionierów
EXP_Reaper = int(1) #Wpisz tutaj liczbę rozprówaczy
baza_ukl = [365, 366, 367] #Wpisz tutaj układy w, których chcesz operować
EXP_SRC = id
Min_deuter_to_start = int(20000) #Wpisz tutaj średnią liczbę zużycia deuteru na jedną ekspedycje.

print("Floty zostaną wysyłane losowo w układy:", baza_ukl)
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
            print("[EXP] Dostępne Sloty ekspedycji.", EXP_NUM, " z ", EXP_MAX)

            # sprawdzanie dostępności statków
            try:
                available_ships = empire.ships(EXP_SRC)

                if available_ships.small_transporter.amount >= EXP_ST:
                    EXP_SQUAD = [ships.small_transporter(EXP_ST),ships.explorer(exp_pio),ships.reaper(EXP_Reaper)]
                else:
                    EXP_SQUAD = [ships.large_transporter(EXP_DT),ships.explorer(exp_pio),ships.reaper(EXP_Reaper)]

            except:
                print("[EXP] Error. Relogowanie...")
                empire.relogin(UNI)
                time.sleep(random.randint(3,7))
                continue

            # wysyłanie ekspedycji
            try:
                empire.resources(id)
                res = empire.resources(id)
                deuter_avaliable = res.deuterium
                if deuter_avaliable >= Min_deuter_to_start:
                    empire.send_fleet(mission=mission.expedition,id=EXP_SRC,where=coordinates(dol_gala[0], random.choice(baza_ukl), 16),ships=EXP_SQUAD,resources=[0, 0, 0],speed=speed.max,holdingtime=1)
                    print(f"[EXP] Ekspedycja wysłana.",)
                else:
                    print(f"[EXP] Błąd, brak deuteru! Proszę uzupełnić deuter!")

            except:
                print("[EXP] Error. Relogowanie...")
                empire.relogin(UNI)
                time.sleep(random.randint(3,7))
                continue
            expeditions = [fleet for fleet in empire.fleet() if fleet.mission == mission.expedition]
            EXP_NUM = len(expeditions)
            if deuter_avaliable < Min_deuter_to_start:
                print(f"[EXP] Proszę uzupełnić deuter! Ponawiam próbę wysłania floty.")
            elif EXP_NUM != EXP_MAX:
                print(f"[EXP] Dostępne są sloty ekspedycji, wysyłam flotę...")
            time.sleep(random.randint(3,7))

        else:

            # znajdź czas powrotu pierwszej ekspedycji
            closest_time = min([ fleet.arrival for fleet in expeditions])
            print(f"[EXP] Brak dostępnych slotów. Ponownie uruchomienie: {closest_time}.")

            # uśpienie programu do czasu powrotu pierwszej ekspedycji + 5s opóźnienia dla bezpieczeństwa
            f"[EXP] Usypiam do: {closest_time}."
            sleep_until(closest_time, 5)

# uruchamianie procesu wysyłania ekspedycji
expeditions = Thread(target=bot_expedition, args=(bot,))
expeditions.start()
