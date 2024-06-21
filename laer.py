#须要有”0001.png”

#预处理
from PIL import Image
print("loading...")
cube = Image.open("0001.png")
back = Image.new( "RGBA", (49,47))
sh = Image.new('RGBA', (13, 13), (0,0,0,0))

#任务表
trr = [
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
i = j = 1
trrs = [[[0,0,0,0,0,0] for _ in range(6)] for _ in range(6)]
for zh in range(4):
    j = zh + 1
    for yh in range(4):
        i = yh + 1
        for xh in range(4):
            trrs[j][i][xh+1] = trr[zh][yh][xh]
l = [(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10)]
r = [(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10)]
m = [(6,5),(6,6),(6,7),(6,8),(6,9),(6,10),(6,11),(6,12)]
n = [(3,4),(3,5),(4,4),(4,5),(5,5),(5,6)]
lb = [(2,1),(3,1),(4,1),(5,0),(6,0)]
rb = [(6,0),(7,0),(8,1),(9,1),(10,1)]
ld = [(0,10),(1,10),(2,11),(3,11),(4,11),(5,12)]
rd = [(7,12),(8,11),(9,11),(10,1),(11,10),(12,10)]

#数据传送
name = input("name:" ) + ".png"
print("loading terrain...")
for z in range(4):
    for y in range(4):
        for x in range(4):
            if(trr[z][y][x]):
                m = 18 - 6 * x + 6 * y
                n = 24 + 2 * x + 2 * y - 8 * z
                d = [trrs[z][y][x+1],trrs[z][y][x-1],trrs[z][y+1][x],trrs[z][y-1][x],trrs[z+1][y][x],trrs[z-1][y][x],trrs[z][y+1][x-1],trrs[z][y-1][x+1]]
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
                    print(p)
                cube.alpha_composite(sh)
                back.alpha_composite(cube,(m,n))


