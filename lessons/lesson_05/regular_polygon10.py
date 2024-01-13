from PIL import Image, ImageDraw

# Setup
img_width = 1000
img_height = 1000
img = Image.new("RGB", (img_width, img_height))
draw = ImageDraw.Draw(img)

# Draw
radius = 3

index = 0
for growth_rate in [1+(i/100) for i in range(20)]:
    #growth_rate = 1.1
    print(f'Growth rate: {growth_rate}')
    rotate_rate = 137.5

    for i in range(50):
        draw.regular_polygon((500, 500, radius), 6, outline='lime', rotation=i*rotate_rate)
        radius = radius * growth_rate

    # Saves the picture
    img_path = __file__.split('.')[0] + f'_{index}.png'
    #img_path = __file__.replace('.py', '.png')
    img.save(img_path)
    print(f'Saved {img_path}')
    #img.show()
    index += 1

