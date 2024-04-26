''' Main Game Code '''
import pygame
import pygame.locals as CONSTANTS
import os, sys, random, time, math
import game_globals as GAME

'''----------------------- Initialisation --------------------------'''
# Initialising imported Pygame modules (basically getting things started) #
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Asteroids') # Setting bar title of game window #

# Global game objects and variables
CLOCK = pygame.time.Clock() # Creating a 'clock' variable that tracks time #
FONT = pygame.font.SysFont('Comic Sans MS', 30)
BACKGROUND_IMAGE = pygame.image.load("images/background.jpg")

GAME.SCREEN = pygame.display.get_surface() # Where graphics/visual output displayed #
GAME.EXIT = False
GAME.STATE = "Start Game"

'''-------------------------- Game Loop --------------------------'''
while not GAME.EXIT:

    CLOCK.tick(60) #60 frames per seconds

    for event in pygame.event.get():
        if event.type == CONSTANTS.QUIT:
            GAME.EXIT = True

    pressed = pygame.key.get_pressed() #returns []
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) # returns (x,y)
    mouse_buttons = pygame.mouse.get_pressed() # return (0, 0, 0) if left button click

    GAME.SCREEN.blit(BACKGROUND_IMAGE, (0,0))

    if GAME.STATE == "Start Game":
        text = FONT.render("START SCREEN",True,(255,0,0))
        GAME.SCREEN.blit(text, (480,370))
        x = str(mouse_pos.x)
        y = str(mouse_pos.y)
        mouse_text = FONT.render("x: " + x + " y: " + y,True,(0,255,0))
        GAME.SCREEN.blit(mouse_text, (10,10))

        

    pygame.display.flip() #all drawing that was done off screen is now flipped onto the screen
    
'''------------------------ Exit --------------------------------'''
print("Exiting")
pygame.quit()
sys.exit(0)


