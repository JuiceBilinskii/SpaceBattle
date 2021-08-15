import pygame
from tortilla.views.view import View
from tortilla.models.game import Game
from tortilla.hexagon import Hexagon
from tortilla.hexagon_points_calculator import HexagonPointsCalculator
from tortilla.sprites_library import SpritesLibrary
from tortilla.text_objects import TextObjects
from tortilla.constants import SMALL_TEXT, WHITE, BLACK, LIGHT_PURPLE, SCALE_FACTOR
from tortilla.entities import *


class GameView(View):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        self.field_img = self._extractor.extract_image('tortilla\\assets\\backgrounds\\field_bg.png', SCALE_FACTOR)
        self.hud_img = self._extractor.extract_image('tortilla\\assets\\backgrounds\\hud_bg.png', SCALE_FACTOR)
        self.overview_img = self._extractor.extract_image('tortilla\\assets\\backgrounds\\overview_bg.png', SCALE_FACTOR)

        self._field = FieldView(screen)
        self._hud = HudView(screen)
        self._overview = OverviewView(screen)

    def draw(self, model: Game):
        self._screen.blit(self.hud_img, (0, 0))
        self._screen.blit(self.field_img, (0, 36 * SCALE_FACTOR))
        self._screen.blit(self.overview_img, (1520 * SCALE_FACTOR, 36 * SCALE_FACTOR))

        self._field.draw(model)
        self._hud.draw(model)
        self._overview.draw(model)


class FieldView(View):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        w = 1520 * SCALE_FACTOR
        x = 0
        y = 36 * SCALE_FACTOR

        self._library = SpritesLibrary()

        self._hexagon_size = w / (29 * 3 ** 0.5)
        self._hexagons_offset = x + w / 29, y + 0.75 * 2 * w / (29 * 3 ** 0.5)

        self._hexagons_points = []
        self._init_hexagons_points()

    def _init_hexagons_points(self):
        for row in range(21):
            self._hexagons_points.append([])
            for col in range(28 - row % 2):
                q, r = col - row // 2, row
                hex_center, hex_corners = HexagonPointsCalculator.calculate_hex_points((q, r), self._hexagon_size, self._hexagons_offset)
                self._hexagons_points[row].append((hex_center, hex_corners))

    def _draw_hexagons_borders(self, rows, cols):
        for row in range(rows):
            for col in range(cols - row % 2):
                pygame.draw.lines(self._screen, (71, 26, 92), True, self._hexagons_points[row][col][1])

    def _draw_hexagons_statuses(self, highlighted_hexagons: dict):
        if highlighted_hexagons['reachable_hexagons']:
            for reachable_hexagon in highlighted_hexagons['reachable_hexagons']:
                if reachable_hexagon:
                    x, y = reachable_hexagon.coordinates
                    pygame.draw.polygon(self._screen, (0, 125, 125), self._hexagons_points[x][y][1])
        if highlighted_hexagons['directed_hexagon']:
            x, y = highlighted_hexagons['directed_hexagon'].coordinates
            pygame.draw.polygon(self._screen, (255, 255, 153), self._hexagons_points[x][y][1])
        if highlighted_hexagons['selected_hexagon']:
            x, y = highlighted_hexagons['selected_hexagon'].coordinates
            pygame.draw.polygon(self._screen, (204, 255, 153), self._hexagons_points[x][y][1])

    def _draw_entities(self, hexagons):
        for x, hexagon_row in enumerate(hexagons):
            for y, hexagon in enumerate(hexagon_row):
                if hexagon.entity:
                    entity_img = self._library.get_asset(hexagon.entity)
                    rect = entity_img.get_rect()
                    rect.center = self._hexagons_points[x][y][0]
                    self._screen.blit(entity_img, rect)

                    text_surf, text_rect = TextObjects.execute(str(hexagon.entity.health_points), SMALL_TEXT,
                                                               colour=WHITE)
                    text_rect = rect
                    self._screen.blit(text_surf, text_rect)

    def draw(self, model: Game):
        self._draw_hexagons_borders(model.field.rows, model.field.cols)
        self._draw_hexagons_statuses(model.field.highlighted_hexagons)
        self._draw_entities(model.field.hexagons)


