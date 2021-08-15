import json
import unittest

from tortilla.actions_capturer import ActionsCapturer
from tortilla.entities import *
from tortilla.field import Field
from tortilla.hexagon import Hexagon
from tortilla.models.game import Game, GameStatus
from tortilla.models.main_menu import MainMenu
from tortilla.models.settings_menu import SettingsMenu
from tortilla.game_strategies import *
from tortilla.player import Player
from tortilla.widgets.widget_models import *
from tortilla.sprites_library import SpritesLibrary


class MainMenuTest(unittest.TestCase):
    def test_start_game(self):
        actions = ActionsCapturer()

        model = MainMenu()

        actions.key_a = True
        self.assertEqual(model.update(actions), 'game')

    def test_open_settings(self):
        actions = ActionsCapturer()

        model = MainMenu()

        actions.key_right = True
        model.update(actions)
        actions.to_default()

        actions.key_a = True
        self.assertEqual(model.update(actions), 'settings_menu')

    def test_open_scores(self):
        actions = ActionsCapturer()

        model = MainMenu()

        actions.key_right = True
        model.update(actions)
        actions.to_default()

        actions.key_right = True
        model.update(actions)
        actions.to_default()

        actions.key_a = True
        self.assertEqual(model.update(actions), 'score_menu')

    def test_quit_game(self):
        actions = ActionsCapturer()

        model = MainMenu()

        actions.key_right = True
        model.update(actions)
        actions.to_default()

        actions.key_right = True
        model.update(actions)
        actions.to_default()

        actions.key_right = True
        model.update(actions)
        actions.to_default()

        actions.key_a = True
        self.assertEqual(model.update(actions), 'quit')

    def test_multiple_left(self):
        actions = ActionsCapturer()

        model = MainMenu()

        for i in range(3):
            actions.key_left = True
            model.update(actions)
            actions.to_default()

        actions.key_a = True
        self.assertEqual(model.update(actions), 'game')

    def test_multiple_right(self):
        actions = ActionsCapturer()

        model = MainMenu()

        for i in range(10):
            actions.key_right = True
            model.update(actions)
            actions.to_default()

        actions.key_a = True
        self.assertEqual(model.update(actions), 'quit')


class SettingsMenuTest(unittest.TestCase):
    def test_close_settings(self):
        actions = ActionsCapturer()

        model = SettingsMenu()

        actions.key_a = True
        self.assertEqual(model.update(actions), 'main_menu')

    def test_multuple_down(self):
        actions = ActionsCapturer()

        model = SettingsMenu()

        for i in range(3):
            actions.key_down = True
            model.update(actions)
            actions.to_default()

        actions.key_a = True
        self.assertEqual(model.update(actions), 'main_menu')

    def test_check_active_toggle_button(self):
        actions = ActionsCapturer()

        model = SettingsMenu()

        for i in range(2):
            actions.key_up = True
            model.update(actions)
            actions.to_default()

        actions.key_a = True
        model.update(actions)
        self.assertEqual(model.buttons[0].active, True)

    def test_change_toggle_button(self):
        actions = ActionsCapturer()

        model = SettingsMenu()

        first_state = model.buttons[0].enabled

        for i in range(2):
            actions.key_up = True
            model.update(actions)
            actions.to_default()

        actions.key_a = True
        model.update(actions)
        self.assertEqual(model.buttons[0].enabled, not first_state)

    def test_check_active_button(self):
        actions = ActionsCapturer()

        model = SettingsMenu()

        for i in range(1):
            actions.key_up = True
            model.update(actions)
            actions.to_default()

        actions.key_a = True
        model.update(actions)
        self.assertEqual(model.buttons[1].active, True)

    def test_change_screen_mode(self):
        config = {'FULL SCREEN': True}
        CONFIG_FILE = '../tortilla/config.json'
        try:
            with open(CONFIG_FILE) as f:
                _config = json.load(f)
        except FileNotFoundError:
            _config = {}
        for k, v in config.items():
            config[k] = _config[k]

        first_state = config['FULL SCREEN']

        actions = ActionsCapturer()

        model = SettingsMenu()

        for i in range(2):
            actions.key_up = True
            model.update(actions)
            actions.to_default()

        actions.key_a = True
        model.update(actions)
        actions.to_default()

        actions.key_down = True
        model.update(actions)
        actions.to_default()

        actions.key_a = True
        model.update(actions)
        actions.to_default()

        try:
            with open(CONFIG_FILE) as f:
                _config = json.load(f)
        except FileNotFoundError:
            _config = {}
        for k, v in config.items():
            config[k] = _config[k]

        self.assertEqual(config['FULL SCREEN'], not first_state)


