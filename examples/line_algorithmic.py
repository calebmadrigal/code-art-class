import os
import sys
import math
from PIL import Image, ImageDraw

# Setup
img_size = (1000, 1000)
img = Image.new('RGB', img_size)
draw = ImageDraw.Draw(img)

# Draw using nested loops to set each pixel
for x_pixel in range(img_size[0]):
    for y_pixel in range(img_size[1]):
        if x_pixel == y_pixel:
            img.putpixel((x_pixel, y_pixel), (255, 255, 255))

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()


