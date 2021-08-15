import pygame
from tortilla.views.view import View
from tortilla.models.settings_menu import SettingsMenu
from tortilla.widgets.widget_views import ButtonView, ToggleButtonView
from tortilla.text_objects import TextObjects
from tortilla.constants import *


class SettingsMenuView(View):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        self.background_img = self._extractor.extract_image('tortilla\\assets\\backgrounds\\settings_menu_bg.png', SCALE_FACTOR)
        self.pixel_position = 0, 0

        self._label, self._label_rect = TextObjects.execute('Settings menu', LARGE_TEXT, colour=WHITE)
        self._label_rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 14

        self.__init_buttons()

    def __init_buttons(self):
        button_width = round(SCREEN_WIDTH * 2 // 13)
        button_height = round(SCREEN_HEIGHT * 5 // 81)

        button_x_start = (SCREEN_WIDTH - button_width) // 2
        button_y_start = (SCREEN_HEIGHT - button_height) * 13 // 14

        buttons_layout = [
            (button_x_start, (SCREEN_HEIGHT - button_height) * 7 // 14, button_width, button_height),
            (button_x_start, (SCREEN_HEIGHT - button_height) * 12 // 14, button_width, button_height),
            (button_x_start, (SCREEN_HEIGHT - button_height) * 13 // 14, button_width, button_height)
        ]

        self._buttons_layout = [
            ToggleButtonView('Full screen', *buttons_layout[0]),
            ButtonView('Accept changes', *buttons_layout[1], inactive_colour=WHITE, text_colour=BLACK),
            ButtonView('Main menu', *buttons_layout[2], inactive_colour=WHITE, text_colour=BLACK)
        ]

    def draw(self, model: SettingsMenu):
        self._screen.blit(self.background_img, self.pixel_position)
        self._screen.blit(self._label, self._label_rect)

        for i, button in enumerate(self._buttons_layout):
            button.draw(self._screen, model.buttons[i])
