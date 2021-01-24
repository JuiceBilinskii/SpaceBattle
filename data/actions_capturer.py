class ActionsCapturer:
    def __init__(self):
        self.__key_a = False

    def to_default(self):
        self.__key_a = False

    @property
    def key_a(self):
        return self.__key_a

    @key_a.setter
    def key_a(self, value: bool):
        self.__key_a = value
