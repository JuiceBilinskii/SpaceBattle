import pygame
from data.views.iview import IView


class SettingsMenuView(IView):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        self.background_img = self.extracter.extract_image('assets\\backgrounds\\main_menu_bg.png', self.scale_factor)
        self.pixel_position = 0, 0

    def draw(self):
        self.screen.blit(self.background_img, self.pixel_position)
