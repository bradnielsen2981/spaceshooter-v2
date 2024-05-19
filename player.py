''' Spaceship Sprite Code '''
import pygame
from laser import Laser
import game_globals as GAME
import math, time

#Sprite Object for the Space Ship
class Player(pygame.sprite.Sprite): ##Q what does sprite class mean?

    # Constructing the player
    def __init__(self, x, y):
        super().__init__() 
        
        # Sprite Image
        self.image = pygame.image.load("images/robotsprite.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.originalimage = self.image.copy() #need original image to rotate

        # Sprite Movement
        self.vspeed = 0
        self.hspeed = 0
        self.speedlimit = 5
        self.friction = 0.1
        self.gravity = 0.1

        self.invincible = False

        # health
        self.health = 100

        # Sprite Positioning
        self.rect = self.image.get_rect() # gets rectangle of the image #
        self.rect.center = (x,y)
        
        self.last_shoot_time = 0 #used to stop machine gun effect
        return
    
    # draw the sprite
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        return
    
    # Updates the sprite every frame
    def update(self, pressed, mouse_pos, mouse_buttons):

        self.rect.centerx += self.hspeed
        self.rect.centery += self.vspeed

        if self.vspeed > 0:
            on_platform = False
            for platform in GAME.PLATFORM_GROUP:
                collision = pygame.sprite.collide_rect(self, platform)
                if collision:
                    if self.is_sprite_landing_on_platform(platform.rect, align=True):
                        on_platform = True

            if on_platform == False:
                self.vspeed += self.gravity  
        elif pressed[pygame.K_w] and self.vspeed == 0:
            self.vspeed = -5
        else:
            self.vspeed += self.gravity

        if pressed[pygame.K_a]:
            self.hspeed = -5
        elif pressed[pygame.K_d]:
            self.hspeed = 5
        else:
            if abs(self.hspeed) > 0:
                self.hspeed += (self.friction)*-1*(self.hspeed/abs(self.hspeed))
                if abs(self.hspeed) < 0.1:
                    self.hspeed = 0

        screen_rect = pygame.Rect((0, 0), GAME.SCREEN.get_size())
        GAME.is_sprite_outside_rectangle(self, screen_rect, wrap=True)

        #cap vspeed
        if self.vspeed > 10:
            self.vspeed = 10
        
        return

    def is_sprite_landing_on_platform(self, rectangle, align=True):
        landing = False
        if self.rect.top < rectangle.bottom and self.vspeed < 0:
            if align:
                self.rect.top = rectangle.bottom
                self.vspeed = 0
        elif self.rect.bottom > rectangle.top:
            if align:
                self.rect.bottom = rectangle.top - 0.1
                self.vspeed = 0
            landing = True
        elif self.rect.left < rectangle.right:
            if align:
                self.rect.left = rectangle.left
                self.hspeed = 0
        elif self.rect.right > rectangle.left:
            if align:
                self.rect.right = rectangle.left
                self.hspeed = 0
        return landing
