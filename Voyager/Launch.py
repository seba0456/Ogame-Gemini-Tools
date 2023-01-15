print('_' * 80)
print("Voyager is online, type help for commands")
i=0
while i == 0:
    mode=input()
    if mode ==str("voyager scout"):
        exec(open('Voyager.py').read())
    elif mode ==str("voyager report"):
        exec(open('Luna.py').read())
    elif mode ==str("voyager draw"):
        exec(open('LunaDrawer.py').read())
    elif mode ==str("voyager ranger"):
        exec(open('Ranger.py').read())
    elif mode ==str("voyager abort"):
        i = 1
    elif mode ==("help"):
        print('_' * 80)
        print("voyager scout", "   ", "--- Scan universe and save it to file .JSON")
        print("voyager report", "  ", "--- Reads data from .JSON file and show details about player.")
        print("voyager draw", "    ", "--- Reads data from .JSON file and creates universe map")
        print("voyager ranger", "    ", "--- Reads data from .JSON file and lists most isolated systems")
        print("voyager abort", "   ", "--- Closes program")
        print('_' * 80)
    else:
        print("Unsupported")
