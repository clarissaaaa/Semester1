# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 07:34:08 2019

@author: Clarissac
"""
import pygame
from FP_gridMod import ColorPallet, PixelArt, Grid
from ButtonOffer import Button, Offer
import sys
import random

pygame.init() #Initalize pygame
paintBrush = pygame.image.load("images\Paintbrush.png") #Load paintbrush image use later for icon

#set pixel's rows and columns 
rows = 50
columns = 50
#set screen width and height
width = 600
height = 600


def fill(press, grid, color):
    #.click from Pixel class which determine the assigned color
    press.click(grid.screen, color)
    pygame.display.update()
    
    #.col and .row is inialize in the Pixel class
    i_col = press.col #indicate the current colomn in the grid 
    i_row = press.row #indicate the current row in the grid

    if i_col < columns-1: #Right
        fill(grid.getGrid()[i_col + 1][i_row], grid, color)
    if i_col > 0: #Left
         fill(grid.getGrid()[i_col - 1][i_row], grid, color)
    if i_row < rows-1: #Up
         fill(grid.getGrid()[i_col][i_row + 1], grid, color)
    if i_row > 0 : #Down
         fill(grid.getGrid()[i_col][i_row - 1], grid, color)

#Creating a screen 
def initalize(columns, rows, showGrid=False):
    #showGrid = False means that the pixels grid will be hidden 
    global pallet, grid, screen, publish_button, colorList
    
    pygame.display.set_icon(paintBrush) #Display paintbrush as the icon 
    
    screen = pygame.display.set_mode((width, height + 100))
    pygame.display.set_caption('Paint-ful') # Set the caption for the window
    screen.fill((255,255,255))
    
    publish_button= Button((0,73,150), 120,610, 130,50,"Publish!") #Set up the publish button
    publish_button.drawBox(screen, (0,0,0))
    

    
    #Display image of critic 
    critic_img = pygame.image.load('images/benjamin_critic.png')
    screen.blit(critic_img, (500,595))


    #Create an object
    grid = PixelArt(screen, 600, 600, columns, rows, showGrid) #set up the width and height as 600 x 600 so it doesnt effect the menu 
    grid.drawGrid()
    
    pallet = ColorPallet(screen, 90, 90, 3, 3, True, 10, grid.height + 2)
    pallet.drawGrid()
    
    colorList = [(255,0,0), (255,128,0), (255,255,0), (0,255,0), (0,0,255), (127,0,255), (0,0,0),(160,160,160), (255,255,255)]
    #Set the colours for the color pallet
    #Red, orange, yellow, green, blue, purple, black, grey, white
    pallet.setColor(colorList)
    
       
    pygame.display.update() 
   
#Main loop 
initalize(columns, rows)
color = (0,0,0) # Set first color black 


while True:
    #Main loop for mouse collision
    events = pygame.event.get()
    

    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
            quit()
        
        #If user clicked or dragged mouse 
        if pygame.mouse.get_pressed()[0]: 
            try:
                pos = pygame.mouse.get_pos()
                #pos[0] determine x coordinate , pos[1] determine y coordinate. Defined in the clicked function in Grid class
                if pos[1] >= grid.height: # If the mouse is below the main drawing grid
                
                    #If the user click on the color pallet
                    if pos[0] >= pallet.startx and pos[0] <= pallet.startx + pallet.width and pos[1] >= pallet.starty and pos[1] <= pallet.starty + pallet.height :
                        #get the color in the grid selected 
                        clicked = pallet.clicked(pos)
                        color = clicked.getColor() # Set drawing color
                
                    
                    #If the user click on the publish button
                    else:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            try:
                                if publish_button.pos(pos):
                                    offer= Offer((255,255,255),270,610, 220, 30, "That's a nice painting!")
                                    money = random.randint(1, 1001)
                                    offer2 = Offer((255,255,255),270,650, 220, 30, ("I'll offer your $" + str(money))) 
                                    offer.drawBox(screen,(0,0,0))
                                    offer2.drawBox(screen,(0,0,0))
                            except TypeError:
                                pass
                        
                else: #if they dont click any of the above then draw the pixels

                    clicked = grid.clicked(pos)
                    clicked.click(grid.screen,color)
                
                pygame.display.update()
            except AttributeError:
                pass

pygame.quit()