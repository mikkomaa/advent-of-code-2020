def rotate_waypoint_right(x, y, value):
    """Return the waypoint's x and y coordinates after rotating it right."""
    for _ in range(0, value, 90):
        x, y = y, -x
    return x, y


def rotate_waypoint_left(x, y, value):
    """Return the waypoint's x and y coordinates after rotating it left."""
    return rotate_waypoint_right(x, y, 360 - value)


# x and y are the waypoint's coordinates.
commands = dict(N=lambda x, y, value: (x, y + value),
                S=lambda x, y, value: (x, y - value),
                E=lambda x, y, value: (x + value, y),
                W=lambda x, y, value: (x - value, y),
                L=rotate_waypoint_left,
                R=rotate_waypoint_right)


def navigate(instructions):
    """Run the instructions. Return the Manhattan distance."""
    xs, ys = 0, 0  # The ship's coordinates.
    x, y = 10, 1  # The waypoint's coordinates.

    for instruction in instructions:
        action, value = instruction[0], int(instruction[1:])
        if action == 'F':
            xs += value * x
            ys += value * y
        else:
            x, y = commands[action](x, y, value)
    return abs(xs) + abs(ys)


if __name__ == '__main__':
    with open('../data/day12.txt') as f:
        instructions = [line.strip() for line in f]
    print(navigate(instructions))