class HudView(View):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

    def draw(self, model: Game):
        text_surf, text_rect = TextObjects.execute(str(model.field.directed_hexagon.coordinates), SMALL_TEXT, colour=WHITE)
        text_rect.midleft = (5, 18 * SCALE_FACTOR)
        self._screen.blit(text_surf, text_rect)


class OverviewView(View):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        self._x = 1520 * SCALE_FACTOR
        self._y = 36 * SCALE_FACTOR
        self._width = 400 * SCALE_FACTOR
        self._height = 1044 * SCALE_FACTOR
        self._players_rects = [
            pygame.Rect(self._x + 2 * SCALE_FACTOR, self._y + 54 * SCALE_FACTOR, 198 * SCALE_FACTOR, 198 * SCALE_FACTOR),
            pygame.Rect(self._x + 200 * SCALE_FACTOR, self._y + 54 * SCALE_FACTOR, 198 * SCALE_FACTOR, 198 * SCALE_FACTOR)
        ]
        self._mode_rects = [
            pygame.Rect(int(self._x + 0 * SCALE_FACTOR), int(self._y + 450 * SCALE_FACTOR), int(200 * SCALE_FACTOR),
                        int(40 * SCALE_FACTOR)),
            pygame.Rect(int(self._x + 200 * SCALE_FACTOR), int(self._y + 450 * SCALE_FACTOR), int(200 * SCALE_FACTOR),
                        int(40 * SCALE_FACTOR))
        ]

        self._library = SpritesLibrary()

    def draw(self, model: Game):
        # headers
        text_surf, text_rect = TextObjects.execute('Players', SMALL_TEXT, colour=WHITE)
        text_rect.center = (self._x + self._width // 2, self._y + 27 * SCALE_FACTOR)
        self._screen.blit(text_surf, text_rect)

        text_surf, text_rect = TextObjects.execute('Overview', SMALL_TEXT, colour=WHITE)
        text_rect.center = (self._x + self._width // 2, self._y + 517 * SCALE_FACTOR)
        self._screen.blit(text_surf, text_rect)

        # modes
        for mode_rect in self._mode_rects:
            pygame.draw.rect(self._screen, WHITE, mode_rect)

        text_surf, text_rect = TextObjects.execute('Move', SMALL_TEXT, colour=BLACK)
        text_rect.center = (self._x + 99 * SCALE_FACTOR, self._y + 470 * SCALE_FACTOR)
        self._screen.blit(text_surf, text_rect)
        text_surf, text_rect = TextObjects.execute('Attack', SMALL_TEXT, colour=BLACK)
        text_rect.center = (self._x + 299 * SCALE_FACTOR, self._y + 470 * SCALE_FACTOR)
        self._screen.blit(text_surf, text_rect)

        # players
        pygame.draw.rect(self._screen, LIGHT_PURPLE, self._players_rects[model.current_player.player_id])

        # selected entity
        if model.field.selected_hexagon:
            entity = model.field.selected_hexagon.entity
            entity_img = self._library.get_asset(entity)
            rect = entity_img.get_rect()
            rect.center = (self._x + self._width // 2, self._y + 604 * SCALE_FACTOR)
            self._screen.blit(entity_img, rect)

            health_points = str(entity.health_points)
            text_surf, text_rect = TextObjects.execute('Health points: ' + health_points, SMALL_TEXT, colour=WHITE)
            text_rect.midleft = (self._x + 10 * SCALE_FACTOR, self._y + 670 * SCALE_FACTOR)
            self._screen.blit(text_surf, text_rect)

            if issubclass(type(entity), Movable):
                health_points = str(entity.move_points)
                text_surf, text_rect = TextObjects.execute('Move points: ' + health_points, SMALL_TEXT, colour=WHITE)
                text_rect.midleft = (self._x + 10 * SCALE_FACTOR, self._y + 700 * SCALE_FACTOR)
                self._screen.blit(text_surf, text_rect)
