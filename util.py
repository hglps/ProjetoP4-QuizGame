import pygame
import pandas as pd


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# def actionButton(stateParam=None):
#     print("foi")
#     if stateParam != None:
#         import main
#         main.state = stateParam
#
#         print("agr a main state eh ", stateParam,"  ", main.state)


# def text_objects(text, font, textColor):
#
#     textSurface = font.render(text, True, textColor)
#     return textSurface, textSurface.get_rect()
#
#
# def generateButton(msg, x, y, w, h, ic, ac, textColor, fontSize, scr, action=None, param=None):
#     """
#     :param param: 'action' parameter
#     :param msg: string
#     :param x: int
#     :param y: int
#     :param w: int
#     :param h: int
#     :param ic: tuple
#     :param ac: tuple
#     :param textColor: tuple
#     :param fontSize: int
#     :param scr: Screen.getScreen()
#     :param action: function
#     :return:
#     """
#
#     mouse = pygame.mouse.get_pos()
#
#     click = pygame.mouse.get_pressed()
#     # print(click)
#
#     if x+w >= mouse[0] >= x and y+h >= mouse[1] >= y:
#         pygame.draw.ellipse(scr, ac,(x,y,w,h))
#
#         if click[0] == 1:
#             print("clicked")  # problem : need to click twice to work ;-;
#             if param != None:
#                 action(param)
#                 print("foi a action param")
#             else:
#                 action()
#             if action == pygame.quit:
#                 exit()
#     else:
#         pygame.draw.ellipse(scr, ic,(x,y,w,h))
#
#     generateText(msg, fontSize, textColor, x+(w/2), y+(h/2), scr)
#
#
# def generateText(text, fontSize, textColor, x, y, scr):
#     """
#     :param text: string
#     :param fontSize: int
#     :param textColor: tuple
#     :param x: int
#     :param y: int
#     :param scr: Screen.getScreen()
#     :return:
#     """
#
#     fontConfig = pygame.font.Font("Akron_Shades_NBP_Regular.ttf", fontSize)
#     TextSurf, logo = text_objects(text, fontConfig, textColor)
#     logo.center = (x, y)
#
#     scr.blit(TextSurf, logo)


def loadImage(strImage=None):
    return pygame.image.load(strImage)


def getData():
    data = pd.read_csv("perguntas.csv")
    return data

def createBoxCenter():
    print()


# def renderQuestionRects(scr):
#     button("1", 150, 120, 100, 80, (12, 191, 117), (17, 150, 124), WHITE, 25, scr, createBoxCenter)
#     button("2", 270, 90, 100, 80, (12, 191, 117), (17, 150, 124), WHITE, 25, scr, createBoxCenter) # 270
#     button("3", 370, 120, 100, 80, (12, 191, 117), (17, 150, 124), WHITE, 25, scr, createBoxCenter)
#     button("4", 470, 90, 100, 80, (12, 191, 117), (17, 150, 124), WHITE, 25, scr, createBoxCenter)
#     button("5", 570, 120, 100, 80, (12, 191, 117), (17, 150, 124), WHITE, 25, scr, createBoxCenter)
#
#     positionButtons = [[150, 250], [270, 370], [370, 470], [470, 570], [570, 670]]
#     return positionButtons

