echo This script will install all bot dependences.
sleep 3
pip install ogame==8.1.0.21 && pip install tqdm python3 -m && pip install --upgrade pip && python3 -m pip install --upgrade Pillow
sleep 6
echo make sure to edit config.ini
echo type something when you are ready to start bot
read name;
sleep 2
python main.py
