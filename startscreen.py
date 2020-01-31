import pygame
from screen import *
from util import *


class StartScreen(Screen):
    def __init__(self):
        self.btnStartGame = button("Start", 400, 150, 100, 60, ())