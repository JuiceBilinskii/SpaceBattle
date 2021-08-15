def cube_add(a: (int, int, int), b: (int, int, int)):
    result = (a[0] + b[0], a[1] + b[1], a[2] + b[2])
    return result


def axial_add(a: (int, int), b: (int, int)):
    result = (a[0] + b[0], a[1] + b[1])
    return result
