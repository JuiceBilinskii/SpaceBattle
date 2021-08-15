import pygame
from enum import Enum
from data.models.main_menu import MainMenu
from data.views.main_menu_view import MainMenuView
from data.models.game import Game
from data.views.game_view import GameView
from data.models.settings_menu import SettingsMenu
from data.views.settings_menu_view import SettingsMenuView
from data.actions_capturer import ActionsCapturer


class ProgramStatus(Enum):
    MainMenu = 1
    SettingsMenu = 2
    Game = 3


class Controller:

    def __init__(self, screen: pygame.Surface):
        self._screen = screen

        self._model = MainMenu()
        self._view = MainMenuView(self._screen)

    def _change_model_view(self, command: str):
        if command == 'main_menu':
            self._model = MainMenu()
            self._view = MainMenuView(self._screen)
        elif command == 'game':
            self._model = Game()
            self._view = GameView(self._screen)
        elif command == 'settings_menu':
            self._model = SettingsMenu()
            self._view = SettingsMenuView(self._screen)
        elif command == 'score_menu':
            pass

    def update_model(self, actions: ActionsCapturer):
        result = self._model.update(actions)
        if result == 'quit':
            return result
        if result:
            self._change_model_view(result)

    def update_view(self):
        self._view.draw(self._model)
