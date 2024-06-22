#预处理
from PIL import Image
print("loading...")
basic_image = Image.open("0001.png")#要堆叠的方块
bitmap = Image.new( "RGBA", (49,47))#4*4*4画布
shadow_basic = Image.new('RGBA', (13, 13), (0,0,0,0))#表面渲染空间
cube = cell.copy()#直接堆叠物
shadow_image = shadow_basic.copy()#对于直接堆叠物的最终表面渲染

terraria = [[[0 for _ in range(4)]for _ in range(4)]for _ in range (4)]

#任务表
terraria = [
    #z = 1
    [[1,1,1,1],
     [1,1,1,1],
     [1,1,1,1],
     [1,0,0,0]],
    #z = 2
    [[1,0,0,1],
     [1,0,0,0],
     [1,0,0,0],
     [1,0,0,0]],
    #z = 3
    [[1,0,0,1],
     [1,0,0,0],
     [1,0,0,0],
     [1,0,0,0]],
    #z = 4
    [[1,1,1,1],
     [1,0,0,0],
     [1,0,0,0],
     [1,0,0,0]]
]

trrsz = trrsy = 1
terraria_basic = [[[0,0,0,0,0,0] for _ in range(6)] for _ in range(6)]
for trrz in range(4):
    trrsy = trrz + 1
    for trry in range(4):
        trrsz = trry + 1
        for trrx in range(4):
            terraria_basic[trrsy][trrsz][trrx+1] = terraria[trrz][trry][trrx]

left_side = {(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10)}
right_side = {(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10)}
in_mid = {(6,5),(6,6),(6,7),(6,8),(6,9),(6,10),(6,11),(6,12)}
in_tot = {(3,4),(3,5),(4,4),(4,5),(5,5),(5,6)}
left_back = {(2,1),(3,1),(4,1),(5,0),(6,0)}
right_back = {(6,0),(7,0),(8,1),(9,1),(10,1)}
left_down = {(0,10),(1,10),(2,11),(3,11),(4,11),(5,12)}
right_down = {(7,12),(8,11),(9,11),(10,1),(11,10),(12,10)}

#数据传送
file_name = input("name:" ) + ".png"
print("loading terrain...")
for z_with in range(4):
    for y_with in range(4):
        for x_with in range(4):
            if(terraria[z_with][y_with][x_with]):
                map_x = 18 - 6 * x_with + 6 * y_with
                map_y = 24 + 2 * x_with + 2 * y_with - 8 * z_with
                x = x_with + 1
                y = y_with + 1
                z = z_with + 1
                near = [terraria_basic[z][y][x+1],terraria_basic[z][y][x-1],terraria_basic[z][y+1][x],terraria_basic[z][y-1][x],terraria_basic[z+1][y][x],terraria_basic[z-1][y][x],terraria_basic[z][y+1][x-1],terraria_basic[z][y-1][x+1]]
                shadow_task = {}
                if(near[0] == 0 and near[3] == 0 and near[6] == 0):
                    shadow_task.update(left_side)
                if(near[1] == 0 and near[2] == 0 and near[7] == 0):
                    shadow_task.update(right_side)
                if(near[0] == 0 and near[2]== 0):
                    shadow_task.update(in_mid)
                    if(near[4] == 0):
                        shadow_task.update(in_tot)
                if(near[4] == 0):
                    if(near[3] == 0):
                        shadow_task.update(left_back)
                    if(near[1] == 0):
                        shadow_task.update(right_back)
                if(near[5] == 0):
                    if(near[0] == 0):
                        shadow_task.update(left_down)
                    if(near[2] == 0):
                        shadow_task.update(right_down)
                for shadow_pixel in shadow_task:
                    shadow_image.putpixel(shadow_pixel,(0,0,0,63))
                cube.alpha_composite(shadow_image)
                bitmap.alpha_composite(cube,(map_x,map_y))
                shadow_image = shadow_basic.copy()
                cube = basic_image.copy()
#完成
bitmap.save(file_name)
bitmap.show()
print(f"saved as {file_name}.")