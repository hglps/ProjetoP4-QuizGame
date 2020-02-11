import pygame
import util
from startscreen import *


class Screen:

    def __init__(self, caption, icon, width, height, state, lives, score):
        self.caption = caption  # string
        self.icon = icon  # string
        self.width = width  # numeric
        self.height = height  # idem
        self.state = state
        self.screen = None  # display object
        self.lives = lives
        self.score = score
        # self.backgroundImg = util.loadImage(backgroundImg)
        self.setIcon()
        self.setCaption()
        self.setScreen(self.width, self.height)
        # self.showBackgroundImg()

    def getLives(self):
        return self.lives

    def setLives(self, lives):
        self.lives = lives

    def getScore(self):
        return self.score

    def setIcon(self):
        icon = pygame.image.load(self.icon)
        pygame.display.set_icon(icon)

    def setCaption(self):
        pygame.display.set_caption(self.caption)

    def getDimensions(self):
        dimensions = (self.width, self.height)
        return dimensions

    def setDimensions(self, width, height):
        self.width = width
        self.height = height

    def setScreen(self, width, height):
        self.setDimensions(width, height)
        self.screen = pygame.display.set_mode((self.width, self.height))

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    # def showBackgroundImg(self):
    #     self.screen.blit(self.backgroundImg, (0,0))

    def getScreen(self):
        return self.screen
