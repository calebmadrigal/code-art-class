""" Challenge: Draw point in top right. """

from PIL import Image, ImageDraw

# Setup
img_width = 101
img_height = 101
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

# Draw point in top right
img1.point((100, 0), fill='aqua')

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

