import pygame
from enum import Enum
from data.contexts import MainMenu
from data.views.main_menu_view import MainMenuView
from data.contexts import Game
from data.views.game_view import GameView
from data.actions_capturer import ActionsCapturer


class ProgramStatus(Enum):
    MainMenu = 1
    SettingsMenu = 2
    Game = 3


class Controller:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        self.model = MainMenu()
        self.view = MainMenuView(self.screen)

    def main_menu(self):
        self.model = MainMenu()
        self.view = MainMenuView(self.screen)

    def game(self):
        self.model = Game()
        self.view = GameView(self.screen)

    def change_mv(self, command: str):
        if command == 'main_menu':
            self.main_menu()
        elif command == 'game':
            self.game()

    def update_model(self, actions: ActionsCapturer):
        result = self.model.update(actions)
        if result:
            self.change_mv(result)
        if result == 'quit':
            return result

    def update_view(self):
        self.view.draw(self.model)
