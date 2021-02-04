import pygame
from data.views.iview import IView, constants
from data.models.game import Game
from data.hexagon_points_calculator import HexagonPointsCalculator
from data.sprites_library import SpritesLibrary
from data.constants import SCREEN_WIDTH


class GameView(IView):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        self.field_img = self.extractor.extract_image('assets\\backgrounds\\field_bg.png', constants.SCALE_FACTOR)
        self.hud_img = self.extractor.extract_image('assets\\backgrounds\\hud_bg.png', constants.SCALE_FACTOR)
        self.overview_img = self.extractor.extract_image('assets\\backgrounds\\overview_bg.png', constants.SCALE_FACTOR)

        self.__field = FieldView(screen)
        self.__hud = HudView(screen)
        self.__overview = OverviewView(screen)

    def draw(self, model: Game):
        self.screen.blit(self.hud_img, (0, 0))
        self.screen.blit(self.field_img, (0, 36 * constants.SCALE_FACTOR))
        self.screen.blit(self.overview_img, (1520 * constants.SCALE_FACTOR, 36 * constants.SCALE_FACTOR))

        self.__field.draw(model)


class FieldView(IView):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        w = 1520 * constants.SCALE_FACTOR
        x = 0
        y = 36 * constants.SCALE_FACTOR

        self.library = SpritesLibrary()

        self.__hexagon_size = w / (29 * 3 ** 0.5)
        self.__hexagons_offset = x + w / 29, y + 0.75 * 2 * w / (29 * 3 ** 0.5)

        self.__hexagons_points = []
        self.__init_hexagons_points()

    def __init_hexagons_points(self):
        for row in range(21):
            self.__hexagons_points.append([])
            for col in range(28 - row % 2):
                q, r = col - row // 2, row
                hex_center, hex_corners = HexagonPointsCalculator.calculate_hex_points((q, r), self.__hexagon_size, self.__hexagons_offset)
                self.__hexagons_points[row].append((hex_center, hex_corners))

    def __draw_hexagons_borders(self, rows, cols):
        for row in range(rows):
            for col in range(cols - row % 2):
                # pygame.draw.lines(self.screen, (71, 26, 92), True, self.__hexagons_points[row][col][1])
                pygame.draw.lines(self.screen, (71, 26, 92), True, self.__hexagons_points[row][col][1])

    def __draw_hexagons_statuses(self, directed_hexagon: (int, int), selected_hexagon: (int, int)):
        # for row in hexagons:
        #    for col in row:
        #        if col.directed:
        #            pygame.draw.polygon(self.screen, (255, 255, 153), self.__hexagons_points[col.x][col.y][1])
        #        elif col.selected:
        #            pygame.draw.polygon(self.screen, (204, 255, 153), self.__hexagons_points[col.x][col.y][1])
        if directed_hexagon:
            pygame.draw.polygon(self.screen, (255, 255, 153), self.__hexagons_points[directed_hexagon[0]][directed_hexagon[1]][1])
        if selected_hexagon:
            pygame.draw.polygon(self.screen, (204, 255, 153), self.__hexagons_points[selected_hexagon[0]][selected_hexagon[1]][1])

    def __draw_entities(self, hexagons):
        pass
        for row in hexagons:
            for hexagon in row:
                if hexagon.entity:
                    entity_img = self.library.get_asset(hexagon.entity)
                    rect = entity_img.get_rect()
                    rect.center = self.__hexagons_points[hexagon.x][hexagon.y][0]
                    self.screen.blit(entity_img, rect)

    def draw(self, model: Game):
        self.__draw_hexagons_borders(model.field.rows, model.field.cols)
        self.__draw_hexagons_statuses(model.field.directed_hexagon, model.field.selected_hexagon)
        self.__draw_entities(model.field.hexagons)


class HudView(IView):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

    def draw(self, model: Game):
        pass


class OverviewView(IView):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

    def draw(self, model: Game):
        pass