class GameTest(unittest.TestCase):
    def test_current_player_parameter(self):
        game = Game()
        self.assertEqual(game.current_player, game.players[0])

    def test_game_status_parameter(self):
        game = Game()
        self.assertEqual(game.status, GameStatus.Active)

    def test_next_turn(self):
        game = Game()
        previous_player = game.current_player
        game.set_next_turn()

        self.assertEqual(game.players[(previous_player.player_id + 1) % len(game.players)], game.current_player)


class FieldTest(unittest.TestCase):
    def test_rows_parameter(self):
        field = Field(12, 20)
        self.assertEqual(field.rows, 12)

    def test_cols_parameter(self):
        field = Field(12, 20)
        self.assertEqual(field.cols, 20)

    def test_hexagon_count(self):
        field = Field(5, 20)
        hexagon_count = 0
        for row in field.hexagons:
            hexagon_count += len(row)
        self.assertEqual(hexagon_count, 98)

    def test_initial_directed_hexagon(self):
        field = Field(5, 20)
        self.assertEqual(field.hexagons[0][0], field.directed_hexagon)

    def test_initial_selected_hexagon(self):
        field = Field(5, 20)
        self.assertEqual(None, field.selected_hexagon)

    def test_initial_reachable_hexagon(self):
        field = Field(5, 20)
        self.assertEqual(None, field.reachable_hexagons)


class PlayerTest(unittest.TestCase):
    def test_player_id(self):
        player = Player(0, 'Uga Buga')
        self.assertEqual(player.player_id, 0)

    def test_player_name(self):
        player = Player(3, 'Gringo')
        self.assertEqual(player.name, 'Gringo')


class HexagonTest(unittest.TestCase):
    def test_hexagon_x_parameter(self):
        hexagon = Hexagon(3, 5)
        self.assertEqual(hexagon.x, 3)

    def test_hexagon_y_parameter(self):
        hexagon = Hexagon(3, 5)
        self.assertEqual(hexagon.y, 5)

    def test_hexagon_coordinates_parameter(self):
        hexagon = Hexagon(3, 5)
        self.assertEqual(hexagon.coordinates, (3, 5))

    def test_hexagon_initial_neighbors(self):
        hexagon = Hexagon(3, 5)
        self.assertEqual(hexagon.neighbors, [])

    def test_hexagon_neighbors(self):
        hexagon_1 = Hexagon(3, 5)
        hexagon_2 = Hexagon(3, 6)
        hexagon_3 = Hexagon(3, 4)
        hexagon_1.neighbors.append(hexagon_2)
        hexagon_1.neighbors.append(hexagon_3)
        self.assertEqual(hexagon_1.neighbors, [hexagon_2, hexagon_3])


class EntityTest(unittest.TestCase):
    def test_entity_none_owner(self):
        entity = Entity(None, 5)
        self.assertEqual(entity.owner, None)

    def test_entity_player_owner(self):
        player = Player(1, 'Ara')
        entity = Entity(player, 5)
        self.assertEqual(entity.owner, player)

    def test_set_another_owner(self):
        player_1 = Player(1, 'Ara')
        player_2 = Player(2, 'Ora')
        entity = Entity(player_1, 5)
        entity.owner = player_2
        self.assertEqual(entity.owner, player_2)

    def test_check_hp(self):
        entity = Entity(None, 5)
        self.assertEqual(entity.health_points, 5)

    def test_set_hp(self):
        entity = Entity(None, 5)
        entity.health_points += 3
        self.assertEqual(entity.health_points, 8)

    def test_initial_killed_state(self):
        entity = Entity(None, 5)
        self.assertEqual(entity.is_killed, False)

    def test_set_killed_state(self):
        entity = Entity(None, 5)
        entity.is_killed = True
        self.assertEqual(entity.is_killed, True)


