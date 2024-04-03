''' Main Game Code '''
import pygame
from pygame.locals import *
import os, sys, random
import game_globals as GAME
from spaceship import Spaceship
from enemy import Enemy
from laser import Laser

'''----------------------- Initialisation --------------------------'''
# Initialising imported Pygame modules (basically getting things started) #
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.set_mode((1024, 800))
pygame.display.set_caption('Space Game') # Setting bar title of game window #

# Global game objects and variables
CLOCK= pygame.time.Clock() # Creating a 'clock' variable that tracks time #
FONT = pygame.font.SysFont('Comic Sans MS', 30)
BACKGROUND_IMAGE = pygame.image.load("images/background.jpg")

GAME.SCREEN = pygame.display.get_surface() # Where graphics/visual output displayed #
GAME.PLAYER = Spaceship(500, 300)
GAME.EXIT = False
GAME.STATE = "Running"
GAME.MUSIC = pygame.mixer.Sound("sounds/sunsetreverie.mp3")
GAME.MUSIC.play(-1)
GAME.BULLET_GROUP = pygame.sprite.Group()
GAME.ENEMY_GROUP = pygame.sprite.Group()

create_enemy_event = pygame.USEREVENT + 1 #create a number of the event
pygame.time.set_timer(create_enemy_event, 5) 

'''-------------------------- Game Loop --------------------------'''
while not GAME.EXIT:

    # Control the rate at which game run --> framerate set to 60fps #
    CLOCK.tick(60)

    # GAME LOGIC ------------------------------------

    # Process events
    for event in pygame.event.get():
        if event.type == QUIT:
            GAME.EXIT = True
        elif event.type == create_enemy_event:
            enemy = Enemy(10,10)
            pygame.time.set_timer(create_enemy_event, 1000) #create a looping time

    # Collect user input
    pressed = pygame.key.get_pressed() #returns []
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) # returns (x,y)
    mouse_buttons = pygame.mouse.get_pressed() # return (1, 0, 0) if left button click
    # Update Sprites
    if GAME.PLAYER:
        GAME.PLAYER.update(pressed, mouse_pos, mouse_buttons) #update all sprites by calling their update function
    GAME.BULLET_GROUP.update()
    GAME.ENEMY_GROUP.update()

    # GAME DRAWING ---------------------------------

    #GAME.SCREEN.fill((0, 0, 0))
    GAME.SCREEN.blit(BACKGROUND_IMAGE, (0,0))
    GAME.BULLET_GROUP.draw(GAME.SCREEN)
    GAME.ENEMY_GROUP.draw(GAME.SCREEN)
    if GAME.PLAYER:
        GAME.PLAYER.draw(GAME.SCREEN) # draw sprite
    LABEL = FONT.render("x: " + str(mouse_pos.x) + " y: " + str(mouse_pos.y),True,(200,200,200))
    GAME.SCREEN.blit(LABEL, (50,50))

    pygame.display.flip() #all drawing that was done off screen is now flipped onto the screen
    
'''------------------------ Exit --------------------------------'''
print("Exiting")
pygame.quit()
sys.exit(0)


