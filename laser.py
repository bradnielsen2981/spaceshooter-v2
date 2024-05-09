#Create an enemy object that will be used to shoot the player
#Create a spaceship object that will be used to shoot the aliens
import pygame
import game_globals as GAME

class Laser(pygame.sprite.Sprite):
 
    def __init__(self, x, y):
        super().__init__() # call the init function in pygame.sprite
        self.image = pygame.Surface( (3, 15) )
        self.image.fill( (0, 255, 0) )  # Green color

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        GAME.BULLET_GROUP.add(self)
  
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return
    
    def update(self):
        self.rect.y = self.rect.y - 10
 

        
