import os
import requests
from PIL import Image, ImageEnhance
from io import BytesIO

url = 'https://github.com/YUVRAJ-SINGH-3178.png'
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Enhance contrast for better ASCII mapping
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1.5)

width = 46
aspect_ratio = img.height / img.width
height = int(aspect_ratio * width * 0.5)
img = img.resize((width, height)).convert('L')

# More detailed character set for better accuracy
chars = ['@', '%', '#', '*', '+', '=', '-', ':', '.', ' ']
pixels = img.getdata()

for y in range(height):
    line = ''
    for x in range(width):
        pixel = pixels[y * width + x]
        idx = int((pixel / 255.0) * (len(chars) - 1))
        line += chars[idx]
    print('        "' + line + '",')
