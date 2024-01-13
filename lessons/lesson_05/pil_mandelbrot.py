from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
draw = ImageDraw.Draw(img)

# Draw
img = Image.effect_mandelbrot((900, 900), (-1.749705744568359348771, -0.000003305355794270639, -1.749696588793945286448, 0.000003557164388020895), 100)

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

