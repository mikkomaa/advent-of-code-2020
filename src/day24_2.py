import functools

from src.day24_1 import parse


@functools.cache
def get_neighbors(x, y):
    """Given a tile's coordinates, return its neighbors' coordinates."""
    return set((x + xd, y + yd) for xd, yd in ((2, 0), (1, -1), (-1, -1),
                                               (-2, 0), (-1, 1), (1, 1)))


def day(blacks):
    """Given black tiles, return the black tiles after one day."""
    new = set()
    whites = set()

    for black in blacks:
        neighbors = get_neighbors(*black)
        white_neighbors = set(n for n in neighbors if n not in blacks)
        if len(neighbors) - len(white_neighbors) in (1, 2):
            new.add(black)
        whites |= white_neighbors

    for white in whites:
        neighbors = get_neighbors(*white)
        if sum(n in blacks for n in neighbors) == 2:
            new.add(white)
    return new


def execute(strings):
    """Return the number of black tiles after 100 days."""
    blacks = parse(strings)
    for _ in range(100):
        blacks = day(blacks)
    return len(blacks)


if __name__ == '__main__':
    with open('../data/day24.txt') as f:
        strings = [line.strip() for line in f]
    print(execute(strings))
