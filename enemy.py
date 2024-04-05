import pygame
import game_globals as GAME
import math, time

#Sprite Object for the Space Ship
class Enemy(pygame.sprite.Sprite): 

    # Constructing spaceship object #
    def __init__(self, x, y):
        super().__init__() 
        
        # Sprite Image
        self.image = pygame.image.load("images/alien.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.originalimage = self.image.copy() #need original image to rotate

        # Sprite Movement
        self.direction = pygame.Vector2(1,0)
        self.speed = 3

        # Sprite Positioning
        self.rect = self.image.get_rect() # gets rectangle of the image #
        self.position = pygame.Vector2(x,y)
        self.rect.center = self.position.xy

        #self.timer = 0

        #add itself to the enemy sprite group
        GAME.ENEMY_GROUP.add(self)
        return
    
    # Updates the sprite every frame
    def update(self):

        #set timed change of direction
        #if time.time() - self.timer > 3:
        #    self.timer = time.time()
        #    self.direction = pygame.Vector2(GAME.PLAYER.position - self.position).normalize() 

        self.position = self.position + self.speed*self.direction
        self.rect.center = self.position.xy #need to move the rectangle to draw
        
        screen_rect = pygame.Rect((0, 0), GAME.SCREEN.get_size())
        if GAME.is_sprite_outside_rectangle(self, screen_rect, align=True):
            self.direction = -self.direction
            #self.position = self.position + pygame.Vector2(0,80)

        #tests for collision and removes any collided sprites
        if pygame.sprite.groupcollide(GAME.BULLET_GROUP, GAME.ENEMY_GROUP, True, True):
            print("Enemy hit")
            GAME.SCORE += 1
        return



