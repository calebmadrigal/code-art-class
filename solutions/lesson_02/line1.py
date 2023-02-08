""" Challenge: Make flat horizontal line on top of image. """

from PIL import Image, ImageDraw

# Setup
img_width = 101
img_height = 101
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

# Draw
for x in range(101):
    # If we set y=0, we get a horizontal line on the top
    img1.point((x, 0), fill='lime')

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

