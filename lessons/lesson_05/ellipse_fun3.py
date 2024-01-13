from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
draw = ImageDraw.Draw(img)

def circle_at_center(center_x, center_y, radius, width, outline=None, fill=None):
    top_left_x = center_x - radius
    top_left_y = center_y - radius
    bottom_right_x = center_x + radius
    bottom_right_y = center_y + radius
    draw.ellipse([(top_left_x, top_left_y), (bottom_right_x, bottom_right_y)], outline=outline, fill=fill, width=width)

# Draw
for radius in range(1, 1000, 10):
    circle_at_center(300, 500, radius, width=1, outline=(0, 255, 0))
    circle_at_center(700, 500, radius, width=1, outline=(0, 255, 0))

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

