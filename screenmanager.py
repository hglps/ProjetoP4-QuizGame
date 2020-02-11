import pygame
from startscreen import *
from levelonescreen import *
import util


class ScreenManager:
    def __init__(self):
        self.screen = StartScreen("Quizzer", "images/icon.png", 900, 600, -1, 3, 0, "images/backgroundStart.png")
        self.state = -1
        self.screen.showScreen()

    def showScreen(self):
        # list of screens / index == question
        self.screen.showScreen()

        if self.screen.getState() == -1:
            self.screen = StartScreen("Quizzer", "images/icon.png", 900, 600, -1, 3, 0, "images/backgroundStart.png")
        else:
            self.screen = LevelOneScreen("Quizzer", "images/icon.png", 900, 600, self.screen.getState(), self.screen.getLives(), self.screen.getScore(), "images/questionbg.png")
        # elif self.screen.getState() == 1:
        #     self.screen = LevelOneScreen("Quizzer", "icon.png", 900, 600, 1, "questionbg.png")
