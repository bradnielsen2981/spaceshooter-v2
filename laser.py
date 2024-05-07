#Create a laser object that will be used to shoot#Create an enemy object that will be used to shoot the player
#Create a spaceship object that will be used to shoot the aliens
import pygame
import game_globals as GAME

class Laser(pygame.sprite.Sprite):
 
    def __init__(self, x, y):
        super().__init__() # call the init function in pygame.sprite
        self.image = None
        self.rect.center = (x,y)
        #self.direction = 1
        #self.speed = 3

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return
    
    def update(self):
        pass

        
