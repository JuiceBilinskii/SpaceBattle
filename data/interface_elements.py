from abc import ABC, abstractmethod


class InterfaceElement(ABC):
    @abstractmethod
    def execute(self):
        pass


class Button(InterfaceElement):
    def __init__(self, command):
        self.command = command
        self.__active = False

    def execute(self):
        return self.command.execute()

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, value: bool):
        self.__active = value
