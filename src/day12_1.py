def run_f(x, y, h, value):
    """Run the F action."""
    headings = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    action = headings[h]
    return commands[action](x, y, h, value)


# The arguments x and y are the ship's coordinates and h is heading.
commands = dict(N=lambda x, y, h, value: (x, y + value, h),
                S=lambda x, y, h, value: (x, y - value, h),
                E=lambda x, y, h, value: (x + value, y, h),
                W=lambda x, y, h, value: (x - value, y, h),
                L=lambda x, y, h, value: (x, y, (h - value) % 360),
                R=lambda x, y, h, value: (x, y, (h + value) % 360),
                F=run_f)


def navigate(instructions):
    """Run the instructions. Return the Manhattan distance."""
    x, y, heading = 0, 0, 90
    for instruction in instructions:
        action, value = instruction[0], int(instruction[1:])
        x, y, heading = commands[action](x, y, heading, value)
    return abs(x) + abs(y)


if __name__ == '__main__':
    with open('../data/day12.txt') as f:
        instructions = [line.strip() for line in f]
    print(navigate(instructions))
