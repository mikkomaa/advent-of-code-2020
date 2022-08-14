import functools
import itertools
import operator

data = '''....#...
.#..###.
.#.#.###
.#....#.
...#.#.#
#.......
##....#.
.##..#.#'''


def initialize(lines, d=3):
    """Return the d-dimensional coordinates of active cubes."""
    coordinates = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                coordinates.add((x, y, *(0,) * (d - 2)))
    return coordinates


@functools.cache
def deltas(d=3):
    """Return deltas for coordinates of neighbor cubes in d dimensions."""
    return set(itertools.product((-1, 0, 1), repeat=d)) - {(0,) * d}


def get_neighbors(cube):
    """Given a cube's coordinates, return its neighbors' coordinates."""
    neighbors = set()
    for delta in deltas(len(cube)):
        neighbors.add(tuple(map(operator.add, cube, delta)))
    return neighbors


def cycle(actives):
    """Simulate one cycle. Return the new coordinates of active cubes."""
    new = set()
    inactives = set()

    for active in actives:
        neighbors = get_neighbors(active)
        inactive_neighbors = set(n for n in neighbors if n not in actives)
        if 2 <= len(neighbors) - len(inactive_neighbors) <= 3:
            new.add(active)
        inactives |= inactive_neighbors

    for inactive in inactives:
        neighbors = get_neighbors(inactive)
        if sum(n in actives for n in neighbors) == 3:
            new.add(inactive)
    return new


def simulate(actives, cycles=6):
    """Given active cubes, return the number of active cubes after cycles."""
    for _ in range(cycles):
        actives = cycle(actives)
    return len(actives)


if __name__ == '__main__':
    lines = data.split()
    actives = initialize(lines)
    print(simulate(actives))
