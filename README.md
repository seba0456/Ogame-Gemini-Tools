# Ogame-Bot
A modification of existing code that is one's own. The bot can be run on any device with internet access and Python installed.

The Gemini bot will have multiple modules. Each one of them (along with instructions) is located in the folder:
1. Gemini is responsible for dispatching expeditions.
2. Voyager is responsible for gathering information about the status of players and their planets, and giving tips about the least crowded places in the universe.

## The future of the bot.
1. Due to being replaced by another solution, the Gemini module will no longer be further developed. 😞
2. The Voyager module is no longer a bot for Ogame, but rather a set of tools to make the game easier for oneself.

## What can the program do?
### Gemini
Currently, Gemini is capable of sending expeditions. The free slots of expeditions and the fleet composition must be selected by us. In the latest version, I added the FS module, but I haven't tested it in practice, it should work 😂
### Voyager
#### Universe scan
Voyager saves information about planets and players to a JSON file, which is later used by the program as a database.
#### Information about the player.
After indicating the JSON file, the program will show all information about the indicated player, including his planets and moons.
#### Draw map
After indicating the JSON file, the program will generate a map of the universe.

![alt text](https://github.com/seba0456/Ogame-Gemini-Bot/blob/Gemini/Voyager/Results/Universe.png "Logo Title Text 1")

At first glance, the map seems to be unreadable, but it has dimensions (15+1) * number of galaxies x 499, the program also generates a cropped version of the galaxy, where each pixel represents a position on the game map. The color black represents an empty field, blue represents a planet, and yellow represents a moon.

#### Potential colony locations.
The program lists the least crowded systems for each galaxy, avoiding high-ranked players and not taking into account low-ranked players.

## How to install
Run this command in your terminal.
```
pip install -r requirements.txt
```
