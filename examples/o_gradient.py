from PIL import Image
img_size = (1024, 1024)

def make_linear_mapper(in_range, out_range):
    in_delta = in_range[1] - in_range[0]
    out_delta = out_range[1] - out_range[0]
    # y = mx + b (m = slope, b = y-intersect)
    m = (out_delta / in_delta)
    # To find b: b = y - mx, just plug in first item of each range
    b = out_range[0] - m * in_range[0]
    def _linear_mapper(val):
        return m * val + b
    return _linear_mapper

def circle_func_gen(center_x, center_y, radius):
    def _circle_error(x, y):
        # Return error by subtracting one side of the equation from the other
        ret = abs(radius**2 - ((x - center_x)**2 + (y - center_y)**2))
        if ret == 0:  # Avoid divide-by-zero error
            return 0.01
        return ret
    return _circle_error

im = Image.new('RGB', img_size)
circle = circle_func_gen(img_size[0]//2, img_size[1]//2, 200)
func = lambda x, y: circle(x, y)**(1/2)

pixel_to_value = {}  # (x, y) -> pixel_value
for x_pixel in range(img_size[0]):
    for y_pixel in range(img_size[1]):
        val = func(x_pixel, y_pixel)
        pixel_to_value[(x_pixel, y_pixel)] = val

max_error = max(pixel_to_value.values())
color_map = make_linear_mapper([0, max_error], [255, 0])

for (x_pixel, y_pixel), val in pixel_to_value.items():
    color = (int(color_map(val)), 0, 0)
    im.putpixel((x_pixel, y_pixel), color)

im.save('o_gradient.png')
im.show()
