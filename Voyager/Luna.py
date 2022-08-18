import json
# Opening JSON file
file = input("Enter .json name:")
target = input("Enter player name that you are looking for:")
with open('test.json', 'r') as f:
    distros_dict = json.load(f)
x=[]
run_once = 1
for x in distros_dict:
    if x["player_name"]== target:
        while run_once:
            if run_once == 1:
                print("Player name: ", target)
                print("Player rank: ", x["player_rank"])
                print("Player alliance: ", x["player_alliance"])
                if x["player_status"] =="['vacation']":
                    print("Player on vacation")
                print("Planets: ")
                print('―' * 30)
                run_once = 0
planets=int(0)
for x in distros_dict:
    if x["player_name"] == target:
        planets=planets+1
        print("Planet name:", x["planet_name"])
        planet_pos = str(x["planet_position"])
        pos=planet_pos.strip(" ,1]")+str("]")
        print("Planet position: ", pos)
        if str(x["does_moon_exist"]) == "True":
            print("Planet has moon.")
        print('―' * 10)
if planets !=0:
    print("Player has:", str(planets)+".")
else:
    print("Player not found!")
