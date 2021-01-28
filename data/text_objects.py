from data.constants import *


class TextObjects:
    @staticmethod
    def execute(text, font: pygame.font, colour=BLACK) -> (pygame.Surface, pygame.Rect):
        text_surface = font.render(text, True, colour)
        return text_surface, text_surface.get_rect()
