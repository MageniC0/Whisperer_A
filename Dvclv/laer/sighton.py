from PIL import Image
filename = input("file name:")
original_image = Image.open('a2.png')
enlarged_image = original_image.resize((980, 980),Image.NEAREST)
enlarged_image.save('filename')