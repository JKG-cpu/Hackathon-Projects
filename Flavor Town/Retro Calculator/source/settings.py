import pygame
import random

from pygame.math import Vector2 as vector
from sys import exit as close_game
from os import system, name
from os.path import join

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 600
OPERATOR_MAP = {
    "×": "*",
    "÷": "/",
    "+": "+",
    "-": "-",
}

# Functions
def cc():
    system("cls" if name == "nt" else "clear")
    
def solve(equation: str):
    return eval(equation, {"__builtins__": None})

# Classes
class MessageLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data = self.load_data()
    
    def load_data(self) -> list[str]:
        try:
            with open(self.file_path, "r", encoding = "utf-8") as f:
                return f.read()
        
        except Exception as e:
            raise ValueError(f"Error Loading Messages: {e}")