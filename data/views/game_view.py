import pygame
from data.views.iview import IView
from data.models.game import Game


class GameView(IView):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        self.field_img = self.extracter.extract_image('assets\\backgrounds\\field_bg.png', self.scale_factor)
        self.hud_img = self.extracter.extract_image('assets\\backgrounds\\hud_bg.png', self.scale_factor)
        self.overview_img = self.extracter.extract_image('assets\\backgrounds\\overview_bg.png', self.scale_factor)

    def draw(self, model: Game):
        self.screen.blit(self.hud_img, (0, 0))
        self.screen.blit(self.field_img, (0, 36 * self.scale_factor))
        self.screen.blit(self.overview_img, (1520 * self.scale_factor, 36 * self.scale_factor))
