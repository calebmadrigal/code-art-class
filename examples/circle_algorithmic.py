from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
img1 = ImageDraw.Draw(img)

center = img_width // 2
radius = img_width / 4

# Draw
for x in range(img_width):
    for y in range(img_height):
        if (x-center)**2 + (y-center)**2 < radius**2:
            img1.point((x, y), fill = 'magenta')

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

