import math

from src.day20_1 import Tile, assemble

monster_string = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''


def make_pattern(strings):
    """Return the pattern as a set of (x, y) coordinates."""
    coords = set()
    for y, line in enumerate(strings.split('\n')):
        for x, c in enumerate(line):
            if c == '#':
                coords.add((x, y))
    return coords


def combine(tiles):
    """Given the assembled list of tiles, return the combined image."""
    side = math.isqrt(len(tiles))
    strings = []
    for i in range(0, len(tiles), side):
        for line in range(1, len(tiles[0].image) - 1):
            strings.append(''.join(tile.image[line][1:-1]
                                   for tile in tiles[i:i+side]))
    return Tile(['0'] + strings)


def count(tile, pattern):
    """Return the number of times pattern is found in image."""
    max_x = max(x for x, y in pattern)
    max_y = max(y for x, y in pattern)
    found = 0
    for xi in range(len(tile.image[0]) - max_x):
        for yi in range(len(tile.image) - max_y):
            if all(tile.image[yi + y][xi + x] == '#' for x, y in pattern):
                found += 1
    return found


def roughness(strings):
    """Return the number of water roughness."""
    tiles = set(Tile(string.split(sep='\n')) for string in strings)
    tiles = assemble(tiles)
    image_tile = combine(tiles)
    monster = make_pattern(monster_string)
    for _ in image_tile.orientations():
        monster_count = count(image_tile, monster)
        if monster_count:
            break
    return (sum(c == '#' for line in image_tile.image for c in line)
            - monster_count * len(monster))


if __name__ == '__main__':
    with open('../data/day20.txt') as f:
        strings = f.read().split(sep='\n\n')
    print(roughness(strings))
