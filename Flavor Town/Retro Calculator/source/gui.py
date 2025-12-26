from .settings import *

class BaseGUI(pygame.sprite.Sprite):
    def __init__(self, text: str, pos: tuple, size: tuple, font: pygame.font.Font, output_font: pygame.font.Font, group: pygame.sprite.Group):
        super().__init__(group)
        self.screen = pygame.display.get_surface()
        self.font = font
        self.output_font = output_font

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
    def __init__(self, text: str, id: str, pos: tuple, font: pygame.font.Font, output_font: pygame.font.Font, group: pygame.sprite.Group):
        super().__init__(text, pos, (50, 50), font, output_font, group)
        self.id = id

class Output(BaseGUI):
    def __init__(self, pos: tuple, font: pygame.font.Font, output_font: pygame.font.Font, group):
        super().__init__("", pos, (200, 100), font, output_font, group)

        self.equation_screen = pygame.Surface(self.foreground_rect.size, pygame.SRCALPHA)
        self.equation_screen_rect = self.foreground_rect.copy()
        self.text_color = "White"

    def reset(self, text: str) -> None:
        self.equation_screen.fill((0, 0, 0, 0))

        text_surf = self.output_font.render(text, True, self.text_color)
        text_width = text_surf.get_width()
        view_width = self.equation_screen.get_width()

        if text_width > view_width:
            offset_x = (text_width - view_width) - 5
        else:
            offset_x = -5

        y = 0

        self.equation_screen.blit(text_surf, (-offset_x, y))

    def draw(self):
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.foreground, self.foreground_rect)
        self.screen.blit(self.equation_screen, self.equation_screen_rect)

class NumPad:
    def __init__(self, font: pygame.font.Font, output_font: pygame.font.Font):
        self.screen = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()
        self.number_slots = pygame.sprite.Group()
        self.font = font
        self.output_font = output_font
        self.generate_pad()

    def generate_pad(self):
        org_x = (self.screen.get_width() // 2 - 100)
        x = org_x
        y = self.screen.get_height() // 2 - 100

        # Output
        self.output = Output((x, y - 100), self.font, self.output_font, self.sprites)

        for i, sign in enumerate(
            ["←", "C", "%", "÷", 
             "7", "8", "9", "×",
             "4", "5", "6", "-", 
             "1", "2", "3", "+", 
             "±", "0", ".", "="
            ], 1):
            if sign in ["←", "C", "±"]:
                if sign == "←":
                    NumberSlot(sign, "DEL", (x, y), self.font, self.output_font, (self.sprites, self.number_slots))
                
                elif sign == "C":
                    NumberSlot(sign, "CLEAR", (x, y), self.font, self.output_font, (self.sprites, self.number_slots))
                
                elif sign == "±":
                    NumberSlot(sign, "POSNEG", (x, y), self.font, self.output_font, (self.sprites, self.number_slots))
            
            else:
                NumberSlot(sign, sign, (x, y), self.font, self.output_font, (self.sprites, self.number_slots))
            
            x += 50
            if i % 4 == 0:
                x = org_x
                y += 50

    def get_sprites(self) -> pygame.sprite.Group:
        return self.sprites

    def get_number_slots(self) -> pygame.sprite.Group:
        return self.number_slots

    def reset_output(self, text: str):
        self.output.reset(text)

    def draw(self):
        for sprite in self.sprites:
            sprite.draw()