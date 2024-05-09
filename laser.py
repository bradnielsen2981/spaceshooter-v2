#Create an enemy object that will be used to shoot the player
#Create a spaceship object that will be used to shoot the aliens
import pygame
import game_globals as GAME

class Laser(pygame.sprite.Sprite):
 
    def __init__(self, x, y):
        super().__init__() # call the init function in pygame.sprite
        self.image = pygame.Surface([10, 10])
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
  
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return
    
    def update(self):
        self.rect.x = self.rect.x + 4
 

        
