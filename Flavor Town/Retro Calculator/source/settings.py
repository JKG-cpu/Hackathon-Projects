import pygame

from sys import exit as close_game
from os import system, name
from os.path import join

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 600

# Functions
def cc():
    system("cls" if name == "nt" else "clear")
    
def solve(equation: str):
    return eval(equation, {"__builtins__": None})