class MovableTest(unittest.TestCase):
    def test_check_mp(self):
        movable = Movable(None, 5, 10)
        self.assertEqual(movable.move_points, 10)

    def test_set_mp(self):
        movable = Movable(None, 5, 10)
        movable.move_points -= 2
        self.assertEqual(movable.move_points, 8)


class UnmovableTest(unittest.TestCase):
    pass


class ShipTest(unittest.TestCase):
    def test_check_weapon_damage(self):
        ship = Ship(None)
        self.assertEqual(ship.weapon_damage, 1)

    def test_change_mp(self):
        ship = Ship(None)
        ship.move_points -= 1
        self.assertEqual(ship.move_points, 4)

    def test_set_default(self):
        ship = Ship(None)
        ship.move_points -= 3
        ship.set_default()
        self.assertEqual(ship.move_points, 5)


class ObstacleTest(unittest.TestCase):
    def test_check_hp(self):
        obstacle = Obstacle(None)
        self.assertEqual(obstacle.health_points, 1)


class MoveTest(unittest.TestCase):
    def test_correct_move(self):
        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        hexagon_1.neighbors.append(hexagon_2)
        hexagon_1.entity = Ship(None)

        self.assertEqual(Move.execute(hexagon_1, hexagon_2), True)

    def test_move_to_no_neighbor(self):
        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        hexagon_1.entity = Ship(None)

        self.assertEqual(Move.execute(hexagon_1, hexagon_2), False)

    def test_move_to_same_hexagon(self):
        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        hexagon_1.neighbors.append(hexagon_2)
        hexagon_1.entity = Ship(None)

        self.assertEqual(Move.execute(hexagon_1, hexagon_1), False)

    def test_change_mp(self):
        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        hexagon_1.neighbors.append(hexagon_2)
        ship = Ship(None)
        hexagon_1.entity = ship
        initial_mp = ship.move_points
        Move.execute(hexagon_1, hexagon_2)

        self.assertEqual(ship.move_points, initial_mp - 1)

    def test_not_enough_mp(self):
        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        hexagon_1.neighbors.append(hexagon_2)
        ship = Ship(None)
        hexagon_1.entity = ship
        ship.move_points = 0
        self.assertEqual(Move.execute(hexagon_1, hexagon_2), False)

    def test_entity_in_end(self):
        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        hexagon_1.neighbors.append(hexagon_2)
        ship = Ship(None)
        hexagon_1.entity = ship
        hexagon_2.entity = Obstacle(None)
        self.assertEqual(Move.execute(hexagon_1, hexagon_2), False)

    def test_start_hexagon_after_correct_move(self):
        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        hexagon_1.neighbors.append(hexagon_2)
        hexagon_1.entity = Ship(None)
        Move.execute(hexagon_1, hexagon_2)

        self.assertEqual(hexagon_1.entity, None)

    def test_start_hexagon_after_incorrect_move(self):
        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        hexagon_1.neighbors.append(hexagon_2)
        ship = Ship(None)
        hexagon_1.entity = ship
        hexagon_2.entity = Obstacle(None)
        Move.execute(hexagon_1, hexagon_2)
        self.assertEqual(hexagon_1.entity, ship)


