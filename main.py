import pygame;
import numpy as np;
import time

def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class color(object):
    @constant
    def BG(): # background
        return (25, 25, 25) 
    @constant
    def GRID():
        return (128, 128, 128)


pygame.init()
pygame.display.set_caption("Game of Life")

width, height = 1000, 1000
width, height = 400, 400
sizeX, sizeY = 20, 20
sizeWidthX = width / sizeX
sizeWidthY = height / sizeY

COLOR = color()

screen = pygame.display.set_mode((width, height))

# State of the cells: 0 = death, 1 = alive
grid = np.matrix([[0 for j in range(sizeY)] for i in range(sizeX)])

grid[1,3] = 1
grid[2,3] = 1
grid[3,3] = 1

running = True
# running = False
while running:
    screen.fill(COLOR.BG)
    newGrid = np.copy(grid)
    for x in range(sizeX):
        for y in range(sizeY):
            poli = [
                (x * sizeWidthX, y * sizeWidthY),
                ((x + 1) * sizeWidthX, y * sizeWidthY),
                ((x + 1) * sizeWidthX, (y + 1) * sizeWidthY),
                (x * sizeWidthX, (y + 1) * sizeWidthY)
            ]
            vecinitos = np.sum(grid[x - 1 : x + 2, y - 1 : y + 2]) - grid[x, y]

            if(grid[x, y] == 1 and (vecinitos < 2 or vecinitos > 3)):
                newGrid[x, y] = 0
            elif(grid[x, y] == 0 and vecinitos == 3):
                newGrid[x, y] = 1

            if(grid[x, y] == 0):
                pygame.draw.polygon(screen, COLOR.GRID, poli, 1)
            else:
                pygame.draw.polygon(screen, COLOR.GRID, poli)
    grid = newGrid
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;    
    print("tick")
    time.sleep(0.3)

# x = 1
# y = 1
# index = 1
# for i in range(0, sizeX):
#     for j in range(0, sizeY):
#         grid[i, j] = index
#         index = index + 1

# vecinito = grid[x - 1 : x + 2, y - 1 : y + 2]

# print(len(grid))
# print(grid)
# print(vecinito)

print("Thanks for playing, I hope you liked it.")
pygame.quit()