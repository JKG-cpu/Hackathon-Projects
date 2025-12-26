from source import *

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Retro Calculator")

        self.font = pygame.font.Font(join("Flavor Town", "Retro Calculator", "fonts", "BoldPixels.ttf"), 20)
        self.output_font = pygame.font.Font(join("Flavor Town", "Retro Calculator", "fonts", "BoldPixels.ttf"), 25)

        self.number_pad = NumPad(self.font, self.output_font)
        self.number_slots = self.number_pad.get_number_slots()

        self.calc = Calc()

    def run(self):
        while True:
            self.screen.fill("Black")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    cc()
                    close_game()
            
            self.number_pad.draw()
            self.calc.update(self.number_slots)

            # Update Output
            self.number_pad.reset_output(self.calc.get_equation())

            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()