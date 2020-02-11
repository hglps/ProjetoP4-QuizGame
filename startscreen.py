import pygame
from screen import *
import util


class StartScreen(Screen):
    def __init__(self, caption, icon, width, height, state, lives, score, backgroundImg):
        super().__init__(caption, icon, width, height, state, lives, score)
        self.backgroundImg = util.loadImage(backgroundImg)

    def showScreen(self):
        self.showBackgroundImg()
        self.generateButton("Iniciar", 570, 120, 130, 60, (12, 191, 117), (17, 150, 124), util.BLACK, 20,
                            super().getScreen(), self.setState, super().getState() + 1)
        self.generateButton("Sair", 570, 200, 130, 60, (12, 191, 117), (17, 150, 124), util.BLACK, 20,
                            super().getScreen(), pygame.quit)

        pygame.display.update()

    def showBackgroundImg(self):
        self.screen.blit(self.backgroundImg, (0, 0))

    def setState(self, state):
        super().setState(state)

    def text_objects(self, text, font, textColor):

        textSurface = font.render(text, True, textColor)
        return textSurface, textSurface.get_rect()

    def generateButton(self, msg, x, y, w, h, ic, ac, textColor, fontSize, scr, action=None, param=None):
        """
        :param param: 'action' parameter
        :param msg: string
        :param x: int
        :param y: int
        :param w: int
        :param h: int
        :param ic: tuple
        :param ac: tuple
        :param textColor: tuple
        :param fontSize: int
        :param scr: Screen.getScreen()
        :param action: function
        :return:
        """

        mouse = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()
        # print(click)

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.ellipse(scr, ac, (x, y, w, h))

            if click[0] == 1:
                if param != None:
                    action(param)
                else:
                    action()
                if action == pygame.quit:
                    exit()
        else:
            pygame.draw.ellipse(scr, ic, (x, y, w, h))

        self.generateText(msg, fontSize, textColor, x + (w / 2), y + (h / 2), scr)

    def generateText(self, text, fontSize, textColor, x, y, scr):
        """
        :param text: string
        :param fontSize: int
        :param textColor: tuple
        :param x: int
        :param y: int
        :param scr: Screen.getScreen()
        :return:
        """

        fontConfig = pygame.font.Font("fonts/Akron_Shades_NBP_Regular.ttf", fontSize)
        TextSurf, logo = self.text_objects(text, fontConfig, textColor)
        logo.center = (x, y)

        scr.blit(TextSurf, logo)






#
# def actionButton(stateParam=None):
#     print("foi")
#     if stateParam != None:
#         super().
#
#         print("agr a main state eh ", stateParam,"  ", main.state)
