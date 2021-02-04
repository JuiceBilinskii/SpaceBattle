from data.models.imodel import IModel, ActionsCapturer
from enum import Enum
from data.field import Field
from data.game_strategies import *
from data.player import *
from data.entities import *


class GameStatus(Enum):
    Active = 1
    Ended = 2


class Game(IModel):
    def __init__(self):
        self.level = 0

        self._strategies = {
            'select': SelectStrategy,
            'overview': OverviewStrategy,
            'move': MoveStrategy,
            'attack': AttackStrategy
        }
        self._strategy = self._strategies['select']

        self.players = [HumanPlayer(0), HumanPlayer(1)]
        self._current_turn = self.players[0]

        self.entities = {
            'ships': (Ship(self.players[0]),
                      Ship(self.players[0]),
                      Ship(self.players[0]),
                      Ship(self.players[1]),
                      Ship(self.players[1]),
                      Ship(self.players[1])),
            'obstacles': (Obstacle(None),
                          Obstacle(None),
                          Obstacle(None),
                          Obstacle(None),
                          Obstacle(None))
        }

        self.field = Field(9, 21, self.entities)

    @property
    def current_turn(self): return self._current_turn

    def _change_strategy(self, key):
        if key in self._strategies:
            self._strategy = self._strategies[key]
        else:
            self._strategy = None

    def update(self, actions: ActionsCapturer):
        key = None
        if actions.key_a:
            key = self._strategy.update_k_a(self)
        elif actions.key_left:
            key = self._strategy.update_k_left(self)
        elif actions.key_up:
            key = self._strategy.update_k_up(self)
        elif actions.key_right:
            key = self._strategy.update_k_right(self)
        elif actions.key_down:
            key = self._strategy.update_k_down(self)
        elif actions.key_escape:
            key = self._strategy.update_k_escape(self)
        elif actions.key_v:
            key = self._strategy.update_k_v(self)

        if key:
            self._change_strategy(key)
