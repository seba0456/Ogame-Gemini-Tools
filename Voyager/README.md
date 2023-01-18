# What is Voyager
Voyager is a faction of the Gemini bot that deals with galaxy scanning. A full galaxy scan takes about 30 minutes, although this depends on the size of the galaxy. The results of the scan are saved in a .json file.
Before running the bot, install PIL

```
python3 -m pip install --upgrade pip

python3 -m pip install --upgrade Pillow

python -m pip install ujson
```

The bot is activated with the command 
> python Launch.py
## I advise against using this on the main account
### The scan costs 35k deuterium.
#### How to use
The program is fired up using the Launch.py file. The following commands are available for now:
>help

The program will list the available commands

>voyager scout

It scans the entire universe and saves the result to a .json file. The scan takes an average of 8 to 9 minutes per galaxy.

>voyager report

Lists information on the selected player 

>voyager draw

It creates a galaxy map, giving each galaxy its own file. Once the files have been generated, it creates a mosaic. The galaxies in the mosaic are separated by one pixel. Each galaxy map is 499x15 in size.

>voyager ranger

It lists the least crowded systems in each galaxy.

## How to configure the program

>scan_range = 6

Range of checking neighboring layouts. E.g. Checks 6 systems to the "left" and 6 layouts to the "right".

>minimum_rank = 600

This is the lowest player rank to be considered by the program, players with a rank of 600< will not be included in the planet counting.

>maximum_rank = 200

This is the upper limit, launderers in this case between 1-200 will be avoided, the higher the rank the more 'hot' the planet. If you set it to 0, the program will not avoid high rank.

>results = 5

This variable defines the number of results.

## The rest of the configuration for most modules

The program (except scout) always asks for a json file.
The file must be in the same folder as the .py file!!!
The file looks like this
>universe_date.json

>gal_size = 0

This variable is responsible for the size of the galaxy, please specify the size of the universe.
