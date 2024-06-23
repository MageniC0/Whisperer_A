from PIL import Image
import json

file_name = input("picture name:" ) + ".png"
map_name = print("map name:") + ".json"
trr_name = map_name  #...
print("loading...")

bitmap = Image.new( "RGBA", (49,49))
shadow_basic = Image.new('RGBA', (13, 13), (0,0,0,0))
shadow_image = shadow_basic.copy()

with open('trr.json', 'r', encoding='utf-8') as f:
    trr = json.load(f)
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
                    trr_near[z][y+1][x-1]]
                
                shadow1 = near[0] + 2 * near[1] + 4 * near[2] + 8 * near[3]
                shadow1 = format(shadow1, 'x').zfill(1)
                shadow2 = near[4] + 2 * near[5] + 4 * near[6] + 8 * near[7]
                shadow2 = format(shadow2, 'x').zfill(1)
                
                shadow_name = f"ff{shadow2}{shadow1}.png"
                shadow_image = Image.open(shadow_name)
                
                cube = Image.open(trr[z_with][y_with][x_with]+".png")
                if trr[z_with][y_with][x_with] != "ffff":
                    cube.alpha_composite(shadow_image)
                
                bitmap.alpha_composite(cube,(map_x,map_y))
                
                shadow_image = shadow_basic.copy()

bitmap.save(file_name)
bitmap.show()
print(f"saved as {file_name}.")