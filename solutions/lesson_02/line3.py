""" Challenge: Make flat vertical line on left of image. """

from PIL import Image, ImageDraw

# Setup
img_width = 101
img_height = 101
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

# Draw
for y in range(101):
    # Since the x and y pixel coordinates start with the number 0, y=100 is the bottom of the image
    img1.point((0, y), fill='lime')

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

