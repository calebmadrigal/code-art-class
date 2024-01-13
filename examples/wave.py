import math
from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

# Draw
for x in range(img_width):
    amplitude = 100
    frequency = 0.1
    y = amplitude * math.sin(frequency * x)
    img1.point((x, y+img_height//2), fill='lime')

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

