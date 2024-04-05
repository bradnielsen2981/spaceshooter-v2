''' Spaceship Sprite Code '''
import pygame
import game_globals as GAME
import math, time

#Sprite Object for the Space Ship
class Enemy(pygame.sprite.Sprite): ##Q what does sprite class mean?

    # Constructing spaceship object #
    def __init__(self, x, y):
        super().__init__() 
        
        # Sprite Image
        self.image = pygame.image.load("images/alien.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.originalimage = self.image.copy() #need original image to rotate

        # Sprite Positioning
        self.rect = self.image.get_rect() # gets rectangle of the image #
        self.position = pygame.Vector2(x,y)
        self.rect.center = self.position.xy

        # Sprite Movement
        self.direction = pygame.Vector2(GAME.PLAYER.position - self.position).normalize() 
        self.speed = 3

        #create timers
        self.direction_timer = time.time()
        self.speed_timer = time.time()

        #add itself to the enemy sprite group
        GAME.ENEMY_GROUP.add(self)
        return
    
    # Updates the sprite every frame
    def update(self):

        #self.direction = pygame.Vector2(GAME.PLAYER.position - self.position).normalize()
        #set timed change of direction
        if time.time() - self.direction_timer > 2:
            self.direction_timer = time.time()
            self.direction = pygame.Vector2(GAME.PLAYER.position - self.position).normalize() 

        if time.time() - self.speed_timer > 5:
            self.speed_timer = time.time()
            self.speed += 1

        self.position = self.position + self.speed*self.direction
        self.rect.center = self.position.xy #need to move the rectangle to draw
        
        screen_rect = pygame.Rect((0, 0), GAME.SCREEN.get_size())
        GAME.is_sprite_outside_rectangle(self, screen_rect, align=True)

        #tests for collision and removes any collided sprites
        if pygame.sprite.groupcollide(GAME.BULLET_GROUP, GAME.ENEMY_GROUP, True, True):
            GAME.SCORE += 1
        return



