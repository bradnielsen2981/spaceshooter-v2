#Create a spaceship object that will be used to shoot the aliens
import pygame
import game_globals as GAME

class Spaceship(pygame.sprite.Sprite):
 
    def __init__(self, x, y):
        super().__init__() # call the init function in pygame.sprite
        self.image = pygame.image.load("images/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return
    
    def update(self, pressed, mouse_pos, mouse_buttons):

        if pressed[pygame.K_a] == 1:
            self.rect.x = self.rect.x - 1
        elif pressed[pygame.K_d] == 1:
            self.rect.x = self.rect.x + 1
        elif pressed[pygame.K_s] == 1:
            self.rect.y = self.rect.y + 1
        elif pressed[pygame.K_w] == 1:
            self.rect.y = self.rect.y - 1
