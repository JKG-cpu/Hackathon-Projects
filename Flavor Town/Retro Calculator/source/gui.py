from .settings import *

class BaseGUI(pygame.sprite.Sprite):
    def __init__(self, text: str, pos: tuple, size: tuple, font: pygame.font.Font, group: pygame.sprite.Group):
        super().__init__(group)
        self.screen = pygame.display.get_surface()
        self.font = font

        self.background = pygame.Surface((size[0] - 3, size[1] - 3), pygame.SRCALPHA).convert_alpha()
        self.background.fill("White")
        self.background_rect = self.background.get_frect(topleft = pos)

        self.foreground = pygame.Surface((size[0] - 5, size[1] - 5)).convert_alpha()
        self.foreground.fill("Black")
        self.foreground_rect = self.foreground.get_frect(center = self.background_rect.center)
    
        self.font_surface = self.font.render(text, True, "White").convert_alpha()
        self.font_rect = self.font_surface.get_frect(center = self.background_rect.center)

    def draw(self):
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.foreground, self.foreground_rect)
        self.screen.blit(self.font_surface, self.font_rect)

class NumberSlot(BaseGUI):
    def __init__(self, text: str, pos: tuple, font: pygame.font.Font, group: pygame.sprite.Group):
        super().__init__(text, pos, (50, 50), font, group)

class Output(BaseGUI):
    def __init__(self, pos, font, group):
        super().__init__("", pos, (200, 100), font, group)

class NumPad:
    def __init__(self, font: pygame.font.Font):
        self.screen = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()
        self.font = font
        self.generate_pad()

    def generate_pad(self):
        org_x = (self.screen.get_width() // 2 - 100)
        x = org_x
        y = self.screen.get_height() // 2 - 100

        # Output
        self.output = Output((x, y - 100), self.font, self.sprites)

        for i, sign in enumerate(
            ["←", "C", "%", "÷", 
             "7", "8", "9", "×",
             "4", "5", "6", "-", 
             "1", "2", "3", "+", 
             "±", "0", ".", "="
            ], 1):
            NumberSlot(sign, (x, y), self.font, self.sprites)
            x += 50
            if i % 4 == 0:
                x = org_x
                y += 50

    def get_sprites(self) -> pygame.sprite.Group:
        return self.sprites

    def draw(self):
        for sprite in self.sprites:
            sprite.draw()