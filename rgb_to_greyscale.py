red = [[255, 0], 
        [0, 255]] 

green = [[0, 255], 
        [0, 255]] 
        
blue = [[0, 0], 
        [255, 255]]
        
alpha = 0.2989
beta = 0.5870
gama = 0.1140

height = len(red)
width = len(red[0]) 

grey = [[0 for x in range(width)] for y in range(height)] 

for i in range(0, len(red)):
    for j in range(0, len(red[i])):
        grey[i][j] = round(red[i][j] * alpha + beta * green[i][j] + gama * blue[i][j])
        
print(grey)
    
