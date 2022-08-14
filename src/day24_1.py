import re

deltas = dict(e=(2, 0), se=(1, -1), sw=(-1, -1),
              w=(-2, 0), nw=(-1, 1), ne=(1, 1))


def parse(strings):
    """Return the set of black tile coordinates."""
    blacks = set()
    for string in strings:
        directions = re.findall(r'e|se|sw|w|nw|ne', string)
        directions = [deltas[d] for d in directions]
        x, y = (sum(delta) for delta in zip(*directions))
        blacks.remove((x, y)) if (x, y) in blacks else blacks.add((x, y))
    return blacks


if __name__ == '__main__':
    with open('../data/day24.txt') as f:
        strings = [line.strip() for line in f]
    print(len(parse(strings)))
