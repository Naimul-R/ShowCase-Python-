from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
path_out = '/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    #sharpen
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-99)
    
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{path_out}/{clean_name}_edited.jpg')