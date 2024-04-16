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
pygame.display.set_caption('Space Game') # Setting bar title of game window #

# Global game objects and variables
CLOCK = pygame.time.Clock() # Creating a 'clock' variable that tracks time #
FONT = pygame.font.SysFont('Comic Sans MS', 30)
BACKGROUND_IMAGE = pygame.image.load("images/background.jpg")

GAME.SCREEN = pygame.display.get_surface() # Where graphics/visual output displayed #
GAME.EXIT = False
GAME.STATE = "Start Game"

'''-------------------------- Game Loop --------------------------'''
while not GAME.EXIT:

    # Control the rate at which game run --> framerate set to 60fps #
    CLOCK.tick(60)

    # GAME LOGIC ------------------------------------
    # Process events
    for event in pygame.event.get():
        if event.type == CONSTANTS.QUIT:
            GAME.EXIT = True

    # Collect user input
    pressed = pygame.key.get_pressed() #returns []
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) # returns (x,y)
    mouse_buttons = pygame.mouse.get_pressed() # return (0, 0, 0) if left button click

    #GAME.SCREEN.blit(BACKGROUND_IMAGE, (0,0))
    GAME.SCREEN.fill((0, 0, 255))

    #if GAME.STATE == "Start Game":
        #text = FONT.render("Welcome to Pygame",True,(200,200,200))
        #GAME.SCREEN.blit(text, (10,10))
        #coord = FONT.render("x: " + str(mouse_pos.x) + " y: " + str(mouse_pos.y),True,(200,200,200))
        #GAME.SCREEN.blit(coord, (10,10))

    pygame.display.flip() #all drawing that was done off screen is now flipped onto the screen
    
'''------------------------ Exit --------------------------------'''
print("Exiting")
pygame.quit()
sys.exit(0)


