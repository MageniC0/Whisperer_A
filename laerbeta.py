#预处理
from PIL import Image
print("loading...")
cell = Image.open("0001.png")
back = Image.new( "RGBA", (49,47))
shc = Image.new('RGBA', (13, 13), (0,0,0,0))
cube = cell.copy()
sh = shc.copy()

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
l = {(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10)}
r = {(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10)}
m = {(6,5),(6,6),(6,7),(6,8),(6,9),(6,10),(6,11),(6,12)}
n = {(3,4),(3,5),(4,4),(4,5),(5,5),(5,6)}
lb = {(2,1),(3,1),(4,1),(5,0),(6,0)}
rb = {(6,0),(7,0),(8,1),(9,1),(10,1)}
ld = {(0,10),(1,10),(2,11),(3,11),(4,11),(5,12)}
rd = {(7,12),(8,11),(9,11),(10,1),(11,10),(12,10)}

#数据传送
name = input("name:" ) + ".png"
print("loading terrain...")
for zu in range(4):
    for yu in range(4):
        for xu in range(4):
            if(trr[zu][yu][xu]):
                mh = 18 - 6 * xu + 6 * yu
                nh = 24 + 2 * xu + 2 * yu - 8 * zu
                x = xu + 1
                y = yu + 1
                z = zu + 1
                d = [trrs[z][y][x+1],trrs[z][y][x-1],trrs[z][y+1][x],trrs[z][y-1][x],trrs[z+1][y][x],trrs[z-1][y][x],trrs[z][y+1][x-1],trrs[z][y-1][x+1]]
                p = {}
                if(d[0] == 0 and d[3] == 0 and d[6] == 0):
                    p.update(l)
                if(d[1] == 0 and d[2] == 0 and d[7] == 0):
                    p.update(r)
                if(d[0] == 0 and d[2]== 0):
                    p.update(m)
                    if(d[4] == 0):
                        p.update(n)
                if(d[4] == 0):
                    if(d[3] == 0):
                        p.update(lb)
                    if(d[1] == 0):
                        p.update(rb)
                if(d[5] == 0):
                    if(d[0] == 0):
                        p.update(ld)
                    if(d[2] == 0):
                        p.update(rd)
                for u in p:
                    sh.putpixel(u,(0,0,0,63))
                cube.alpha_composite(sh)
                back.alpha_composite(cube,(mh,nh))
                sh = shc.copy()
                cube = cell.copy()
#完成
back.save(name )
back.show()
print(f"saved as {name}.")








