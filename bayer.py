import numpy as np
from PIL import Image

bayer = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 10, 130, 15, 110, 15, 120, 0],
    [0, 215, 40, 250, 30, 250, 40, 0],
    [0, 15, 255, 15, 255, 15, 230, 0],
    [0, 210, 30, 255, 45, 250, 45, 0],
    [0, 10, 115, 10, 110, 10, 115, 0],
    [0, 110, 30, 110, 35, 115, 45, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

lines = len(bayer)
columns = len(bayer[0])

rgb_matrix = np.zeros((lines -2, columns-2, 3))

for l in range (1, lines-1):
    for c in range(1, columns-1):
        # red pixel:
        if (l % 2) != 0 and (c % 2) != 0:
            r = bayer[l][c]
            g = round((bayer[l-1][c] + bayer[l+1][c] + bayer[l][c-1] + bayer[l][c+1])/4)
            b = round((bayer[l-1][c-1] + bayer[l-1][c+1] + bayer[l+1][c-1] + bayer[l+1][c+1])/4)
        # blue pixel:
        elif (l % 2) == 0 and (c % 2) == 0:
            r = round((bayer[l-1][c-1] + bayer[l-1][c+1] + bayer[l+1][c-1] + bayer[l+1][c+1])/4)
            g = round((bayer[l-1][c] + bayer[l+1][c] + bayer[l][c-1] + bayer[l][c+1])/4)
            b = bayer[l][c]
        #green pixel with blue pixels on its sides:
        elif (l % 2) == 0 and (c % 2) != 0:
            r = round((bayer[l-1][c] + bayer[l+1][c])/2)
            g = bayer[l][c]
            b = round((bayer[l][c-1] + bayer[l][c+1])/2)
        # green pixel with red pixels on its sides:
        else:
            r = round((bayer[l][c - 1] + bayer[l][c + 1]) / 2)
            g = bayer[l][c]
            b = round((bayer[l - 1][c] + bayer[l + 1][c]) / 2)
        rgb_matrix[l - 1][c - 1][0] = r
        rgb_matrix[l - 1][c - 1][1] = g
        rgb_matrix[l - 1][c - 1][2] = b

final_rgb = np.zeros((lines -2, columns-2), dtype='i,i,i')
for i in range(lines -2):
    for j in range(columns -2):
        r = rgb_matrix[i][j][0]
        g = rgb_matrix[i][j][1]
        b = rgb_matrix[i][j][2]
        tup = (r,g,b)
        final_rgb[i][j] = tup

# cria imagem:
width = lines - 2
height = lines -2
img = Image.new(mode = "RGB", size = (width, height))
new_image = img.load()

for i in range(0, width):
    for j in range(0, height):
        r = final_rgb[i,j][0]
        g = final_rgb[i, j][1]
        b = final_rgb[i, j][2]
        new_image[i,j] = (r, g, b)
img.save('image.png')


#greyscale:
alpha = 0.1
beta = 0.1
gama = 0.1

for i in range(0, width):
    for j in range(0, height):
        # grey color has the same value for red, green and blue
        grey = round(new_image[i,j][0] * alpha + beta * new_image[i,j][1] + gama * new_image[i,j][2])
        new_image[i,j] = (grey, grey, grey)

img.save('grey.png')
