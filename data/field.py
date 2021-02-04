from data.hexagon import Hexagon


class Field:
    def __init__(self, rows, cols, entities):
        self.__rows = rows
        self.__cols = cols
        self.__hexagons = []
        self.__init_hexagons()
        self.__init_entities(entities)
        # self.__hexagons[8][19].directed = True
        # self.__hexagons[4][14].selected = True
        self.directed_hexagon = (0, 0)
        self.selected_hexagon = None

    def __init_hexagons(self):
        for row in range(self.__rows):
            self.__hexagons.append([])
            for col in range(self.__cols - row % 2):
                self.__hexagons[row].append(Hexagon(row, col))

    def __init_entities(self, entities):
        self.__hexagons[0][0].entity = entities['ships'][0]
        self.__hexagons[3][2].entity = entities['ships'][1]
        self.__hexagons[6][3].entity = entities['ships'][2]
        self.__hexagons[6][5].entity = entities['ships'][3]
        self.__hexagons[7][3].entity = entities['obstacles'][0]

    @property
    def rows(self): return self.__rows

    @property
    def cols(self): return self.__cols

    @property
    def hexagons(self): return self.__hexagons
