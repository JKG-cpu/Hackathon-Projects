from .settings import *

class Calc:
    def __init__(self) -> None:
        self.equation = ""
        self.eval_equation = ""
        self.answer = ""

    def get_equation(self) -> str:
        return self.equation

    def solve(self, equation: str):
        try:
            return str(eval(equation))
        except Exception:
            return "Error"

    def format_answer(self, answer: str) -> str:
        try:
            num = float(answer)
        
        except ValueError:
            return "Error"
    
        if num == 0:
            return "0"
    
        abs_num = abs(num)

        if abs_num > 1e10 or abs_num < 1e-6:
            return f"{num:2e}"
        
        if num.is_integer():
            return str(int(num))

        return str(round(num, 8))

    def check_input(self, number_slots: pygame.sprite.Group):
        mouse_pos = pygame.mouse.get_pos()

        for sprite in number_slots:
            if sprite.foreground_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_just_pressed()[0]:
                    sid = sprite.id

                    if sid == "DEL":
                        self.equation = self.equation[:-1]
                        self.eval_equation = self.eval_equation[:-1]

                    elif sid == "CLEAR":
                        self.equation = ""
                        self.eval_equation = ""
                        self.answer = ""

                    elif sid == "POSNEG":
                        if self.eval_equation.startswith("-"):
                            self.eval_equation = self.eval_equation[1:]
                            self.equation = self.equation[1:]
                        else:
                            self.eval_equation = "-" + self.eval_equation
                            self.equation = "-" + self.equation

                    elif sid == "=":
                        self.answer = self.format_answer(self.solve(self.eval_equation))
                        self.equation = self.answer
                        self.eval_equation = self.answer

                    # ---- NUMBERS & OPERATORS ----
                    else:
                        self.equation += sid

                        if sid in OPERATOR_MAP:
                            self.eval_equation += OPERATOR_MAP[sid]
                        elif sid == "%":
                            self.eval_equation += "/100"
                        else:
                            self.eval_equation += sid

    def update(self, number_slots: pygame.sprite.Group):
        self.check_input(number_slots)