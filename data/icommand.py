from abc import ABC, abstractmethod


class ICommand(ABC):
    @staticmethod
    def execute():
        pass
