"""Challenge: change the square color from blue to red."""

import sys
from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

# Iterate over every pixel (x, y) in the image, and set the color of each pixel to red
for x in range(img_width):
    for y in range(img_height):
        img1.point((x, y), fill='red')

# Saves the picture
img_path = sys.argv[0].split('.')[0]+'.png'
img.save(img_path)
print(f'Saved {img_path}')
img.show()

