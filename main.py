import pygame
from screen import *
from pygame.locals import *
from util import *

#TODO CHECK Plugins de color palette

pygame.init()

currentScreen= Screen("Quiz Game", "icon.png", 900, 600)

color = (78, 150, 124)

background = pygame.image.load('fundogreen2.png')



def testePrint():

    global currentScreen
    currentScreen.getScreen().fill((0,200,0))




while True:
    #currentScreen.getScreen().fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #generateText("Quiz Game", 80, (0, 0, 0), 450, 100, currentScreen)


    currentScreen.getScreen().blit(background, (0, 0))

    generateButton("Start",    570, 120, 130, 60, (12, 191, 117), (17, 150, 124), BLACK, 20, currentScreen,
                   testePrint)
    generateButton("Button 2", 570, 200, 130, 60, (12, 191, 117), (17, 150, 124), BLACK, 20, currentScreen,
                   testePrint)
    generateButton("Button 3", 570, 280, 130, 60, (12, 191, 117), (17, 150, 124), BLACK, 20, currentScreen,
                   testePrint)
    generateButton("Quit",     570, 360, 130, 60, (12, 191, 117), (17, 150, 124), BLACK, 20, currentScreen,
                   pygame.quit)

    pygame.display.update()

