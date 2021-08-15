from data.views.view import View
from data.widgets.widget_views import ButtonView
from data.models.main_menu import MainMenu
from data.constants import *


class MainMenuView(View):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        self.background_img = self._extractor.extract_image('data\\assets\\backgrounds\\main_menu_bg.png', SCALE_FACTOR)
        self.pixel_position = 0, 0

        self._init_buttons()

    def _init_buttons(self):
        button_width = round(SCREEN_WIDTH * 2 // 13)
        button_height = round(SCREEN_HEIGHT * 5 // 81)

        button_x_start = (SCREEN_WIDTH - button_width) // 2
        button_y_start = (SCREEN_HEIGHT - button_height) * 13 // 14

        buttons_layout = [(SCREEN_WIDTH * 1 // 13, button_y_start, button_width, button_height),
                          (SCREEN_WIDTH * 4 // 13, button_y_start, button_width, button_height),
                          (SCREEN_WIDTH * 7 // 13, button_y_start, button_width, button_height),
                          (SCREEN_WIDTH * 10 // 13, button_y_start, button_width, button_height)]

        self._buttons_layout = [
            ButtonView('Start game', *buttons_layout[0]),
            ButtonView('Settings', *buttons_layout[1]),
            ButtonView('Score', *buttons_layout[2]),
            ButtonView('Quit', *buttons_layout[3])
        ]

    def draw(self, model: MainMenu):
        self._screen.blit(self.background_img, self.pixel_position)
        # pygame.draw.rect(self.screen, (0, 0, 0), (200, 200, 400, 400))

        for i, button in enumerate(self._buttons_layout):
            button.draw(self._screen, model.buttons[i])
