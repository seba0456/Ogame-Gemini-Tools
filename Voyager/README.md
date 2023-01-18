# Co to Voyager
Voyager to odłam bota Gemini zajmujący się skanowaniem galaktyki. Pełen skan galaktyki trwa około 30 minut, choć jest to zależne od wielkości galaktyki. Wyniki skanu są zapisywane w pliku .json.
Przed uruchomieniem bota zainstaluj PIL

```
python3 -m pip install --upgrade pip

python3 -m pip install --upgrade Pillow

python -m pip install ujson
```

Bota aktywujemy komendą 
> python Launch.py
## Odradzam używanie  tego na głównym koncie
### Skan kosztuje 35k deuteru.
#### Jak używać
Program odpalamy za pomocą pliku Launch.py. Na teraz dostępne są następujące komendy:
>help

Program wypisze tryby działania
>voyager scout

Skanuje całe uniwersum i zapisuje rezultat do pliku .json. Skan trwa średnio od 8 do 9 minut na galaktykę.

>voyager report

Wypisuje informacje na temat wskazanego gracza 

>voyager draw

Tworzy mapę galaktyki, dając każdej galaktyce własny plik. Po wygenerowaniu plików, tworzy mozaikę. Galaktyki w mozaice są oddzielone jednym pikselem. Każda mapa galaktyki ma rozmiar 499x15.

>voyager ranger

Wypisuje najmniej zatłoczone układy w każdej galaktyce.

## Jak skonfigurować program

>scan_range = 6

Zasięg sprawdzania sąsiednich układów. Np. Sprawdza 6 układów w „lewo” i 6 układów w „prawo”.

>minimum_rank = 600

To najniższa ranga gracza, która ma uwzględnić program, graczy o randze 600< nie uwzględni do liczenia planet

>maximum_rank = 200

To góra granica, pracze w tym wypadku z przedziału 1-200 będą unikani, im wyższa ranga tym bardziej „gorąca” planeta. Jeśli ustawisz na 0, program nie będzie unikał wysokiej rangi.

>results = 5

Ta zmienna definiuje liczbę wyników. 

## Reszta konfiguracji dla większości programów

Program (oprócz scout) zawsze pyta o plik json
Plik musi być w tym samym folderze co plik .py!!!
Wygłada ona tak
>nazwapliku.json

>gal_size = 0

Ta zmienna odpowiada za rozmiar galaktyki, proszę podać rozmiar uniwersum.
Program (oprócz scout) zawsze pyta o plik json
Plik musi być w tym samym folderze co plik .py!!!

