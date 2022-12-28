# Aktualizacja
Od teraz domyślnym branchem jest gemini. Jedynym wspieranym (przezemnie branchem jest gemini).
## Ogame-Expedition Bot koniguracja bota
Własna modyfikacja już istniejącego kodu.
Bot wysyła wskazaną liczbę ekspedycji.
<br>Bota konfigurujemy w pliku config.ini!
<br>W liniach 2-4 wpisujemy dane logowania.
<br>W lini 7 wpisujemy ID swojej planety/moona z której będziemy wysyłać ekspedycję.
<br>W sekcji fleet wpisujemy liczbę statków, oznaczone są one w komentarzach .
<br>W polu 8 wpisujemy nasz układ.
<br>W polu 9 wpisujemy zasięg w, kótrych mamy zamiar operować zasięgo to: (nasz układ - target_system range) i  (nasz układ + target_system range).
<br>Aby zdobyć ID musimy:
1. Wejść do Ogame.
1. Klinkąć na interesującą nas planetę.
1. Wejść w zakładkę "podgląd".
1. Wejść w pasek adresu storny.     
> Przykładowo https://s180-pl.ogame.gameforge.com/game/index.php?page=ingame&component=overview&cp=33640732
5. ID znajduje się po cp=, w tym przypadku to 33640732.
### Instalacja oraz przygotowywanie systemu do używania bota w systemie Windows 10 lub nowszym
1. Uruchom Microsoft Store oraz wyszukaj frazę: Python 3.9, którego wydawcą jest Python Software Foundation 
2. Zainstaluj program Python 3.9
3. Uruchom CMD
4. Wpisz w CMD 
> pip install ogame==8.1.0.21

> pip install tqdm
5. Wciśnij Enter i zaczekaj na ukończenie pobierania pakietu
6. Pobierz plik .py z tej strony
7. Przenieś plik do C:/Users/TwojaNazwaUżytkownika
#### Uruchamianie bota
1. Uruchom CMD
2. Wpisz 
> python3 simplebot.py i naciśnij enter
#### Alternatywnie uruchamianie na windowsie
1. Uruchom Launch.bat
I to tyle żadnego przenoszenia plików z botem, nic tylko jeden plik do odpalenia bota ^^

### Instalacja oraz przygotowywanie systemu do używania bota w systemie Windows 10 lub nowszym
1. Uruchom terminal w folderze bota
2. Zainstaluj wszystkie wymagane pliki za pomocą tej komendy:
> ./InstallDependences.sh
Bot powinien wystartować po tym automatycznie, jeśli chcesz odpalić tylko bota użyj:
> ./Gemini.sh
<br>Gotowe! Bot został Pomyślnie uruchomiony!
