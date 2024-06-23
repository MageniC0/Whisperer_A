from PIL import Image
import json
import os

file_name = input("picture name:" ) + ".png"
map_name = input("map name:") + ".json"
trr_name = map_name  #...
print("loading...")

bitmap = Image.new( "RGBA", (49,49))
shadow_basic = Image.new('RGBA', (13, 13), (0,0,0,0))
shadow_image = shadow_basic.copy()

with open('trr.json', 'r', encoding='utf-8') as f:
    trr = json.load(f)

shadow = {}  
folder_path = "sors"
for i in range(65536):
    u = str(hex(i))
    shadow_name = f"{u}.png"
    if os.path.exists(file_path)：
        img = Image.open(file_path)
        file_path = os.path.join(folder_path, shadow_name)
        img = Image.open(file_path)
        shadow[f'{i}'] = img
    else:
        shadow[f'{i}'] = 0

trrsz = trrsy = 1
trr_near = [[[0,0,0,0,0,0] for _ in range(6)] for _ in range(6)]
for trrz in range(4):
    trrsy = trrz + 1
    for trry in range(4):
        trrsz = trry + 1
        for trrx in range(4):
            if trr[trrz][trry][trrx] != "ffff":
                trr_near[trrsy][trrsz][trrx+1] = 1

for z_with in range(4):
    for y_with in range(4):
        for x_with in range(4):
            if(trr[z_with][y_with][x_with]):
                map_x = 18 - 6 * x_with + 6 * y_with
                map_y = 24 + 2 * x_with + 2 * y_with - 8 * z_with
                x = x_with + 1
                y = y_with + 1
                z = z_with + 1
                near = [
                    trr_near[z][y][x+1],
                    trr_near[z][y][x-1],
                    trr_near[z][y+1][x],
                    trr_near[z][y-1][x],
                    trr_near[z+1][y][x],
                    trr_near[z-1][y][x],
                    trr_near[z][y-1][x+1],
                    trr_near[z][y+1][x-1]
                   ]

                h1 = tb[0] + 2 * tb[1] + 4 * tb[2] + 8 * tb[3]+ 16 * tb[4] + 32 * tb[5] + 64 * tb[6] + 128 * tb[7]
                h2 = hex(h1+4352)
                shadow_image = shadow{h2}
                
                cube = Image.open(trr[z_with][y_with][x_with]+".png")
                if trr[z_with][y_with][x_with] != "ffff":
                    cube.alpha_composite(shadow_image)
                
                bitmap.alpha_composite(cube,(map_x,map_y))
                
                shadow_image = shadow_basic.copy()

bitmap.save(file_name)
bitmap.show()
print(f"saved as {file_name}.")