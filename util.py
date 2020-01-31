import pygame
from screen import *
from startscreen import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def text_objects(text, font, textColor):

    textSurface = font.render(text, True, textColor)
    return textSurface, textSurface.get_rect()


def generateButton(msg,x,y,w,h,ic,ac,textColor,fontSize,scr,action=None):
    '''
    :param textColor: tuple
    :param fontSize:
    :param scr: Screen
    :param action: function
    :return: void
    '''

    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()
    #print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.ellipse(scr.getScreen(), ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.ellipse(scr.getScreen(), ic,(x,y,w,h))

    generateText(msg, fontSize, textColor, x+(w/2), y+(h/2), scr)


def generateText(text, fontSize, textColor, x, y, scr):
    '''
    text: String
    fontSize : num
    textColor: tuple
    x,y : center
    type: String - "button" or else
    '''

    fontConfig = pygame.font.Font("Akron_Shades_NBP_Regular.ttf", fontSize)
    TextSurf, logo = text_objects(text, fontConfig, textColor)
    logo.center = (x,y)

    scr.getScreen().blit(TextSurf, logo)
