import sys
from PIL import Image, ImageDraw

# Setup
img_width = 1024
img_height = 1024
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)


# Draw
for x in range(img_width):
    for y in range(img_height):
        if y > img_height * (1/4) and y < img_height * (3/4) and x > img_width * (1/4) and x < img_width * (3/4):
            img1.point((x, y), fill = ((x+y)%256, (x*y)%256, (y-x)%256))


# Saves the picture
img_path = sys.argv[0].split('.')[0]+'.png'
img.save(img_path)
print(f'Saved {img_path}')
img.show()

