from PIL import Image, ImageDraw

# Setup
img_width = 1200
img_height = 1200
img = Image.new("RGB", (img_width, img_height))
draw = ImageDraw.Draw(img)

# Draw
radius = 3
for i in range(73):
    draw.regular_polygon((img_width/2, img_height/2, radius+(i*5)), 5, outline='lime', rotation=i*5)
    #radius = radius * 1.05
    radius = radius * 1.045

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

