from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
draw = ImageDraw.Draw(img)

# Draw
draw.line((100, 100, 900, 900), fill='red', width=5)
draw.line((100, 900, 900, 100), fill='blue', width=5)

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

