# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 19:39:57 2019

@author: Clarissa
"""
import pygame
pygame.init()

#Parent class for creating a grid with different rows and columns
class Grid(object):
    def __init__(self, screen, width, height, columns, rows, showGrid=False, startx = 0, starty = 0, bg=(255,255,255)):
        self.width = width
        self.height = height
        self.columns = columns
        self.rows = rows
        self.bg = bg
        self.startx = startx
        self.starty = starty
    
        self.showGrid = showGrid #Return black outline
  
        self.grid = None

        self.screen = screen
        pygame.display.update()
                    
    def getGrid(self):
        return self.grid #Return the grid list

    def clicked(self, pos): #Return position of x and y grid which the user's clicked 
        try:
            posx = pos[0]
            posy = pos[1]
            grid1 = int((posx - self.startx) / self.grid[0][0].wc)
            grid2 = int((posy - self.starty) / self.grid[0][0].hr)

            self.selected = self.grid[grid1][grid2]

            return self.grid[grid1][grid2] 
        
        except IndexError: #If user clicked outside of the grid 
            return False


#This class draws pixels inside the grids 
class PixelArt(Grid): #Child class of Grid class
    ##Draw a black outline grid in the screen by overlapping boxes
    def drawGrid(self):
        self.grid = []
        for i_col in range(self.columns):
            self.grid.append([])
            for i_row in range(self.rows):
                self.grid[i_col].append(Pixel(i_col, i_row, self.width, self.height, self.columns, self.rows, self.startx, self.starty, self.showGrid))
                self.grid[i_col][i_row].show(self.screen, (255,255,255))


#Create the color pallet at the bottom 
class ColorPallet(PixelArt):
    def setColor(self, colorList): 
        #The colorList argument must be equal to the number of pixels inside the grid
        colourCount = 0

        for pixels in self.getGrid():
            for p in pixels:
                p.show(self.screen, colorList[colourCount],0)
                colourCount += 1


#Store the colors which will be appended to the color pallet
class Pixel():
    def __init__(self, i_col,i_row, width, height, columns, rows, startx=0, starty=0, showGrid=False):
        self.col = i_col #The column of the current instance
        self.row = i_row #The row of the current instance
        self.color = (255,255,255)
        self.rows = rows #Amount of rows in whole grid
        self.columns = columns #Amount of columns in whole grid
        self.showGrid = showGrid
        self.wc = width / columns
        self.hr = height / rows 
        self.x = self.col * self.wc + startx
        self.y = self.row * self.hr + starty
    
        
    def show(self, screen, color, outline=False, showGrid=False): #Display the current pixel
        if not(showGrid):
            self.color = color
            pygame.draw.rect(screen, color, (self.x, self.y, self.wc, self.hr))
        
        if self.showGrid and not(outline):
            pygame.draw.rect(screen, (0,0,0), (self.x, self.y, self.wc, self.hr), 1)

    def click(self, screen, color): #Set color atrribute to the assigned color 
        self.show(screen, color, 0)
        self.color = color

    def getColor(self): 
        return self.color