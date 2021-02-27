class Hexagon:
    def __init__(self, x, y):
        self.__entity = None
        self.__x = x
        self.__y = y
        # self.__directed = False
        # self.__selected = False

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, value):
        self.__entity = value

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
