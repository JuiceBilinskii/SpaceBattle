from abc import ABC


class Player(ABC):
    def __init__(self, human_player: bool, player_id: int):
        self.__human_player = human_player
        self._player_id = player_id

    @property
    def is_human_player(self):
        return self.__human_player

    @property
    def player_id(self):
        return self._player_id


class HumanPlayer(Player):
    def __init__(self, player_id: int):
        super().__init__(True, player_id)


class ComputerPlayer(Player):
    def __init__(self, player_id: int):
        super().__init__(False, player_id)
