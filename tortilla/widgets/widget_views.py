from tortilla.constants import *
from tortilla.text_objects import TextObjects, DrawCircle
from tortilla.widgets.widget_models import *


class WidgetView:
    def draw(self, screen: pygame.Surface, model_button: WidgetModel):
        pass


class ButtonView(WidgetView):
    def __init__(self, text, x, y, w, h, inactive_colour=PURPLE, active_colour=LIGHT_PURPLE, text_colour=WHITE):
        self._rect = pygame.Rect(x, y, w, h)
        self._inactive_colour = inactive_colour
        self._active_colour = active_colour
        self._text = text

        self._text_surf, self._text_rect = TextObjects.execute(self._text, SMALL_TEXT, colour=text_colour)
        self._text_rect.center = (round(self._rect.x + self._rect.w / 2), round(self._rect.y + self._rect.h / 2))

    def draw(self, screen: pygame.Surface, model_button: Button):
        if model_button.active:
            pygame.draw.rect(screen, self._active_colour, self._rect)
        else:
            pygame.draw.rect(screen, self._inactive_colour, self._rect)

        # text_surf, text_rect = text_objects(self._text, SMALL_TEXT, colour=self._text_colour)
        # text_rect.center = (round(self._rect.x + self._rect.w / 2), round(self._rect.y + self._rect.h / 2))
        screen.blit(self._text_surf, self._text_rect)


class ToggleButtonView(WidgetView):
    def __init__(self, text, x, y, w, h, inactive_colour=WHITE, active_colour=LIGHT_PURPLE, text_colour=WHITE,
                 enabled_colour=LIGHT_PURPLE, disabled_colour=GREY):
        self._rect = pygame.Rect(x, y, w, h)
        self._inactive_colour = inactive_colour
        self._active_colour = active_colour
        self._enabled_colour = enabled_colour
        self._disabled_colour = disabled_colour
        self._text = text

        self._toggle_w = round(w * 0.1)
        self._toggle_h = round(h * 0.5)
        self._toggle_rect = pygame.Rect(round(x + w - self._toggle_w - self._toggle_h / 2),
                                        round(y + (h - self._toggle_h) / 2),
                                        self._toggle_w,
                                        self._toggle_h)

        self._text_surf, self._text_rect = TextObjects.execute(self._text, SMALL_TEXT, colour=text_colour)
        self._text_rect.center = (round(self._rect.x + self._rect.w / 2), round(self._rect.y + self._rect.h / 2))
        self._text_rect.midleft = self._rect.midleft

    def draw(self, screen: pygame.Surface, model_button: ToggleButton):
        if model_button.active:
            pygame.draw.rect(screen, self._enabled_colour, self._rect)
        if model_button.enabled:
            pygame.draw.rect(screen, self._enabled_colour, self._toggle_rect)
            DrawCircle.execute(screen, round(self._toggle_rect.right), round(self._toggle_rect.centery),
                               self._toggle_h // 2,
                               self._enabled_colour)
            DrawCircle.execute(screen, round(self._toggle_rect.left), round(self._toggle_rect.centery),
                               self._toggle_h // 2,
                               self._enabled_colour)
            DrawCircle.execute(screen, round(self._toggle_rect.right), round(self._toggle_rect.centery),
                               round(self._toggle_h // 2 * 0.8), WHITE) # small inner circle
        else:
            pygame.draw.rect(screen, self._disabled_colour, self._toggle_rect)
            DrawCircle.execute(screen, round(self._toggle_rect.right), round(self._toggle_rect.centery),
                               self._toggle_h // 2,
                               self._disabled_colour)
            DrawCircle.execute(screen, round(self._toggle_rect.left), round(self._toggle_rect.centery),
                               self._toggle_h // 2,
                               self._disabled_colour)
            DrawCircle.execute(screen, round(self._toggle_rect.left), round(self._toggle_rect.centery),
                               round(self._toggle_h // 2 * 0.8), WHITE) # small inner circle

        # text_surf, text_rect = text_objects(self._text, SMALL_TEXT, colour=self._text_colour)
        # text_rect.midleft = self._rect.midleft
        screen.blit(self._text_surf, self._text_rect)
