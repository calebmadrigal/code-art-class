import sys
from PIL import Image, ImageDraw

# Setup
img_width = 1001
img_height = 1001
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

img1.point((img_width / 2, img_height / 2), fill ='red')

# Saves the picture
img_path = sys.argv[0].split('.')[0]+'.png'
img.save(img_path)
print(f'Saved {img_path}')
img.show()

