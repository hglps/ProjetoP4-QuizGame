import pygame
import util
from screen import *
import random
from question import *


class LevelOneScreen(Screen):
    def __init__(self, caption, icon, width, height, state, lives, score, backgroundImg):
        super().__init__(caption, icon, width, height, state, lives, score)
        self.backgroundImg = util.loadImage(backgroundImg)

    def setState(self, state):
        super().setState(state)

    def showScreen(self):
        self.showBackgroundImg()
        self.verifyLives()
        self.checkEndOfGame()
        selectedQuestion = self.selectQuestion()
        positions = self.renderQuestionRects(super().getScreen(), selectedQuestion)


        # if self.mustNextLevel():
        #     if self.state + 1 > 19:
        #         pass  # end game
        #     self.state += 1

        for i in range(0,4):
            alpha = {0:"A", 1:"B", 2:"C", 3: "D"}
            if positions[i][1] > pygame.mouse.get_pos()[1] > positions[i][0]:
                if 800 > pygame.mouse.get_pos()[0] > 700:  # mudancas p considerar so hitbox do botao
                    if pygame.mouse.get_pressed()[0]:

                        if selectedQuestion.answer == alpha[i]:
                            correctAnswer = util.loadImage("images/correct.png")
                            super().getScreen().blit(correctAnswer, (0, 0))
                            self.state += 1
                            self.lives -= 0
                            self.score += 1
                            lives = "Vidas :" + str(self.lives) + " de 3"
                            self.button(lives, 700, 300, 165, 50, (12, 191, 117), (12, 191, 117), util.BLACK, 30,
                                        super().getScreen(), "rect", print)
                            pygame.display.update()
                            pygame.time.wait(3333)
                        else:
                            wrongAnswer = util.loadImage("images/wrong.png")
                            super().getScreen().blit(wrongAnswer, (0, 0))
                            self.lives -= 1
                            self.state += 1
                            lives = "Vidas :" + str(self.lives) + " de 3"
                            self.button(lives, 700, 300, 165, 50, (12, 191, 117), (12, 191, 117), util.BLACK, 30,
                                        super().getScreen(), "rect", print)
                            pygame.display.update()
                            pygame.time.wait(3333)

        pygame.display.update()

    def verifyLives(self):
        if self.lives == 0:
            gameover = util.loadImage("images/gameover.png")
            super().getScreen().blit(gameover, (0, 0))
            score = "Pontos : " + str(self.score)
            self.button(score, 700, 300, 165, 50, (12, 191, 117), (12, 191, 117), util.BLACK, 30, super().getScreen(),
                        "rect", print)

            self.state = -1
            self.lives = 3
            pygame.display.update()
            pygame.time.wait(5555)

    def checkEndOfGame(self):
        if self.state > 19:
            if self.lives > 0:
                wonGame = util.loadImage("images/winner.png")
                super().getScreen().blit(wonGame, (0, 0))
                pygame.display.update()
                pygame.time.wait(3333)

                endScreen = util.loadImage("images/endscreen.png")
                super().getScreen().blit(endScreen, (0, 0))
                score = "Pontos : " + str(self.score)
                self.button(score, 700, 300, 165, 50, (12, 191, 117), (12, 191, 117), util.BLACK, 30, super().getScreen(), "rect", print )
                pygame.display.update()
                pygame.time.wait(5555)

                self.state = -1
                self.lives = 3
                # END OF GAME
        pass

    def showBackgroundImg(self):
        self.screen.blit(self.backgroundImg, (0, 0))

    def selectQuestion(self):
        selectedQuestion = questionList[self.state]
        return selectedQuestion

    def text_objects(self, text, font, textColor):

        textSurface = font.render(text, True, textColor)
        return textSurface, textSurface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac, textColor, fontSize, scr, form, action=None):

        mouse = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()

        if x + w >= mouse[0] >= x and y + h >= mouse[1] >= y:
            if form == "ellipse":
                pygame.draw.ellipse(scr, ac, (x, y, w, h))
            elif form == "rect":
                pygame.draw.rect(scr, ac, (x, y, w, h))

            if click[0] == 1:
                action()
                if action == pygame.quit:
                    exit()
        else:
            if form == "ellipse":
                pygame.draw.ellipse(scr, ic, (x, y, w, h))
            elif form == "rect":
                pygame.draw.rect(scr, ic, (x, y, w, h))

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
        textsurf, logo = self.text_objects(text, fontConfig, textColor)
        logo.center = (x, y)

        scr.blit(textsurf, logo)

    def renderQuestionRects(self, scr, selectedQuestion):
        self.button(selectedQuestion.question, 100,  50, 500, 100,  (12, 191, 117), (12, 191, 117), util.BLACK,  20, scr, "rect", util.createBoxCenter)  # w = 500, h = 100
        self.button(selectedQuestion.a,        100, 150, 500, 100, (12, 191, 117), (12, 191, 117), util.BLACK, 20, scr, "rect", util.createBoxCenter)  # w = 500, h = 100
        self.button(selectedQuestion.b,        100, 250, 500, 100, (12, 191, 117), (12, 191, 117), util.BLACK, 20, scr, "rect", util.createBoxCenter)  # w = 500, h = 100
        self.button(selectedQuestion.c,        100, 350, 500, 100, (12, 191, 117), (12, 191, 117), util.BLACK, 20, scr, "rect", util.createBoxCenter)  # w = 500, h = 100
        self.button(selectedQuestion.d,        100, 450, 500, 100, (12, 191, 117), (12, 191, 117), util.BLACK, 20, scr, "rect", util.createBoxCenter)  # w = 500, h = 100


        self.button("A", 700, 150, 100, 100, (12, 191, 117), (17, 150, 124), util.BLACK, 20, scr,"ellipse", util.createBoxCenter)  # test with msg
        self.button("B", 700, 250, 100, 100, (12, 191, 117), (17, 150, 124), util.BLACK, 20, scr,"ellipse", util.createBoxCenter)
        self.button("C", 700, 350, 100, 100, (12, 191, 117), (17, 150, 124), util.BLACK, 20, scr,"ellipse", util.createBoxCenter)  # tava com util.createbox....
        self.button("D", 700, 450, 100, 100, (12, 191, 117), (17, 150, 124), util.BLACK, 20, scr,"ellipse", util.createBoxCenter)

        positionButtons = [[150, 250], [250, 350], [350, 450], [450, 550]]
        return positionButtons

