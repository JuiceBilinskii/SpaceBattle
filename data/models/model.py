from abc import ABC, abstractmethod
from data.actions_capturer import ActionsCapturer


class Model(ABC):
    @abstractmethod
    def update(self, actions: ActionsCapturer):
        pass
