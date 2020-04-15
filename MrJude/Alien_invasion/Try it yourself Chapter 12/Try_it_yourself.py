# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:30:43 2019

@author: Clarissa
"""
import pygame
#12-1 Blue Sky 
def blue_sky():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    bg_color = (0,0,255)
    screen.fill(bg_color)
    pygame.display.flip()

blue_sky()
#%%
#12-2 Game Character 
import pygame
class Character():
    def __init__ (self,screen):
        self.screen = screen
        
        self.image = pygame.image.load('pikachu.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    character = Character(screen)
    bg_color = (230,230,230)
    while True:
        screen.fill(bg_color)
        character.blitme
        pygame.display.flip()

run_game() 

#%%
#12-3 Rocket 
import pygame
class Rocket ():
    def __init__ (self,game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()
        
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
        

    def update(self):
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.rect.x += 5
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 5
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 5
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
class Main:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        self.guy = Rocket(self)
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.guy.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.guy.moving_left = True
                if event.key == pygame.K_UP:
                    self.guy.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.guy.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.guy.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.guy.moving_left = False
                if event.key == pygame.K_UP:
                    self.guy.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.guy.moving_down = False
                
    def _update_screen(self):
        self.screen.fill((0,0,0))
        rocket = Rocket(screen) 
        self.rocket.blitme()
        self.rocket.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
        
if __name__ == "__main__":
    mg = Main()
    mg.run_game()