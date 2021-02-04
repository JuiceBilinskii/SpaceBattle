from data.constants import *
from data.text_objects import TextObjects
from data.widgets.interface_elements import Button


class VisualButton:
    def __init__(self, text, x, y, w, h, inactive_colour=PURPLE, active_colour=LIGHT_PURPLE, text_colour=WHITE):
        self.__rect = pygame.Rect(x, y, w, h)
        self.__inactive_colour = inactive_colour
        self.__active_colour = active_colour
        self.__text = text

        self._text_surf, self._text_rect = TextObjects.execute(self.__text, SMALL_TEXT, colour=text_colour)
        self._text_rect.center = (round(self.__rect.x + self.__rect.w / 2), round(self.__rect.y + self.__rect.h / 2))

    def draw(self, screen: pygame.Surface, model_button: Button):
        if model_button.active:
            pygame.draw.rect(screen, self.__active_colour, self.__rect)
        else:
            pygame.draw.rect(screen, self.__inactive_colour, self.__rect)

        # text_surf, text_rect = text_objects(self._text, SMALL_TEXT, colour=self._text_colour)
        # text_rect.center = (round(self._rect.x + self._rect.w / 2), round(self._rect.y + self._rect.h / 2))
        screen.blit(self._text_surf, self._text_rect)
