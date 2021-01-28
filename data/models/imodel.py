from abc import ABC, abstractmethod
from data.actions_capturer import ActionsCapturer


class IModel(ABC):
    @abstractmethod
    def update(self, actions: ActionsCapturer):
        pass
