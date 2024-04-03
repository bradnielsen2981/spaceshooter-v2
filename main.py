''' Main Game Code '''
import pygame
from pygame.locals import *
import os, sys, random
import game_globals as GAME
from spaceship import Spaceship
from laser import Laser

'''-----------------------Initialisation--------------------------'''
# Initialising imported Pygame modules (basically getting things started) #
sys.tracebacklimit = 1
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
GAME.ALL_SPRITE_GROUP = pygame.sprite.Group()
GAME.PLAYER = Spaceship(500, 300)
GAME.EXIT = False
GAME.STATE = "Running"
GAME.MUSIC = pygame.mixer.Sound("sounds/sunsetreverie.mp3")
GAME.MUSIC.play(-1)

'''-------------------------- Game Loop --------------------------'''
# Loop game until EXIT = True
while not GAME.EXIT:

    # Control the rate at which game run --> framerate set to 60fps #
    CLOCK.tick(60)

    # Process events #
    for event in pygame.event.get():
        if event.type == QUIT:
            GAME.EXIT = True
        elif event.type == USEREVENT + 1:
            #clear the time
            pygame.time.set_timer(USEREVENT + 1, 0)

    # Process user input
    pressed = pygame.key.get_pressed() #returns []
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) # returns (x,y)
    mouse_buttons = pygame.mouse.get_pressed() # return (1, 0, 0) if left button click
    # do something with the input

    GAME.ALL_SPRITE_GROUP.update(pressed, mouse_pos, mouse_buttons) #update all sprites by calling their update function
    #DRAWING CODE---------------------------------
    #GAME.SCREEN.fill((0, 0, 0))
    GAME.SCREEN.blit(BACKGROUND_IMAGE, (0,0))

    GAME.ALL_SPRITE_GROUP.draw(GAME.SCREEN) # draw all sprites by calling their draw function
    
    LABEL = FONT.render("x: " + str(mouse_pos.x) + " y: " + str(mouse_pos.y),True,(200,200,200))
    GAME.SCREEN.blit(LABEL, (50,50))
    pygame.display.flip()
    
'''------------------------ Exit --------------------------------'''
print("Exiting")
pygame.quit()
sys.exit(0)


