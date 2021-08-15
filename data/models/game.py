from data.models.model import Model, ActionsCapturer
from enum import Enum
from data.field import Field
from data.game_strategies import *
from data.player import *
from data.entities import *


class GameStatus(Enum):
    Active = 1
    Ended = 2


class Game(Model):
    def __init__(self):
        self._status = GameStatus.Active

        self._strategies = {
            'select': SelectStrategy,
            'overview': OverviewStrategy,
            'move': MoveStrategy,
            'attack': AttackStrategy
        }
        self._strategy = self._strategies['select']

        self._players = [Player(0, 'Uga Buga'), Player(1, 'Gringo')]
        self._current_player: Player = self._players[0]

        #self._entities = {
        #    'ships': ((Ship(self._players[0]), (1, 0)),
        #              (Ship(self._players[0]), (3, 2)),
        #              (Ship(self._players[0]), (6, 3)),
        #              (Ship(self._players[1]), (6, 5)),
        #              (Ship(self._players[1]), (2, 2)),
        #              (Ship(self._players[1]), (7, 8))),
        #    'obstacles': ((Obstacle(None), (7, 3)),
        #                  (Obstacle(None), (5, 3)),
        #                  (Obstacle(None), (5, 4)),
        #                  (Obstacle(None), (5, 5)),
        #                  (Obstacle(None), (5, 6)))
        #}

        self._ships = {
            'player_1': [
                (Ship(self._players[0]), (1, 0)),
                (Ship(self._players[0]), (3, 2)),
                (Ship(self._players[0]), (6, 3))
            ],
            'player_2': [
                (Ship(self._players[1]), (6, 5)),
                (Ship(self._players[1]), (2, 2)),
                (Ship(self._players[1]), (7, 8))
            ]
        }

        self._entities = (
            *self._ships['player_1'],
            *self._ships['player_2'],
            (Obstacle(None), (7, 3)),
            (Obstacle(None), (5, 3)),
            (Obstacle(None), (5, 4)),
            (Obstacle(None), (5, 5)),
            (Obstacle(None), (5, 6))
        )

        self.field = Field(9, 21, self._entities)

    @property
    def current_player(self): return self._current_player

    @property
    def players(self): return self._players

    @property
    def status(self): return self._status

    def _update_status(self):
        for player, ships in self._ships.items():
            for ship, coordinates in ships:
                if not ship.is_killed:
                    break
            else:
                self._status = GameStatus.Ended
                break

    def _change_strategy(self, key):
        if key in self._strategies:
            self._strategy = self._strategies[key]
        else:
            self._strategy = None

    def set_next_turn(self):
        self._current_player = self._players[(self._current_player.player_id + 1) % len(self._players)]
        for entity, coordinates in self._entities:
            if entity.owner is self._current_player:
                entity.set_default()

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
        elif actions.key_space:
            key = self._strategy.update_k_space(self)

        if key:
            self._change_strategy(key)

        self._update_status()
        if self._status == GameStatus.Ended:
            return 'main_menu'
