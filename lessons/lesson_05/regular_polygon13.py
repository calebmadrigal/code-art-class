from PIL import Image, ImageDraw

# Setup
img_width = 1200
img_height = 1200
img = Image.new("RGB", (img_width, img_height))
draw = ImageDraw.Draw(img)

# Draw
radius = 3
for i in range(120):
    draw.regular_polygon((img_width/2, img_height/2, radius+(i*2)), 12, outline=(i*2+10, 0, i*2+10), rotation=i*2)
    #radius = radius * 1.05
    radius = radius * 1.045

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

