#预处理
from PIL import Image
sh = Image.new('RGBA', (13, 13), (0,0,0,0))

#渲染判定
x = 2
y = 3
z = 1
d = [trrs[z][y][x+1],trrs[z][y][x-1],trrs[z][y+1][x],trrs[z][y-1][x],trrs[z+1][y][x],trrs[z-1][y][x],trrs[z][y+1][x-1],trrs[z][y-1][x+1]]

#任务表[渲染列]
l = [(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10)]
r = [(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10)]
m = [(6,5),(6,6),(6,7),(6,8),(6,9),(6,10),(6,11),(6,12)]
n = [(3,4),(3,5),(4,4),(4,5),(5,5),(5,6)]
lb = [(2,1),(3,1),(4,1),(5,0),(6,0)]
rb = [(6,0),(7,0),(8,1),(9,1),(10,1)]
ld = [(0,10),(1,10),(2,11),(3,11),(4,11),(5,12)]
rd = [(7,12),(8,11),(9,11),(10,1),(11,10),(12,10)]

#函数[表面渲染]
def s():
    p = []
    pixels = []
    if(d[0] and d[3] and d[6]):
        p += l
    if(d[1] and d[2] and d[7]):
        p += r
    if(d[0] and d[2]):
        p += m
        if(d[4]):
            p += n
    if(d[4]):
        if(d[3]):
            p += lb
        if(d[3]):
            p += rb
    if(d[5]):
        if(d[0]):
            p += ld
        if(d[2]):
            p += rd
    for u in p:
        sh.putpixel(u,(0,0,0,63))

#函数[放置方块]
def block(a,b,c):
    m = 18 - 6 * a + 6 * b
    n = 24 + 2 * a + 2 * b - 8 * c
    s()
    cube.alpha_composite(sh)
    back.alpha_composite(cube,(m,n))

#创建文件
name = input("name:" ) + ".png"

#数据传送
print("loading terrain...")
for z in range(4):
    for y in range(4):
        for x in range(4):
            if(trr[z][y][x] != 0):
                block(x,y,z)

#完成
back.save(name )
back.show()
print(f"saved as {name}.")