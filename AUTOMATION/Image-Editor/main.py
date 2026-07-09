from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
path_out = './editedImgs'

os.makedirs(path_out, exist_ok=True)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    #sharpen
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90, expand=True)
    
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{path_out}/{clean_name}_edited.jpg')