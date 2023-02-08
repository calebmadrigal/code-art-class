""" Challenge: Draw point in top right. """

import sys
from PIL import Image, ImageDraw

# Setup
img_width = 101
img_height = 101
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

# Draw point in center. NOTE: because the img1.point() function takes integers, we use the img_width // 2 operator,
# which does division to the nearest integer
img1.point((img_width // 2, img_height // 2), fill='aqua')

# Saves the picture
img_path = sys.argv[0].split('.')[0]+'.png'
img.save(img_path)
print(f'Saved {img_path}')
img.show()

