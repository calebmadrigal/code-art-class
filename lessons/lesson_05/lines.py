from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
draw = ImageDraw.Draw(img)

# Draw
for i in range(50):
    draw.line([(img_width/2, 200), (i*(1000/50), 999)], width=1, fill=(200+i, 0, 0))

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

