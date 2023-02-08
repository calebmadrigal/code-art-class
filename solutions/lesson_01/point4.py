""" Challenge: Draw point in bottom left. """

import sys
from PIL import Image, ImageDraw

# Setup
img_width = 101
img_height = 101
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

# NOTE: X and Y coordinates start with 0 (not 1), so that's why the bottom right pixel is (100, 100) rather than (101, 101).
img1.point((0, 100), fill='aqua')

# Saves the picture
img_path = sys.argv[0].split('.')[0]+'.png'
img.save(img_path)
print(f'Saved {img_path}')
img.show()

