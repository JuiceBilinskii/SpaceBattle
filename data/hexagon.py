class Hexagon:
    def __init__(self, x, y, container=None):
        if container is None:
            container = []
        self.container = container
        self.x = x
        self.y = y