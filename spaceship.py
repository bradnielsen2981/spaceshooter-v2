''' Spaceship Sprite Code '''
import pygame
import game_globals as GAME
import math, time

#Sprite Object for the Space Ship
class Spaceship(pygame.sprite.Sprite):
#
    # Constructing spaceship object #
    def __init__(self, x, y):
        super().__init__() 
        return
    
    # draw the sprite
    def draw(self, screen):
        #screen.blit(self.image, self.rect)
        return
    
    # Updates the sprite every frame
    def update(self, pressed, mouse_pos, mouse_buttons):
        return