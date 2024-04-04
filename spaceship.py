''' Spaceship Sprite Code '''
import pygame
#from laser import Laser
import game_globals as GAME
import math, time

#Sprite Object for the Space Ship
class Spaceship(pygame.sprite.Sprite): ##Q what does sprite class mean?

    # Constructing spaceship object #
    def __init__(self, x, y):
        super().__init__() 
        
        # Sprite Image
        self.image = pygame.image.load("images/spaceship.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.originalimage = self.image.copy() #need original image to rotate

        # Sprite Movement
        self.direction = pygame.Vector2(0,0)
        self.speed = 4
        #self.speedlimit = 3

        # Sprite Positioning
        self.rect = self.image.get_rect() # gets rectangle of the image #
        self.position = pygame.Vector2(x,y)
        self.rect.center = self.position.xy
        
        self.last_shoot_time = 0 #used to stop machine gun effect
        return
    
    # draw the sprite
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return
    
    # Updates the sprite every frame
    def update(self, pressed, mouse_pos, mouse_buttons):

        if pressed[pygame.K_a] == 1:
            self.direction = pygame.Vector2(-1,0)
            self.position = self.position + self.speed*self.direction
            self.rect.center = self.position.xy #need to move the rectangle to draw

        elif pressed[pygame.K_d] == 1:
            self.direction = pygame.Vector2(1,0)
            self.position = self.position + self.speed*self.direction
            self.rect.center = self.position.xy #need to move the rectangle to draw

        #if pressed[pygame.K_SPACE] == 1:
        #    if (time.time() - self.last_shoot_time) > 0.2:
        #        direction = pygame.Vector2(0,-1)
        #        l = Laser(self.position + (direction*40), direction, 10)
        #        self.last_shoot_time = time.time()

        screen_rect = pygame.Rect((0, 0), GAME.SCREEN.get_size())
        if GAME.is_sprite_outside_rectangle(self, screen_rect, align=True):
            self.speed = 0
        else: 
            self.speed = 4

        return

