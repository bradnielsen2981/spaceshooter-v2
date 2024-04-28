import pygame
import game_globals as GAME

class Laser(pygame.sprite.Sprite):

    def __init__(self, position, direction, speed):

        super().__init__()  #need to call the super constructor to work with Groups

        self.image = pygame.Surface((3, 15), pygame.SRCALPHA)
        self.image.fill((0, 255, 0))  # Green color

        self.rect = self.image.get_rect(center=position)
        self.position = position

        # Set velocity based on direction and speed
        self.direction = direction
        self.speed = speed

        # Play sound
        self.sound = pygame.mixer.Sound("sounds/laser.mp3")
        self.sound.play(0)

        GAME.BULLET_GROUP.add(self) #makes it draw and update
        return

    def update(self):
        self.position = self.position + self.speed*self.direction
        self.rect.center = self.position.xy #need to move the rectangle to draw
        
        if not self.rect.colliderect(GAME.SCREEN.get_rect()):
            self.kill()
        return
    

