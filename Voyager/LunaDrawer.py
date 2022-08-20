import json
from tqdm import tqdm
from PIL import Image, ImageColor
# Opening JSON file
file = input("Enter .json name:")
with open(file, 'r') as f:
    distros_dict = json.load(f)
#stats
painted_plantes=int(0)
painted_moons=int(0)
x=[]
for gal in tqdm(range(1,8)):
    im = Image.new('RGB', (499, 16))
    for y in range(1,499):
        for z in range(1,16):
            pos=[gal,y,z,int(1)]
            pos_check=str(pos)
            for x in distros_dict:
                if str(x["planet_position"]) == pos_check:
                    im.putpixel((int(y), int(z)), ImageColor.getcolor('lightblue', 'RGB'))  # or whatever color you wish
                    painted_plantes=painted_plantes+1
                    if str(x["does_moon_exist"]) == "True":
                        im.putpixel((int(y), int(z)), ImageColor.getcolor('lightgoldenrodyellow', 'RGB'))  # or whatever color you wish
                        painted_moons=painted_moons+1
    image_file_name=("Image"+str(gal)+".png")
    im.save(image_file_name)  # or any image format
print("Done")
print("Painted: ", painted_plantes, "planets.")
percent_galaxy=(painted_plantes / (7*499*15)) * int (100)
print("Plantes are: ",round(percent_galaxy, 2),"% of galaxy")
percent_moons=(painted_moons/painted_plantes) * int(100)
print(round(percent_moons, 2),"% planets has moons.")