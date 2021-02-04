import pygame
from data.views.iview import IView, constants


class SettingsMenuView(IView):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        self.background_img = self.extractor.extract_image('assets\\backgrounds\\main_menu_bg.png', constants.SCALE_FACTOR)
        self.pixel_position = 0, 0

    def draw(self):
        self.screen.blit(self.background_img, self.pixel_position)
