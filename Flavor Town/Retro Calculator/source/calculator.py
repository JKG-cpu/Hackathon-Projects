from .settings import *

class Calc:
    def __init__(self) -> None:
        pass

    def solve(self, equtation: str) -> float | int:
        return eval(equtation, {"__builtins__": None})

    def check_input(self, number_slots: pygame.sprite.Group):
        mouse_pos = pygame.mouse.get_pos()

        # Check for collision between number slots

    def update(self, number_slots: pygame.sprite.Group):
        self.check_input(number_slots)