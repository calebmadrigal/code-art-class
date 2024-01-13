from PIL import Image, ImageDraw
from PIL import ImageFont

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGBA", (img_width, img_height), (0, 0, 0))
draw = ImageDraw.Draw(img)

# Use a font to determine the size and shape of the text
# Documentation on fonts: https://pillow.readthedocs.io/en/stable/reference/ImageFont.html

# Draw
font_size = 200
font = ImageFont.truetype('../../_resources/fonts/Avenir.ttc', font_size)
draw.text((300, 140), 'thou', fill=(0, 140, 0), align='center', stroke_width=2, font=font, stroke_fill=None)

font_size = 300
font = ImageFont.truetype('../../_resources/fonts/Avenir.ttc', font_size)
draw.text((130, 380), '¡ART!', fill='lime', align='center', stroke_width=2, font=font, stroke_fill=None)


# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

