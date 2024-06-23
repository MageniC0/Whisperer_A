from PIL import Image
import json
import os

#选项
file_name = input("picture name:" ) + ".png"
trr_name = input("map name:") + ".json"
print("loading...")

#加载画布
bitmap = Image.new( "RGBA", (49,49))
shadow_basic = Image.new('RGBA', (13, 13), (0,0,0,0))
shadow_image = shadow_basic.copy()

#加载地形
with open(trr_name, 'r', encoding='utf-8') as f:
    trr = json.load(f)

#加载资源文件
shadow = {}  
for i in range(65536):
    u = str(hex(i))
    shadow_name = f"{u}.png"
    file_path = os.path.join("sors", shadow_name)
    loading = Image.open(file_path)
    if os.path.exists(file_path):
        loading = Image.open(file_path)
        shadow[f'{i}'] = loading
    else:
        shadow[f'{i}'] = 0

#加载渲染表
trrsz = trrsy = 1
trr_near = [[[0,0,0,0,0,0] for _ in range(6)] for _ in range(6)]
for trrz in range(4):
    trrsy = trrz + 1
    for trry in range(4):
        trrsz = trry + 1
        for trrx in range(4):
            if trr[trrz][trry][trrx] != "ffff":
                trr_near[trrsy][trrsz][trrx+1] = 1

#数据传送
for z_with in range(4):
    for y_with in range(4):
        for x_with in range(4):
            #对于每一个方块
             cube_name = trr[z_with][y_with][x_with]
             if cube_name != 0 :
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
                #表面渲染
                h1 = near[0] + 2 * near[1] + 4 * near[2] + 8 * near[3]+ 16 * near[4] + 32 * near[5] + 64 * near[6] + 128 * near[7]
                h2 = hex(h1+4352)
                shadow_image = shadow[h2]
                
                #图形
                cube = shadow[cube_name]
                
                cube.alpha_composite(shadow_image,(0,0))
                bitmap.alpha_composite(cube,(map_x,map_y))

                shadow_image = shadow_basic.copy()

bitmap.save(file_name)
bitmap.show()
print(f"saved as {file_name}.")