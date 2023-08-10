Update
======

From now on, the default branch is 'gemini'. The only supported branch (by me) is 'gemini'.

Ogame-Expedition Bot - Bot Configuration
----------------------------------------

Custom modification of existing code. The bot sends the specified number of expeditions. <br>Configure the bot in the config.ini file! <br>In lines 2-4, enter your login details. <br>In line 7, enter the ID of your planet/moon from which you'll be sending the expedition. <br>In the 'fleet' section, enter the number of ships, they are labeled in the comments. <br>In field 8, enter your system. <br>In field 9, enter the range within which you intend to operate; it should be (your system - target_system range) and (your system + target_system range). <br>To get the ID:

1.  Go to Ogame.
2.  Click on the planet you're interested in.
3.  Go to the "overview" tab.
4.  Check the address bar of the page.

> For example, <https://s180-pl.ogame.gameforge.com/game/index.php?page=ingame&component=overview&cp=33640732>

1.  The ID is after cp=, in this case, it's 33640732.

### Installation and preparation of the system for using the bot on Windows 10 or newer

1.  Launch Microsoft Store and search for the phrase: Python 3.9, published by Python Software Foundation
2.  Install Python 3.9
3.  Open CMD
4.  Type in CMD
5.  Move the file to C:/Users/YourUsername

#### Running the bot

1.  Open CMD
2.  Type

> python3 simplebot.py and press enter

#### Alternatively, running on Windows

1.  Run Launch.bat That's all, no file moving for the bot, just one file to run the bot ^^

### Installation and preparation of the system for using the bot on Windows 10 or newer

1.  Launch the terminal in the bot folder
2.  Install all required files using this command:

> ./InstallDependences.sh

The bot should start automatically after this, if you want to run only the bot, use:

> ./Gemini.sh

<br>Done! The bot has been successfully launched!
