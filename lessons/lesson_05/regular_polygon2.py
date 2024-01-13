from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
draw = ImageDraw.Draw(img)

# Draw
radius = 3
for i in range(80):
    draw.regular_polygon((500, 500, radius), 3, outline='lime', rotation=i*3)
    radius = radius * 1.1

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

