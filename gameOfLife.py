#!/usr/bin/env python3
import pygame; # library to generate the graphic interface
import numpy as np; # library to handle matrices
from math import floor; # import this function
import time; # to set a delay between each iteration

def constant(f): #define of a constant class
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class color(object): #Create the COLOR class as a collection of constants
    @constant
    def BG(): # background
        return (25, 25, 25) 
    @constant
    def GRID(): # Color of the grid
        return (128, 128, 128)
    @constant
    def WHITE(): # Color of a living cell
        return (255, 255, 255)


pygame.init() # Init pygame
pygame.display.set_caption("Game of Life") # Set the title of the game

# CONSTANTS
width, height = 1000, 1000 
sizeX, sizeY = 50, 50 # Number of cell spots in each axis
sizeWidthX = width / sizeX # Size of each spot
sizeWidthY = height / sizeY
COLOR = color() # Get the color class with the constants

screen = pygame.display.set_mode((width, height)) # Set the size of the window

# State of the cells: 0 = death, 1 = alive
grid = np.matrix([[0 for j in range(sizeY)] for i in range(sizeX)])

gameRunning = True # If false, the game stops
timeRunning = False # If true, time runs (so iterations occur)
while gameRunning:
    screen.fill(COLOR.BG) # Clean screen
    newGrid = np.copy(grid) # Make a copy of the grid
    for x in range(sizeX): # for each spot in the grid
        for y in range(sizeY):
            poli = [ # get coord of the cornes of the spot
                (x * sizeWidthX, y * sizeWidthY),
                ((x + 1) * sizeWidthX, y * sizeWidthY),
                ((x + 1) * sizeWidthX, (y + 1) * sizeWidthY),
                (x * sizeWidthX, (y + 1) * sizeWidthY)
            ]
            if timeRunning: # if iterations on
                #get all neighbours
                vecinitos = np.sum(grid[x - 1 : x + 2, y - 1 : y + 2]) - grid[x, y]
                #change the state of the cell in the spot acoording to the rules
                if(grid[x, y] == 0 and vecinitos == 3):
                    newGrid[x, y] = 1 # new cell
                elif(grid[x, y] == 1 and (vecinitos < 2 or vecinitos > 3)):
                    newGrid[x, y] = 0 # over or under population
            
            # Draw the spot
            if(grid[x, y] == 0):
                pygame.draw.polygon(screen, COLOR.GRID, poli, 1)
            else:
                pygame.draw.polygon(screen, COLOR.WHITE, poli)

    if timeRunning:
        time.sleep(0.1) # set a delay between each iteration
    grid = newGrid # Save the new grid as the normal one
    pygame.display.flip() # Update the screen

    for event in pygame.event.get(): # for each event
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
            #if mouse pressed down and it is left click: 
            pos = pygame.mouse.get_pos()
            x = floor(pos[0] / sizeWidthX)
            y = floor(pos[1] / sizeWidthY)
            grid[x, y] = (grid[x, y] - 1) % 2 # change value of selected cell

        if event.type == pygame.MOUSEMOTION: # If mouse moved
            pos = pygame.mouse.get_pos()
            x = floor(pos[0] / sizeWidthX)
            y = floor(pos[1] / sizeWidthY)
            if event.buttons[0] == 1: # If left click hold
                grid[x, y] = 1 # Activate the cell
            if event.buttons[2] == 1: # Right click
                grid[x, y] = 0 # Kill the cell
        elif event.type == pygame.QUIT: # if quit btn pressed
            gameRunning = False # no longer running game
        elif event.type == pygame.KEYDOWN:
            if event.key == 32: # Space pressed
                timeRunning = not timeRunning # Togle the run of iterations

print("Thanks for playing, I hope you liked it.")
print("See more projects like this one on https://github.com/jkutkut/")
pygame.quit() # End the pygame