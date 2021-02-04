from data.actions_capturer import ActionsCapturer
from data.game_strategies import *
from data.models.game import Game
from data.models.main_menu import MainMenu


class GameContext:
    def __init__(self):
        self.__strategy = SelectStrategy()

        self.__model = Game()

    @property
    def model(self):
        return self.__model

    @property
    def strategy(self):
        """
        The Context maintains a reference to one of the Strategy entities. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: str) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = self.__strategies[strategy]

    def update(self, actions: ActionsCapturer):
        if actions.key_a:
            self.__strategy.update_k_a(self.__model)
        elif actions.key_left:
            self.__strategy.update_k_left(self.__model)
        elif actions.key_up:
            self.__strategy.update_k_up(self.__model)
        elif actions.key_right:
            self.__strategy.update_k_right(self.__model)
        elif actions.key_down:
            self.__strategy.update_k_down(self.__model)
