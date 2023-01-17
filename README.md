# Ogame-Bot
Własna modyfikacja już istniejącego kodu. Bota można uruchomić na każdym urządzeniu z dostępem do internetu i zainstalowanym językiem Python.

Bot Gemini będzie mieć wiele modułów. Każdy z nich (wraz z instrukcjami) znajduje się w folderze:
1. Gemini zajmuje się wysyłaniem ekspedycji.
2. Voyager zajmuje się zdobywaniem informacji o statusie graczy oraz ich planetach oraz dawaniem wskazówek o najmniej tłocznych miejscach w uniwersum.

## Przyszłość bota
1. Moduł Gemini, z racji bycia wypartym przez [TBot](https://github.com/ogame-tbot/TBot), nie będzie już dalej rozwijany 😞
2. Moduł Voyager nie jest już defacto botem do Ogame, lecz zestawem narzędzi do ułatwienia sobie gry.

## Co program potrafi?
### Gemini
Aktualnie Gemini jest w stanie wysłać ekspedycję, wolne sloty ekspedycji oraz skład floty musimy wybrać sami. W najnowszej wersji dodałem moduł FS, ale nie testowałem go w praktyce, powinien działać 😂
### Voyager
#### Skan Uniwersum
Voyager zapisuje informacje o planetach, graczach do pliku JSON, plik ten jest później wykorzystywany przez program jako baza danych.
#### Informacje o graczu
Po wskazaniu pliku JSON, program pokaże wszystkie informacje na temat wskazanego gracza, w tym planety i jego księżyce.
#### Maluj mapę
Po wskazaniu pliku JSON, program wygeneruje mapę uniwersum.

![alt text](https://github.com/seba0456/Ogame-Gemini-Bot/blob/Gemini/Voyager/Results/Universe.png "Logo Title Text 1")

Na pierwszy rzut oka, mapa wydaje się być nieczytelna, ale ma rozmiary (15+1) * liczba galaktyk x 499, program też generuje pociętą wersję galaktyki, gdzie każdy piksel oznacza pozycję na mapie gry. Kolor czarny oznacza puste pole, kolor niebieski planetę, a żółty moon.

Potencjalne miejsca na kolonię
Program wypisuje najmniej tłoczne układy dla każdej galaktyki, unika graczy o wysokiej randze oraz nie bierze pod uwagę graczy o niskiej randze.
