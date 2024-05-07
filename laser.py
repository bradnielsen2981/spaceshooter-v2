#Create a laser object that will be used to shoot#Create an enemy object that will be used to shoot the player
import pygame
import game_globals as GAME

class Laser(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()  #need to call the super constructor to work with Groups

        self.image = pygame.Surface((3, 15), pygame.SRCALPHA)
        self.image.fill((0, 255, 0))  # Green color

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Play sound
        self.sound = pygame.mixer.Sound("sounds/laser.mp3")
        self.sound.play(0)
        return
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return

    def update(self):
        self.rect.y = self.rect.y - 10
        return
    

