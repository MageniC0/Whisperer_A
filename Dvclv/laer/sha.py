from PIL import Image, ImageDraw

# 初始化图像和绘图对象
s = Image.new('RGBA', (13, 13), (0, 0, 0, 0))
dr = ImageDraw.Draw(s)
c = (0, 0, 0, 31)  # 点的颜色（RGBA）

# 定义坐标集合
left_side, right_side, left_back, right_back, left_down, right_down, in_mid, in_tot = {(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10)},{(12,3),(12,4),(12,5),(12,6),(12,7),(12,8),(12,9),(12,10)},{(2,1),(3,1),(4,1),(5,0),(6,0)},{(6,0),(7,0),(8,1),(9,1),(10,1)},{(0,10),(1,10),(2,11),(3,11),(4,11),(5,12)},{(7,12),(8,11),(9,11),(10,10),(11,10),(12,10)},{(6,5),(6,6),(6,7),(6,8),(6,9),(6,10),(6,11),(6,12)},{(3,4),(3,5),(4,4),(4,5),(5,5),(5,6)}

# 封装绘制逻辑
def draw_points(points):
    for pos in points:
        dr.point(pos, c)

# 绘制函数，根据二进制列表来决定绘制哪些集合
def draw_based_on_binary(tb):
    if tb[0] == 0 and tb[3] == 0 and tb[6] == 0:
        draw_points(left_side)
    if tb[1] == 0 and tb[2] == 0 and tb[7] == 0:
        draw_points(right_side)
    if tb[4] == 0:
        if tb[3] == 0:
            draw_points(left_back)
        if tb[1] == 0:
            draw_points(right_back)
    if tb[5] == 0:
        if tb[0] == 0:
            draw_points(left_down)
        if tb[2] == 0:
            draw_points(right_down)
    if tb[0] == 0 and tb[2] == 0:
        draw_points(in_mid)
        if tb[4] == 0:
            draw_points(in_tot)

# 主循环，遍历所有可能的8位二进制数
for i in range(256):
    tb = [(i >> j) & 1 for j in range(7, -1, -1)]  # 从高位到低位转换二进制列表
    draw_based_on_binary(tb)
    h1 = sum(tb[j] << j for j in range(8))  # 更简洁地计算整数
    h = hex(h1)[2:].zfill(2)  # 转换为十六进制字符串，并确保长度为2
    s.save(f"0xff{h}.png")  # 保存图像文件，添加.png后缀
    dr.rectangle([(0, 0), (12, 12)], fill=(0, 0, 0, 0))  # 清空图像以供下一次迭代使用

print("Images generated.")