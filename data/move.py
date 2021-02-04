from data.hexagon import Hexagon


class Move:
    def __init__(self, start_hexagon: Hexagon, end_hexagon: Hexagon):
        self._start_hexagon = start_hexagon
        self._end_hexagon = end_hexagon

    def execute_move(self):
        if not self._end_hexagon.entity:
            self._end_hexagon.entity = self._start_hexagon.entity
            self._start_hexagon.entity = None
            return True
        return False
