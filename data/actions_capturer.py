class ActionsCapturer:
    def __init__(self):
        self.__key_a = False
        self.__key_left = False
        self.__key_right = False

    def to_default(self):
        self.__key_a = False
        self.__key_left = False
        self.__key_right = False

    @property
    def key_a(self):
        return self.__key_a

    @key_a.setter
    def key_a(self, value: bool):
        self.__key_a = value

    @property
    def key_left(self):
        return self.__key_left

    @key_left.setter
    def key_left(self, value: bool):
        self.__key_left = value

    @property
    def key_right(self):
        return self.__key_right

    @key_right.setter
    def key_right(self, value: bool):
        self.__key_right = value
