import pygame
from screen import *
from util import *


class StartScreen(Screen):
    def __init__(self, caption, icon, width, height, backgroundImg):
        super().__init__(caption, icon, width, height, backgroundImg)
        self.btnStartGame = generateButton("Start", 570, 120, 130, 60, (12, 191, 117), (17, 150, 124), BLACK, 20,
                                           super().getScreen(), actionButton, 1)
        self.btnExit = generateButton("Quit", 570, 200, 130, 60, (12, 191, 117), (17, 150, 124), BLACK, 20,
                                      super().getScreen(), pygame.quit)


####################################################################
# currentScreen = Screen("Quiz Game", "icon.png", 900, 600)


# def testPrint():
#     print("pressed button")
#     import main
#     main.state = 1
#
#     # state = 1
