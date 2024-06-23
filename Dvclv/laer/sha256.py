from PIL import Image, ImageDraw

# 初始化表面和绘图对象
s = Image.new('RGBA', (13, 13), (0, 0, 0, 0))
draw = ImageDraw.Draw(s)
c = (0, 0, 0, 31)

left_side = {(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10)}
right_side = {(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10)}
left_back = {(2,1),(3,1),(4,1),(5,0),(6,0)}
right_back = {(6,0),(7,0),(8,1),(9,1),(10,1)}
left_down = {(0,10),(1,10),(2,11),(3,11),(4,11),(5,12)}
right_down = {(7,12),(8,11),(9,11),(10,10),(11,10),(12,10)}
in_mid = {(6,5),(6,6),(6,7),(6,8),(6,9),(6,10),(6,11),(6,12)}
in_tot = {(3,4),(3,5),(4,4),(4,5),(5,5),(5,6)}

def d(l):
    for pos in l:
        draw.point(pos,c)

# 主循环，遍历所有可能的8位二进制数
for i in range(256):
    tb = [(i & (1 << j)) != 0 for j in range(8)]  # 将整数转换为二进制列表
    # 根据二进制列表决定绘制哪些集合
    if tb[0] == 0 and tb[3] == 0 and tb[6] == 0:
        d(left_side)
    if tb[1] == 0 and tb[2] == 0 and tb[7] == 0:
        d(right_side)
    if tb[4] == 0:
        if tb[3] == 0:
            d(left_back)
        if tb[1] == 0:
            d(right_back)
    if tb[5] == 0:
        if tb[0] == 0:
            d(left_down)
        if tb[2] == 0:
            d(right_down)
    if tb[0] == 0 and tb[2] == 0:
        d(in_mid)
        if tb[4] == 0:
            d(in_tot)
    h1 = tb[0] + 2 * tb[1] + 4 * tb[2] + 8 * tb[3]+ 16 * tb[4] + 32 * tb[5] + 64 * tb[6] + 128 * tb[7]
    h2 = hex(h1+4352)
    fname = f"{h2}.png"
    s.save(fname)
    draw.rectangle([(0, 0), (12, 12)], fill=(0, 0, 0, 0))

print("Images generated.")