from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, owner):
        self.__killed = False
        self.__owner = owner
        self.__health_points = None

    @property
    def is_killed(self):
        return self.__killed

    @is_killed.setter
    def is_killed(self, value: bool):
        self.__killed = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        self.__health_points = value


class Movable(Entity):
    def __init__(self, owner):
        super().__init__(owner)


class Ship(Movable):
    def __init__(self, owner):
        super().__init__(owner)


class Unmovable(Entity):
    def __init__(self, owner):
        super().__init__(owner)


class Obstacle(Unmovable):
    def __init__(self, owner):
        super().__init__(owner)
