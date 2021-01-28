from data.views.iview import IView
from data.visual_element import VisualButton
from data.models.main_menu import MainMenu
from data.constants import *


class MainMenuView(IView):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        self.background_img = self.extracter.extract_image('assets\\backgrounds\\main_menu_bg.png', self.scale_factor)
        self.pixel_position = 0, 0

        self.__init_buttons()

    def __init_buttons(self):
        button_width = round(SCREEN_WIDTH * 2 // 13)
        button_height = round(SCREEN_HEIGHT * 5 // 81)

        button_x_start = (SCREEN_WIDTH - button_width) // 2
        button_y_start = (SCREEN_HEIGHT - button_height) * 13 // 14

        buttons_layout = [(SCREEN_WIDTH * 1 // 13, button_y_start, button_width, button_height),
                          (SCREEN_WIDTH * 4 // 13, button_y_start, button_width, button_height),
                          (SCREEN_WIDTH * 7 // 13, button_y_start, button_width, button_height),
                          (SCREEN_WIDTH * 10 // 13, button_y_start, button_width, button_height)]

        self.__buttons = [
            VisualButton('Start game', *buttons_layout[0]),
            VisualButton('Settings', *buttons_layout[1]),
            VisualButton('Score', *buttons_layout[2]),
            VisualButton('Quit', *buttons_layout[3])
        ]

    def draw(self, model: MainMenu):
        self.screen.blit(self.background_img, self.pixel_position)
        # pygame.draw.rect(self.screen, (0, 0, 0), (200, 200, 400, 400))

        for i in range(len(self.__buttons)):
            self.__buttons[i].draw(self.screen, model.buttons[i])
