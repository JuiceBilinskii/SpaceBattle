from data.models.imodel import IModel, ActionsCapturer
from enum import Enum


class GameStatus(Enum):
    Active = 1
    Ended = 2


class Game(IModel):
    def __init__(self):
        self.level = 0

        self.field = 0

        self.players = []
        self.current_turn = None

    def update(self, actions: ActionsCapturer):
        pass

