# name: David McDonald
# start date: 12/30/1016
# last update: 12/31/2016
# description: Rogue-like text based game
import pygame
import random
import time
import sys
import os

pygame.init()
pygame.mixer.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

FPS = 60
displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Rogue Python')

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
archer = pygame.image.load('archer.png')#player
boss1 = pygame.image.load('gargoyle.png')

def Player(playerX,playerY):
    gameDisplay.blit(archer,(playerX-16,playerY-16))

def Boss1(bossX,bossY):
    gameDisplay.blit(boss1,(bossX-48,bossY-48))

def BossAI(bossX,bossDir):
    if bossDir == True:#travel right
        bossX += 5
    elif bossDir == False:#travel left
        bossX -= 5
    if bossX <=50:
        bossDir = True
    if bossX >=750:
        bossDir = False
    rand = random.randint(1, 100)
    if rand > 99:
        bossDir = not bossDir
    return bossX, bossDir

def text_objects(text,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,posX,posY):
    textSurf, textRect = text_objects(msg,color)
    textRect.center =  (posX),(posY)
    gameDisplay.blit(textSurf,textRect)

def gameLoop():
    playerX = displayWidth/2
    playerY = 50
    changeX = 0
    changeY = 0
    playerHP = 100

    bossX = displayWidth/2
    bossY = displayHeight-50
    bossHP = 100
    bossDir = True #boss move direction: true is right and left is false
    bossfight = False
    gameExit = False
    
    while not bossfight:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    bossfight = True
        message_to_screen("Welcome to Python Boss Fights!",white,displayWidth/2,displayHeight/4)
        message_to_screen("Press right arrow to continue...",white,displayWidth/2,displayHeight/3)
        pygame.display.update() #update canvas
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changeX = -5
                elif event.key == pygame.K_RIGHT:
                    changeX = 5
                #elif event.key == pygame.K_UP:
                #    changeY = -2
                #elif event.key == pygame.K_DOWN:
                #    changeY = 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    changeX = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeY = 0
        if playerX > 790 or playerX < 10:
            changeX = -changeX
        #if playerY > 590 or playerY < 10:
        #    changeY = -changeY

        playerX += changeX
        playerY += changeY

        gameDisplay.fill(black) #background drawn first
        Player(playerX,playerY)
        bossX, bossDir = BossAI(bossX,bossDir)
        Boss1(bossX,bossY)
        pygame.display.update() #update canvas
            
        clock.tick(FPS)
        
    pygame.quit()
    quit()

gameLoop()
