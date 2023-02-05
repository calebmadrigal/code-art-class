import sys
from PIL import Image, ImageDraw

# Setup
img_width = 101
img_height = 101
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

# Draw
for i in range(101):
    if i > 10 and i < 90:
        img1.point((50, i), fill = (2*i, i, 100-i))

for i in range(101):
    if i > 10 and i < 90:
        img1.point((i, 50), fill = (2*i, i, 100-i))


# Saves the picture
img_path = sys.argv[0].split('.')[0]+'.png'
img.save(img_path)
print(f'Saved {img_path}')
img.show()

