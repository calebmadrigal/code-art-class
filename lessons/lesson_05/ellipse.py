from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
draw = ImageDraw.Draw(img)

# Draw
draw.ellipse([(400, 400), (600, 600)], outline=(255, 0, 0), width=5)
draw.ellipse([(300, 300), (700, 700)], outline=(200, 0, 0), width=5)
draw.ellipse([(200, 200), (800, 800)], outline=(150, 0, 0), width=5)

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

