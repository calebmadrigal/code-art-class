from PIL import Image, ImageDraw

# Setup
img_width = 1200
img_height = 1200
img = Image.new("RGB", (img_width, img_height), (0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw
#radius = 1
for i in range(1, 500):
    #draw.regular_polygon((img_width/2, img_height/2, radius), 12, outline=(i, 0, (i*21)%255), rotation=i*9)

    # Draw a color wave which oscillates between white and black and other colors - differenet frequency waves which synchroonize...
    # Need something that is 256-periodic - so, like... i*4, i*8, i*16
    #draw.regular_polygon((img_width/2, img_height/2, i), 6, outline=((i*3)%256, 50, (i*27)%256), rotation=i*1)
    draw.regular_polygon((img_width/2, img_height/2, i), 6, outline=((i*3)%256, 0, (i*27)%256), rotation=i*0.6)
    #radius = radius * 1.0255

# Saves the picture
img_path = __file__.replace('.py', '.png')
img.save(img_path)
print(f'Saved {img_path}')
img.show()

