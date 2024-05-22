import pygame
import game_globals as GAME

class Platform(pygame.sprite.Sprite):
    def __init__(self, position, width, height):

        super().__init__()  #need to call the super constructor to work with Groups

        self.image = pygame.Surface((width, height))
        self.image.fill((200, 10, 10))  # Green color
        self.rect = self.image.get_rect(center=position)
        self.position = position
        return

    #moving platform?
    def update(self):
        self.rect.y += 1

        if self.rect.y > 768:
            self.kill()
        return
    

