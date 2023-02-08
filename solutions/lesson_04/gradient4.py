import sys
from PIL import Image, ImageDraw

# Setup
img_width = 256
img_height = 256
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

# Draw
for x in range(img_width):
    for y in range(img_height):
        img1.point((x, y), fill = (256 - (x+y), 0, x+y))

# Saves the picture
img_path = sys.argv[0].split('.')[0]+'.png'
img.save(img_path)
print(f'Saved {img_path}')
img.show()

