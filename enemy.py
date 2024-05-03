#Create an enemy object that will be used to shoot the player
#Create a spaceship object that will be used to shoot the aliens
import pygame
import game_globals as GAME

class Enemy(pygame.sprite.Sprite):
 
    def __init__(self, x, y):
        super().__init__() # call the init function in pygame.sprite
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = 1
        self.speed = 1
        GAME.ENEMY_GROUP.add(self) #add it to the sprite group

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return
    
    def update(self):
        self.rect.x = self.rect.x + (self.direction * self.speed)
        if self.rect.x > 1024:
            self.direction = self.direction * -1
        if self.rect.x < 0:
            self.direction = self.direction * -1  

        
