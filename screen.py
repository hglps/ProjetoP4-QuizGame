import pygame


class Screen:

    def __init__(self, caption, icon, width, height):
        self.__caption = caption #string
        self.__icon = icon #string
        self.__width = width #numeric
        self.__height = height #idem
        self.__screen = None #display object
        self.__setIcon()
        self.__setCaption()
        self.setScreen(self.__width, self.__height)

    def __setIcon(self):
        icon = pygame.image.load(self.__icon)
        pygame.display.set_icon(icon)

    def __setCaption(self):
        pygame.display.set_caption(self.__caption)

    def getDimensions(self):
        dimensions = (self.__width, self.__height)
        return dimensions

    def setDimensions(self, width, height):
        self.__width = width
        self.__height = height

    def setScreen(self, width, height):
        self.setDimensions(width, height)
        self.__screen = pygame.display.set_mode((self.__width, self.__height))

    def getScreen(self):
        return self.__screen
