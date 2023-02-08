""" Challenge: Make flat vertical line in the center of the image. """

import sys
from PIL import Image, ImageDraw

# Setup
img_width = 101
img_height = 101
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

# Draw
for y in range(101):
    img1.point((img_width // 2, y), fill='lime')

for x in range(101):
    img1.point((x, img_height // 2), fill='lime')

# Saves the picture
img_path = sys.argv[0].split('.')[0]+'.png'
img.save(img_path)
print(f'Saved {img_path}')
img.show()

