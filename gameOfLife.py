#!/usr/bin/env python3
import pygame;
import numpy as np;
import math;
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
    @constant
    def WHITE():
        return (255, 255, 255)


pygame.init()
pygame.display.set_caption("Game of Life")

width, height = 1000, 1000
sizeX, sizeY = 50, 50
sizeWidthX = width / sizeX
sizeWidthY = height / sizeY

COLOR = color()

screen = pygame.display.set_mode((width, height))

# State of the cells: 0 = death, 1 = alive
grid = np.matrix([[0 for j in range(sizeY)] for i in range(sizeX)])

gameRunning = True
timeRunning = True
# running = False
while gameRunning:
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
            if timeRunning:
                vecinitos = np.sum(grid[x - 1 : x + 2, y - 1 : y + 2]) - grid[x, y]
                if(grid[x, y] == 0 and vecinitos == 3):
                    newGrid[x, y] = 1 # new cell
                elif(grid[x, y] == 1 and (vecinitos < 2 or vecinitos > 3)):
                    newGrid[x, y] = 0 # over or under population

            # Draw
            if(grid[x, y] == 0):
                pygame.draw.polygon(screen, COLOR.GRID, poli, 1)
            else:
                pygame.draw.polygon(screen, COLOR.WHITE, poli)


    grid = newGrid
    pygame.display.flip()
    time.sleep(0.1)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
            pos = pygame.mouse.get_pos()
            x = math.floor(pos[0] / sizeWidthX)
            y = math.floor(pos[1] / sizeWidthY)
            # print((x, y))
            grid[x, y] = (grid[x, y] - 1) % 2 
        elif event.type == pygame.QUIT:
            gameRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 32: # Space pressed
                timeRunning = not timeRunning
            # print(event.key)

print("Thanks for playing, I hope you liked it.")
pygame.quit()