import pygame
from util import *
import pandas as pd


class QuestionManager:
    def __init__(self):
        self.data = pd.read_csv("perguntas.csv")
        self.questions = self.data["PERGUNTA"]
        self.options = [self.data["A"], self.data["B"], self.data["C"], self.data["D"]]
        self.answer = self.data["GABARITO"]

    def getQuestions(self):
        return self.questions

    def getOptions(self):
        return self.options

    def getAnswer(self):
        return self.answer



