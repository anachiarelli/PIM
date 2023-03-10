from PIL import Image

img = Image.open('parrot.jpg')
pix = img.load()

width = img.size[0]
height = img.size[1]

alpha = 0.2989
beta = 0.5870
gama = 0.1140

for i in range(0, width):
    for j in range(0, height):
        grey= round(pix[i,j][0] * alpha + beta * pix[i,j][1] + gama * pix[i,j][2])
        pix[i,j] = (grey, grey, grey)

img.save('grey_parrot.png')
