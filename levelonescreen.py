import pygame
from util import *
from screen import *
from questionmanager import *
import random


class LevelOneScreen(Screen):
    def __init__(self, caption, icon, width, height, backgroundImg):
        super().__init__(caption, icon, width, height, backgroundImg)
        self.screenManager = QuestionManager()

    def showScreen(self):
        positions = renderQuestionRects(super().getScreen())
        selectedQuestions, selectedOptions, selectedAnswer = self.selectQuestions()



    def selectQuestions(self):
        arrayQuestions = []
        for i in range(0, 5):
            index = random.randint(0, 19)
            if index not in arrayQuestions:
                arrayQuestions.append(index)

        for i in range(0, 5):
            selectedQuestions = [self.screenManager.getQuestions()[item] for item in arrayQuestions]
            selectedOptions = [self.screenManager.getOptions()[item] for item in arrayQuestions]
            selectedAnswer = [self.screenManager.getAnswer()[item] for item in arrayQuestions]

        return selectedQuestions, selectedOptions, selectedAnswer

    def showQuestion(self):
        mouse = pygame.mouse.get_pos()
        if mouse[0]  # pegar intervalo e mostrar pergunta

    def text_objects(text, font, textColor):

        textSurface = font.render(text, True, textColor)
        return textSurface, textSurface.get_rect()

    def button(msg, x, y, w, h, ic, ac, textColor, fontSize, scr, action=None):

        mouse = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()

        if x + w >= mouse[0] >= x and y + h >= mouse[1] >= y:
            pygame.draw.ellipse(scr, ac, (x, y, w, h))

            if click[0] == 1:
                print("clicked")  # problem : need to click twice to work ;-;

                action()
                if action == pygame.quit:
                    exit()
        else:
            pygame.draw.ellipse(scr, ic, (x, y, w, h))

        generateText(msg, fontSize, textColor, x + (w / 2), y + (h / 2), scr)

    def generateText(text, fontSize, textColor, x, y, scr):
        """
        :param text: string
        :param fontSize: int
        :param textColor: tuple
        :param x: int
        :param y: int
        :param scr: Screen.getScreen()
        :return:
        """

        fontConfig = pygame.font.Font("Akron_Shades_NBP_Regular.ttf", fontSize)
        TextSurf, logo = text_objects(text, fontConfig, textColor)
        logo.center = (x, y)

        scr.blit(TextSurf, logo)