class AttackTest(unittest.TestCase):
    def test_correct_attack(self):
        player_1 = Player(1, 'Uga')
        player_2 = Player(2, 'Buda')

        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        hexagon_1.entity = Ship(player_1)
        hexagon_2.entity = Ship(player_2)

        self.assertEqual(Attack.execute(hexagon_1, hexagon_2), True)

    def test_attack_to_allied_entity(self):
        player_1 = Player(1, 'Uga')
        player_2 = Player(2, 'Buda')

        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        hexagon_1.entity = Ship(player_1)
        hexagon_2.entity = Ship(player_1)

        self.assertEqual(Attack.execute(hexagon_1, hexagon_2), False)

    def test_change_mp(self):
        player_1 = Player(1, 'Uga')
        player_2 = Player(2, 'Buda')

        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        ship_1, ship_2 = Ship(player_1), Ship(player_2)
        hexagon_1.entity = ship_1
        hexagon_2.entity = ship_2

        Attack.execute(hexagon_1, hexagon_2)
        self.assertEqual(ship_1.move_points, 0)

    def test_not_enough_mp(self):
        player_1 = Player(1, 'Uga')
        player_2 = Player(2, 'Buda')

        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        ship_1, ship_2 = Ship(player_1), Ship(player_2)
        ship_1.move_points = 2
        hexagon_1.entity = ship_1
        hexagon_2.entity = ship_2

        self.assertEqual(Attack.execute(hexagon_1, hexagon_2), False)

    def change_hp(self):
        player_1 = Player(1, 'Uga')
        player_2 = Player(2, 'Buda')

        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        ship_1, ship_2 = Ship(player_1), Ship(player_2)
        initial_hp = ship_2.health_points
        hexagon_1.entity = ship_1
        hexagon_2.entity = ship_2

        Attack.execute(hexagon_1, hexagon_2)
        self.assertEqual(ship_2.health_points, initial_hp - 1)

    def test_kill(self):
        player_1 = Player(1, 'Uga')
        player_2 = Player(2, 'Buda')

        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        ship_1, ship_2 = Ship(player_1), Ship(player_2)
        ship_2.health_points = 1
        hexagon_1.entity = ship_1
        hexagon_2.entity = ship_2

        Attack.execute(hexagon_1, hexagon_2)
        self.assertEqual(ship_2.is_killed, True)

    def test_no_entity(self):
        player_1 = Player(1, 'Uga')
        player_2 = Player(2, 'Buda')

        hexagon_1 = Hexagon(0, 0)
        hexagon_2 = Hexagon(1, 1)
        ship_1, ship_2 = Ship(player_1), Ship(player_2)
        ship_2.health_points = 1
        hexagon_1.entity = ship_1

        self.assertEqual(Attack.execute(hexagon_1, hexagon_2), False)


