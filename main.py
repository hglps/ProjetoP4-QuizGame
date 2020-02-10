import pygame
from pygame.locals import *

# from screen import *
from startscreen import *
from levelonescreen import *
from util import *

'''
state = 0 : Start Screen
state = 1 : Level 1 Screen
state = 2 : Level 2 Screen
state = 3 : Finished Game Screen
'''

pygame.init()


global state
state = 0

# color = (78, 150, 124)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if state == 0:
        currentScreen = StartScreen("Quizzer", "icon.png", 900, 600, "fundogreen2.png")
    elif state == 1:
        currentScreen = LevelOneScreen("Quizzer", "icon.png", 900, 600, "questionbg.png")
        currentScreen.showScreen()

    pygame.display.update()

