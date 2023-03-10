from PIL import Image

img = Image.open('parrot.jpg')
new_image = img.load()

width = img.size[0]
height = img.size[1]

# alpha, beta and gama weight values from:
# Fundamentals of Digital Image Processing - Chris Solomon & Toby Breckon (John Wiley & Sons Ltd, 2011, p.11)
alpha = 0.2989
beta = 0.5870
gama = 0.1140

for i in range(0, width):
    for j in range(0, height):
        # grey color has the same value for red, green and blue
        grey = round(new_image[i,j][0] * alpha + beta * new_image[i,j][1] + gama * new_image[i,j][2])
        new_image[i,j] = (grey, grey, grey)

img.save('grey_parrot.png')