class SelectStrategyTest(unittest.TestCase):
    def test_key_left(self):
        game = Game()

        self.assertEqual(SelectStrategy.update_k_left(game), 'select')

    def test_key_left_changes_1(self):
        game = Game()
        SelectStrategy.update_k_left(game)
        initial_hexagon = game.field.directed_hexagon

        self.assertEqual(initial_hexagon, game.field.directed_hexagon)

    def test_key_left_changes_2(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[3][3]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_left(game)

        self.assertEqual(initial_hexagon.neighbors[3], game.field.directed_hexagon)

    def test_key_up(self):
        game = Game()

        self.assertEqual(SelectStrategy.update_k_up(game), 'select')

    def test_key_up_changes_1(self):
        game = Game()
        SelectStrategy.update_k_up(game)
        initial_hexagon = game.field.directed_hexagon

        self.assertEqual(initial_hexagon, game.field.directed_hexagon)

    def test_key_up_changes_2(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[3][3]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_up(game)

        self.assertEqual(initial_hexagon.neighbors[2], game.field.directed_hexagon)

    def test_key_down(self):
        game = Game()

        self.assertEqual(SelectStrategy.update_k_down(game), 'select')

    def test_key_down_changes_1(self):
        game = Game()
        SelectStrategy.update_k_down(game)
        initial_hexagon = game.field.directed_hexagon

        self.assertEqual(initial_hexagon, game.field.directed_hexagon)

    def test_key_down_changes_2(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[3][3]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_down(game)

        self.assertEqual(initial_hexagon.neighbors[5], game.field.directed_hexagon)

    def test_key_right(self):
        game = Game()

        self.assertEqual(SelectStrategy.update_k_right(game), 'select')

    def test_key_right_changes_1(self):
        game = Game()
        SelectStrategy.update_k_right(game)
        initial_hexagon = game.field.directed_hexagon

        self.assertEqual(initial_hexagon, game.field.directed_hexagon)

    def test_key_right_changes_2(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[3][3]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_right(game)

        self.assertEqual(initial_hexagon.neighbors[0], game.field.directed_hexagon)

    def test_key_a_on_empty_hexagon(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[0][0]

        self.assertEqual(SelectStrategy.update_k_a(game), 'select')

    def test_key_a_on_hexagon_with_allied_ship(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]

        self.assertEqual(SelectStrategy.update_k_a(game), 'move')

    def test_key_a_on_hexagon_with_enemy_ship(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[6][5]

        self.assertEqual(SelectStrategy.update_k_a(game), 'overview')

    def test_key_a_on_hexagon_with_obstacle(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[7][3]

        self.assertEqual(SelectStrategy.update_k_a(game), 'overview')

    def test_key_a_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[7][3]

        SelectStrategy.update_k_a(game)
        self.assertEqual(game.field.selected_hexagon, game.field.directed_hexagon)

    def test_key_a_changes_2(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]

        SelectStrategy.update_k_a(game)
        reachable_hexagons = [
            game.field.hexagons[1][1], game.field.hexagons[0][1], game.field.hexagons[0][0],
            None, game.field.hexagons[2][0], game.field.hexagons[2][1]
        ]
        self.assertEqual(game.field.reachable_hexagons, reachable_hexagons)

    def test_key_space(self):
        game = Game()

        self.assertEqual(SelectStrategy.update_k_space(game), 'select')

    def test_key_space_changes(self):
        game = Game()
        initial_player = game.current_player

        SelectStrategy.update_k_space(game)
        self.assertEqual(game.players[(initial_player.player_id + 1) % len(game.players)], game.current_player)


class MoveStrategyTest(unittest.TestCase):
    def test_key_left(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)

        self.assertEqual(MoveStrategy.update_k_left(game), 'move')

    def test_key_left_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_left(game)

        self.assertEqual(initial_hexagon, game.field.directed_hexagon)

    def test_key_left_changes_2(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[3][2]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_left(game)

        self.assertEqual(initial_hexagon.neighbors[3], game.field.directed_hexagon)

    def test_key_up(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)

        self.assertEqual(MoveStrategy.update_k_up(game), 'move')

    def test_key_up_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_up(game)

        self.assertEqual(initial_hexagon.neighbors[2], game.field.directed_hexagon)

    def test_key_down(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)

        self.assertEqual(MoveStrategy.update_k_down(game), 'move')

    def test_key_down_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_down(game)

        self.assertEqual(initial_hexagon.neighbors[5], game.field.directed_hexagon)

    def test_key_right(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)

        self.assertEqual(MoveStrategy.update_k_right(game), 'move')

    def test_key_right_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_right(game)

        self.assertEqual(initial_hexagon.neighbors[0], game.field.directed_hexagon)

    def test_key_a_on_reachable_empty_hexagon(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        game.field.directed_hexagon = game.field.hexagons[2][0]

        self.assertEqual(MoveStrategy.update_k_a(game), 'select')

    def test_key_a_on_reachable_empty_hexagon_changes_1(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        game.field.directed_hexagon = game.field.hexagons[2][0]

        MoveStrategy.update_k_a(game)
        self.assertEqual(game.field.selected_hexagon, None)

    def test_key_a_on_unreachable(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        game.field.directed_hexagon = game.field.hexagons[5][0]

        self.assertEqual(MoveStrategy.update_k_a(game), 'move')

    def test_key_a_on_unreachable_changes_1(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        game.field.directed_hexagon = game.field.hexagons[5][0]

        MoveStrategy.update_k_a(game)
        self.assertEqual(game.field.selected_hexagon, game.field.hexagons[1][0])

    def test_key_escape(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)

        self.assertEqual(MoveStrategy.update_k_escape(game), 'select')

    def test_key_escape_changes_1(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)

        MoveStrategy.update_k_escape(game)
        self.assertEqual(game.field.selected_hexagon, None)

    def test_key_escape_changes_2(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)

        MoveStrategy.update_k_escape(game)
        self.assertEqual(game.field.reachable_hexagons, None)

    def test_key_v(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)

        self.assertEqual(MoveStrategy.update_k_v(game), 'attack')

    def test_key_v_changes_1(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)

        MoveStrategy.update_k_v(game)
        self.assertEqual(game.field.reachable_hexagons, None)


class AttackStrategyTest(unittest.TestCase):
    def test_key_left(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)

        self.assertEqual(AttackStrategy.update_k_left(game), 'attack')

    def test_key_left_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)
        AttackStrategy.update_k_left(game)

        self.assertEqual(initial_hexagon, game.field.directed_hexagon)

    def test_key_left_changes_2(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[3][2]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)
        AttackStrategy.update_k_left(game)

        self.assertEqual(initial_hexagon.neighbors[3], game.field.directed_hexagon)

    def test_key_up(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)

        self.assertEqual(AttackStrategy.update_k_up(game), 'attack')

    def test_key_up_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)
        AttackStrategy.update_k_up(game)

        self.assertEqual(initial_hexagon.neighbors[2], game.field.directed_hexagon)

    def test_key_down(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)

        self.assertEqual(AttackStrategy.update_k_down(game), 'attack')

    def test_key_down_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)
        AttackStrategy.update_k_down(game)

        self.assertEqual(initial_hexagon.neighbors[5], game.field.directed_hexagon)

    def test_key_right(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)

        self.assertEqual(AttackStrategy.update_k_right(game), 'attack')

    def test_key_right_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        initial_hexagon = game.field.directed_hexagon
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)
        AttackStrategy.update_k_right(game)

        self.assertEqual(initial_hexagon.neighbors[0], game.field.directed_hexagon)

    def test_key_a_on_hexagon_with_enemy_entity(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)
        game.field.directed_hexagon = game.field.hexagons[6][5]

        self.assertEqual(AttackStrategy.update_k_a(game), 'select')

    def test_key_a_on_hexagon_with_enemy_entity_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)
        game.field.directed_hexagon = game.field.hexagons[6][5]
        AttackStrategy.update_k_a(game)

        self.assertEqual(game.field.selected_hexagon, None)

    def test_key_a_on_empty_hexagon(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)
        game.field.directed_hexagon = game.field.hexagons[0][0]

        self.assertEqual(AttackStrategy.update_k_a(game), 'attack')

    def test_key_a_on_empty_hexagon_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)
        game.field.directed_hexagon = game.field.hexagons[0][0]
        AttackStrategy.update_k_a(game)

        self.assertEqual(game.field.selected_hexagon, game.field.hexagons[1][0])

    def test_key_escape(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)

        self.assertEqual(AttackStrategy.update_k_escape(game), 'select')

    def test_key_escape_changes_1(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)
        AttackStrategy.update_k_escape(game)

        self.assertEqual(game.field.selected_hexagon, None)

    def test_key_v(self):
        game = Game()

        game.field.directed_hexagon = game.field.hexagons[1][0]
        SelectStrategy.update_k_a(game)
        MoveStrategy.update_k_v(game)

        self.assertEqual(AttackStrategy.update_k_v(game), 'move')


class OverviewStrategyTest(unittest.TestCase):
    def test_key_escape(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[7][3]
        SelectStrategy.update_k_a(game)

        self.assertEqual(OverviewStrategy.update_k_escape(game), 'select')

    def test_key_escape_changes_1(self):
        game = Game()
        game.field.directed_hexagon = game.field.hexagons[7][3]
        SelectStrategy.update_k_a(game)
        OverviewStrategy.update_k_escape(game)

        self.assertEqual(game.field.selected_hexagon, None)


class WidgetTest(unittest.TestCase):
    def test_widget_active_parameter_1(self):
        widget = WidgetModel(lambda: 'main_menu')
        self.assertEqual(widget.active, False)

    def test_widget_active_parameter_2(self):
        widget = WidgetModel(lambda: 'main_menu')
        widget.active = True
        self.assertEqual(widget.active, True)

    def test_widget_execute(self):
        widget = WidgetModel(lambda: 'main_menu')
        self.assertEqual(widget.execute(), 'main_menu')

    def test_toggle_button_enabled_parameter_1(self):
        toggle_button = ToggleButton(lambda: 'main_menu', True)
        self.assertEqual(toggle_button.enabled, True)

    def test_toggle_button_enabled_parameter_2(self):
        toggle_button = ToggleButton(lambda: 'main_menu', False)
        self.assertEqual(toggle_button.enabled, False)

    def test_toggle_button_execute(self):
        toggle_button = ToggleButton(lambda: 'main_menu', False)
        self.assertEqual(toggle_button.execute(), 'main_menu')

    def test_toggle_button_execute_changes_1(self):
        toggle_button = ToggleButton(lambda: 'main_menu', False)
        toggle_button.execute()
        self.assertEqual(toggle_button.enabled, True)

    def test_toggle_button_execute_changes_2(self):
        toggle_button = ToggleButton(lambda: 'main_menu', True)
        toggle_button.execute()
        self.assertEqual(toggle_button.enabled, False)


class ActionsCapturerTest(unittest.TestCase):
    def test_key_a_parameter_1(self):
        actions = ActionsCapturer()
        self.assertEqual(actions.key_a, False)

    def test_key_a_parameter_2(self):
        actions = ActionsCapturer()
        actions.key_a = True
        self.assertEqual(actions.key_a, True)

    def test_key_left_parameter_1(self):
        actions = ActionsCapturer()
        self.assertEqual(actions.key_left, False)

    def test_key_left_parameter_2(self):
        actions = ActionsCapturer()
        actions.key_left = True
        self.assertEqual(actions.key_left, True)

    def test_key_right_parameter_1(self):
        actions = ActionsCapturer()
        self.assertEqual(actions.key_right, False)

    def test_key_right_parameter_2(self):
        actions = ActionsCapturer()
        actions.key_right = True
        self.assertEqual(actions.key_right, True)

    def test_key_up_parameter_1(self):
        actions = ActionsCapturer()
        self.assertEqual(actions.key_up, False)

    def test_key_up_parameter_2(self):
        actions = ActionsCapturer()
        actions.key_up = True
        self.assertEqual(actions.key_up, True)

    def test_key_down_parameter_1(self):
        actions = ActionsCapturer()
        self.assertEqual(actions.key_down, False)

    def test_key_down_parameter_2(self):
        actions = ActionsCapturer()
        actions.key_down = True
        self.assertEqual(actions.key_down, True)

    def test_key_escape_parameter_1(self):
        actions = ActionsCapturer()
        self.assertEqual(actions.key_escape, False)

    def test_key_escape_parameter_2(self):
        actions = ActionsCapturer()
        actions.key_escape = True
        self.assertEqual(actions.key_escape, True)

    def test_key_v_parameter_1(self):
        actions = ActionsCapturer()
        self.assertEqual(actions.key_v, False)

    def test_key_v_parameter_2(self):
        actions = ActionsCapturer()
        actions.key_v = True
        self.assertEqual(actions.key_v, True)

    def test_key_space_parameter_1(self):
        actions = ActionsCapturer()
        self.assertEqual(actions.key_space, False)

    def test_key_space_parameter_2(self):
        actions = ActionsCapturer()
        actions.key_space = True
        self.assertEqual(actions.key_space, True)

    def test_to_default_1(self):
        actions = ActionsCapturer()
        actions.key_space = True
        actions.to_default()
        self.assertEqual(actions.key_space, False)

    def test_to_default_2(self):
        actions = ActionsCapturer()
        actions.key_space = True
        actions.key_a = True
        actions.key_up = True
        actions.key_escape = True
        actions.to_default()
        self.assertEqual((actions.key_space, actions.key_a, actions.key_up, actions.key_escape), (False, False, False, False))


if __name__ == '__main__':
    unittest.main()
