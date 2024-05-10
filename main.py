''' Main Game Code '''
import pygame
import pygame.locals as CONSTANTS
import os, sys, random, time, math
import game_globals as GAME
from spaceship import Spaceship
from enemy import Enemy

'''----------------------- Initialisation --------------------------'''
# Initialising imported Pygame modules (basically getting things started) #
pygame.init()
pygame.mixer.init()
pygame.font.init()

# window
pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Asteroids') # Setting bar title of game window #

# Global game objects and variables
CLOCK = pygame.time.Clock() # Creating a 'clock' variable that tracks time #
FONT = pygame.font.SysFont('Impact', 60)
FONT2 = pygame.font.SysFont('Ariel', 30)
BACKGROUND_IMAGE = pygame.image.load("images/background.jpg")

GAME.SCREEN = pygame.display.get_surface() # Where graphics/visual output displayed #
GAME.EXIT = False
GAME.STATE = "Start Game"
GAME.PLAYER = None
GAME.ENEMY_GROUP = pygame.sprite.Group() #list = [Enemy1,Enemy2 ]
GAME.BULLET_GROUP = pygame.sprite.Group() #list = [Bullet1, Bullet2]
create_enemy_event = pygame.USEREVENT + 1 #event number

'''-------------------------- Game Loop --------------------------'''
while not GAME.EXIT:

    CLOCK.tick(60) #60 frames per seconds

    for event in pygame.event.get():
        if event.type == CONSTANTS.QUIT:
            GAME.EXIT = True
        elif event.type == create_enemy_event:
            e = Enemy(100,100)
            GAME.ENEMY_GROUP.add(e)
            pygame.time.set_timer(create_enemy_event, 2000)

    #get inputs
    pressed = pygame.key.get_pressed() #returns []
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) # returns (x,y)
    mouse_buttons = pygame.mouse.get_pressed() # return (0, 0, 0) if left button click

    GAME.SCREEN.blit(BACKGROUND_IMAGE, (0,0))

    #Start Game Screen
    if GAME.STATE == "Start Game":
        GAME.SCORE = 0
        text = FONT.render("Press SPACE to Start", True, (255,0,0) )
        GAME.SCREEN.blit(text, (280,320))

        #get the mouse position
        x = mouse_pos.x
        y = mouse_pos.y
        position_text = "X: " + str(x) + " Y: " + str(y)
        text = FONT2.render(position_text, True, (255,255,255))
        GAME.SCREEN.blit(text, (10,10))

        #test to see if space is pressed
        if pressed[pygame.K_SPACE] == 1:
            GAME.STATE = "Running"
            GAME.MUSIC = pygame.mixer.Sound("sounds/sunsetreverie.mp3")
            GAME.MUSIC.play(-1) 
            GAME.PLAYER = Spaceship(512, 384)
            pygame.time.set_timer(create_enemy_event, 2000)

    #Running Game Screen
    elif GAME.STATE == "Running":
        text = FONT2.render("Score: " + str(GAME.SCORE), True, (255,0,0) )
        GAME.SCREEN.blit(text, (10,10))

        #update my sprites
        GAME.PLAYER.update(pressed, mouse_pos, mouse_buttons)
        GAME.ENEMY_GROUP.update()
        GAME.BULLET_GROUP.update()

        #check for collisions
        if pygame.sprite.groupcollide(GAME.ENEMY_GROUP, GAME.BULLET_GROUP, True, True):
            GAME.SCORE = GAME.SCORE + 1

        if pygame.sprite.spritecollide(GAME.PLAYER, GAME.ENEMY_GROUP, True):
            GAME.STATE = "Start Game"
            GAME.ENEMY_GROUP.empty()
            GAME.BULLET_GROUP.empty()
            GAME.PLAYER.kill()
            GAME.MUSIC.stop()

        #draw my sprites
        GAME.PLAYER.draw(GAME.SCREEN) #call every frame
        GAME.ENEMY_GROUP.draw(GAME.SCREEN)
        GAME.BULLET_GROUP.draw(GAME.SCREEN)

    if GAME.STATE == "Game Over":
        pass

    pygame.display.flip() #all drawing that was done off screen is now flipped onto the screen
    
'''------------------------ Exit --------------------------------'''
print("Exiting")
pygame.quit()
sys.exit(0)


