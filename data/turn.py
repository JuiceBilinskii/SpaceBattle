from enum import Enum


class TurnStatus(Enum):
    Overview = 1
    Move = 2
    Attack = 3


class Turn:
    def __init__(self):
        self.player = None
