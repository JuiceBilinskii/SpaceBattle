from data.move import Move


class Strategy:
    @staticmethod
    def update_k_left(model):
        pass

    @staticmethod
    def update_k_up(model):
        pass

    @staticmethod
    def update_k_right(model):
        pass

    @staticmethod
    def update_k_down(model):
        pass

    @staticmethod
    def update_k_a(model):
        pass

    @staticmethod
    def update_k_escape(model):
        pass

    @staticmethod
    def update_k_v(model):
        pass


class SelectStrategy(Strategy):
    @staticmethod
    def update_k_left(model):
        x, y = model.field.directed_hexagon
        if y - 1 >= 0:
            model.field.directed_hexagon = x, y - 1
        return 'select'

    @staticmethod
    def update_k_up(model):
        x, y = model.field.directed_hexagon
        if x - 1 >= 0:
            if y == model.field.cols - 1:
                model.field.directed_hexagon = x - 1, y - 1
            else:
                model.field.directed_hexagon = x - 1, y
        return 'select'

    @staticmethod
    def update_k_right(model):
        x, y = model.field.directed_hexagon
        if y + 1 <= model.field.cols - 1 and not (y + 1 == model.field.cols - 1 and x % 2 == 1):
            model.field.directed_hexagon = x, y + 1
        return 'select'

    @staticmethod
    def update_k_down(model):
        x, y = model.field.directed_hexagon
        if x + 1 <= model.field.rows - 1:
            if y == model.field.cols - 1:
                model.field.directed_hexagon = x + 1, y - 1
            else:
                model.field.directed_hexagon = x + 1, y
        return 'select'

    @staticmethod
    def update_k_a(model):
        if model.field.hexagons[model.field.directed_hexagon[0]][model.field.directed_hexagon[1]].entity:
            entity = model.field.hexagons[model.field.directed_hexagon[0]][model.field.directed_hexagon[1]].entity
            model.field.selected_hexagon = model.field.directed_hexagon
            if entity.owner is model.current_turn:
                return 'move'
            else:
                return 'overview'
        return 'select'

    @staticmethod
    def update_k_escape(model):
        return 'select'

    @staticmethod
    def update_k_v(model):
        return 'select'


class MoveStrategy(Strategy):
    @staticmethod
    def update_k_left(model):
        x, y = model.field.directed_hexagon
        if y - 1 >= 0:
            model.field.directed_hexagon = x, y - 1
        return 'move'

    @staticmethod
    def update_k_up(model):
        x, y = model.field.directed_hexagon
        if x - 1 >= 0:
            if y == model.field.cols - 1:
                model.field.directed_hexagon = x - 1, y - 1
            else:
                model.field.directed_hexagon = x - 1, y
        return 'move'

    @staticmethod
    def update_k_right(model):
        x, y = model.field.directed_hexagon
        if y + 1 <= model.field.cols - 1 and not (y + 1 == model.field.cols - 1 and x % 2 == 1):
            model.field.directed_hexagon = x, y + 1
        return 'move'

    @staticmethod
    def update_k_down(model):
        x, y = model.field.directed_hexagon
        if x + 1 <= model.field.rows - 1:
            if y == model.field.cols - 1:
                model.field.directed_hexagon = x + 1, y - 1
            else:
                model.field.directed_hexagon = x + 1, y
        return 'move'

    @staticmethod
    def update_k_a(model):
        if Move(model.field.hexagons[model.field.selected_hexagon[0]][model.field.selected_hexagon[1]], model.field.hexagons[model.field.directed_hexagon[0]][model.field.directed_hexagon[1]]).execute_move():
            model.field.selected_hexagon = None
            return 'select'
        else:
            return 'move'

    @staticmethod
    def update_k_escape(model):
        model.field.selected_hexagon = None
        return 'select'

    @staticmethod
    def update_k_v(model):
        return 'attack'


class AttackStrategy(Strategy):
    @staticmethod
    def update_k_left(model):
        x, y = model.field.directed_hexagon
        if y - 1 >= 0:
            model.field.directed_hexagon = x, y - 1
        return 'attack'

    @staticmethod
    def update_k_up(model):
        x, y = model.field.directed_hexagon
        if x - 1 >= 0:
            if y == model.field.cols - 1:
                model.field.directed_hexagon = x - 1, y - 1
            else:
                model.field.directed_hexagon = x - 1, y
        return 'attack'

    @staticmethod
    def update_k_right(model):
        x, y = model.field.directed_hexagon
        if y + 1 <= model.field.cols - 1 and not (y + 1 == model.field.cols - 1 and x % 2 == 1):
            model.field.directed_hexagon = x, y + 1
        return 'attack'

    @staticmethod
    def update_k_down(model):
        x, y = model.field.directed_hexagon
        if x + 1 <= model.field.rows - 1:
            if y == model.field.cols - 1:
                model.field.directed_hexagon = x + 1, y - 1
            else:
                model.field.directed_hexagon = x + 1, y
        return 'attack'

    def update_k_a(self):
        return 'attack'

    @staticmethod
    def update_k_escape(model):
        model.field.selected_hexagon = None
        return 'select'

    @staticmethod
    def update_k_v(model):
        return 'move'


class OverviewStrategy(Strategy):
    @staticmethod
    def update_k_left(self):
        return 'overview'

    @staticmethod
    def update_k_up(self):
        return 'overview'

    @staticmethod
    def update_k_right(self):
        return 'overview'

    @staticmethod
    def update_k_down(self):
        return 'overview'

    @staticmethod
    def update_k_a(self):
        return 'overview'

    @staticmethod
    def update_k_escape(model):
        model.field.selected_hexagon = None
        return 'select'

    @staticmethod
    def update_k_v(model):
        return 'overview'
