""" Challenge: Use a compound conditional to cut off all 4 sides by 250 pixels, leaving a square in the middle. """

import sys
from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)


# Draw
for x in range(img_width):
    for y in range(img_height):
        if x > 250 and x < 750 and y > 250 and y < 750:
            img1.point((x, y), fill='red')

# Saves the picture
img_path = sys.argv[0].split('.')[0]+'.png'
img.save(img_path)
print(f'Saved {img_path}')
img.show()

