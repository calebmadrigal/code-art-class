""" Challenge: Draw point in top right. """

from PIL import Image, ImageDraw

# Setup
img_width = 101
img_height = 101
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

# Draw point in center. NOTE: because the img1.point() function takes integers, we use the img_width // 2 operator,
# which does division to the nearest integer

# Left eye
img1.point((50 - 15, 25), fill='aqua')

# Right eye
img1.point((50 + 15, 25), fill='aqua')

# Mouth
img1.point((25, 75), fill='aqua')
img1.point((35, 80), fill='aqua')
img1.point((45, 85), fill='aqua')
img1.point((55, 85), fill='aqua')
img1.point((65, 80), fill='aqua')
img1.point((75, 75), fill='aqua')

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

