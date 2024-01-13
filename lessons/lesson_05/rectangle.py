import random
from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
draw = ImageDraw.Draw(img)

random.seed(13)

# Draw
for i in range(113):
    x0 = random.randint(0, 1000)
    y0 = random.randint(0, 1000)
    x1 = random.randint(0, 1000)
    y1 = random.randint(0, 1000)
    red_amount = random.randint(0, 256)
    green_amount = random.randint(0, 256)
    blue_amount = random.randint(0, 256)
    width = random.randint(1, 5)
    draw.rectangle([(x0, y0), (x1, y1)], outline=(red_amount, green_amount, blue_amount), width=width)

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

