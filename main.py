''' Main Game Code '''
import pygame
from pygame.locals import *
import os, sys, random, time, math
import game_globals as GAME
from spaceship import Spaceship
from enemy import Enemy
from laser import Laser

'''----------------------- Initialisation --------------------------'''
# Initialising imported Pygame modules (basically getting things started) #
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Space Game') # Setting bar title of game window #

# Global game objects and variables
CLOCK= pygame.time.Clock() # Creating a 'clock' variable that tracks time #
FONT = pygame.font.SysFont('Comic Sans MS', 30)
BACKGROUND_IMAGE = pygame.image.load("images/background.jpg")

GAME.SCREEN = pygame.display.get_surface() # Where graphics/visual output displayed #
GAME.EXIT = False
GAME.STATE = "Start Game"
GAME.BULLET_GROUP = pygame.sprite.Group()
GAME.ENEMY_GROUP = pygame.sprite.Group()

create_enemy_event = pygame.USEREVENT + 1 #create a number of the event

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
            #choose a random corner
            position = random.choice([(0,0),(1024,0),(0,768),(1024,768)])
            enemy = Enemy(position[0],position[1])
            pygame.time.set_timer(create_enemy_event, 1000) #create a looping time


    # Collect user input
    pressed = pygame.key.get_pressed() #returns []
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) # returns (x,y)
    mouse_buttons = pygame.mouse.get_pressed() # return (1, 0, 0) if left button click

    GAME.SCREEN.blit(BACKGROUND_IMAGE, (0,0))
    #GAME.SCREEN.fill((0, 0, 0))

    if GAME.STATE == "Start Game":
        coord = FONT.render("x: " + str(mouse_pos.x) + " y: " + str(mouse_pos.y),True,(200,200,200))
        GAME.SCREEN.blit(coord, (10,10))
        button_rect = pygame.rect.Rect(460,330,200,100)
        pygame.draw.rect(GAME.SCREEN,(200,0,0),button_rect) 
        button_text = FONT.render("Play",True,(200,200,200))
        GAME.SCREEN.blit(button_text,(520,360))
        
        if mouse_buttons[0] == 1:
            if button_rect.collidepoint(mouse_pos):
                GAME.STATE = "Running"
                GAME.STARTTIME = time.time()
                GAME.PLAYER = Spaceship(500,300)
                GAME.MUSIC = pygame.mixer.Sound("sounds/sunsetreverie.mp3")
                GAME.MUSIC.play(-1)
                pygame.time.set_timer(create_enemy_event, 1000)

    elif GAME.STATE == "Running":
        # Update Sprites
        if GAME.PLAYER:
            GAME.PLAYER.update(pressed, mouse_pos, mouse_buttons) #update all sprites by calling their update function
        GAME.BULLET_GROUP.update()
        GAME.ENEMY_GROUP.update()

        # GAME DRAWING ---------------------------------
        GAME.BULLET_GROUP.draw(GAME.SCREEN)
        GAME.ENEMY_GROUP.draw(GAME.SCREEN)
        if GAME.PLAYER:
            GAME.PLAYER.draw(GAME.SCREEN) # draw sprite
        
        timer = int(time.time() - GAME.STARTTIME)
        timer_text = FONT.render("Time: " + str(timer),True,(200,200,200))
        GAME.SCREEN.blit(timer_text,(10,10))
        
        score_text = FONT.render("Score: " + str(GAME.SCORE),True,(200,200,200))
        GAME.SCREEN.blit(score_text,(10,80))

        #draw player health
        health_rect = pygame.rect.Rect(200,10,400,50)
        pygame.draw.rect(GAME.SCREEN,(200,0,0),health_rect)
        playerhealth = int(400*GAME.PLAYER.health/100)
        health_remaining_rect = pygame.rect.Rect(200+(400-playerhealth),10,playerhealth,50)
        pygame.draw.rect(GAME.SCREEN,(0,200,0),health_remaining_rect)         

    elif GAME.STATE == "Game Over":
        LABEL = FONT.render("GAME OVER",True,(200,200,200))
        GAME.SCREEN.blit(LABEL, (400,360))
        pygame.time.set_timer(create_enemy_event, 0)
        GAME.PLAYER = None #Now kill the player
        GAME.BULLET_GROUP.empty()
        GAME.ENEMY_GROUP.empty()

        if time.time() - GAME.ENDTIME > 3:
            GAME.STATE = "Start Game"

    pygame.display.flip() #all drawing that was done off screen is now flipped onto the screen
    
'''------------------------ Exit --------------------------------'''
print("Exiting")
pygame.quit()
sys.exit(0)


