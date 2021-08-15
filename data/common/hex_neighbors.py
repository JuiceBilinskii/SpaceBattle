from data.common import coordinate_math

cube_directions = [
    (+1, -1, 0), (+1, 0, -1), (0, +1, -1),
    (-1, +1, 0), (-1, 0, +1), (0, -1, +1)
]


def cube_direction(direction):
    return cube_directions[direction]


def cube_neighbor(cube, direction):
    coordinate_math.cube_add(cube, cube_directions[direction])


# ----


axial_directions = [
    (+1, 0), (+1, -1), (0, -1),
    (-1, 0), (-1, +1), (0, +1)
]


def axial_direction(direction):
    return axial_directions[direction]


def axial_neighbor(axial, direction):
    return coordinate_math.axial_add(axial, axial_directions[direction])
