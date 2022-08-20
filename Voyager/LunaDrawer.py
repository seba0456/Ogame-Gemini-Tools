import json
from time import sleep
from tqdm import tqdm
from PIL import Image, ImageColor
# Opening JSON file
a = 1
while a == 1:
    file = input("Enter .json name:")
    try:
        with open(file, 'r') as f:
            distros_dict = json.load(f)
            a = 0
    except:
        print("Invalid file name, please try again...")
#stats
painted_plantes=int(0)
painted_moons=int(0)
x=[]
for gal in tqdm(range(1,8)):
    im = Image.new('RGB', (499, 15))
    for y in range(1,501):
        for z in range(1,16):
            pos=[gal,y,z,int(1)]
            pos_check=str(pos)
            for x in distros_dict:
                if str(x["planet_position"]) == pos_check:
                    im.putpixel((int(y-1), int(z-1)), ImageColor.getcolor('lightblue', 'RGB'))  # or whatever color you wish
                    painted_plantes=painted_plantes+1
                    if str(x["does_moon_exist"]) == "True":
                        im.putpixel((int(y-1), int(z-1)), ImageColor.getcolor('lightgoldenrodyellow', 'RGB'))  # or whatever color you wish
                        painted_moons=painted_moons+1
    sleep(5)
    image_file_name=("Image"+str(gal)+".png")
    im.save(image_file_name)  # or any image format
print("Done")
print("Painted: ", painted_plantes, "planets.")
percent_galaxy=(painted_plantes / (7*499*15)) * int (100)
print("Plantes are: ",round(percent_galaxy, 2),"% of galaxy")
percent_moons=(painted_moons/painted_plantes) * int(100)
print(round(percent_moons, 2),"% planets has moons.")
