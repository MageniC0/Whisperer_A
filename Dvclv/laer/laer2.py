import os  
from PIL import Image

shadow = {}  
  
# 指定文件夹路径  
folder_path = 'sors'  # 注意：确保文件夹名没有拼写错误  
  
# 遍历从0到255的数字  
for i in range(256):  
    # 构造文件名
    u = str(hex(i))
    shadow_name = f'{u}.png'  
    # 构造文件完整路径
    file_path = os.path.join(folder_path, shadow_name)
    img = Image.open(file_path)
    shadow[f'{i}'] = img