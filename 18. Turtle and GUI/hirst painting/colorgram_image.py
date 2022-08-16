import colorgram
# import turtle as t

colors = colorgram.extract("image.jpg", 30)

color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    color_list.append(rgb)

print(color_list)
