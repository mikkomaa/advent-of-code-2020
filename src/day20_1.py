# We would need only the borders to solve part 1, but let's use the whole
# tiles because we need the assembled image in part 2 anyway.

import math


class Tile:
    def __init__(self, lines):
        """Given a tile as strings, store the tile ID number and the image."""
        self.id = int(''.join(filter(str.isdigit, lines[0])))
        self.image = [line.strip() for line in lines[1:] if line.strip()]

    def rotate(self):
        """Rotate the tile 90 degrees right."""
        self.image = [''.join(c)[::-1] for c in zip(*self.image)]
        return self

    def flip(self):
        """Flip the tile."""
        self.image = [line[::-1] for line in self.image]
        return self

    def orientations(self):
        """Generate all 8 tile orientations."""
        yield self
        for _ in range(3):
            yield self.rotate()
        yield self.flip()
        for _ in range(3):
            yield self.rotate()

    def up(self):
        """Return the upper border."""
        return self.image[0]

    def down(self):
        """Return the lower border."""
        return self.image[-1]

    def left(self):
        """Return the left border."""
        return ''.join(line[0] for line in self.image)

    def right(self):
        """Return the right border."""
        return ''.join(line[-1] for line in self.image)


def fit(tile, lst, side):
    """Return True if tile fits with tiles and side length, else False."""
    if len(lst) % side and tile.left() != lst[-1].right():
        return False
    if len(lst) >= side and tile.up() != lst[len(lst) - side].down():
        return False
    return True


result = None  # The assembled list of tiles.


def assemble(tiles):
    """Given the set of tiles, return the list of assembled tiles."""

    class Found(Exception):
        """We use this class to terminate the recursive search."""
        pass

    def search(tiles, lst, side):
        """Create the list of assembled tiles, and store it in result."""
        if not tiles:
            global result
            result = lst
            raise Found
        for tile in tiles:
            for t in tile.orientations():
                if fit(t, lst, side):
                    search(tiles - {tile}, lst + [t], side)

    try:
        search(tiles, [], math.isqrt(len(tiles)))
    except Found:
        return result


def multiply_ids(tiles):
    """Return the product of the corner tile IDs of the assembled tiles."""
    side = math.isqrt(len(tiles))
    return (tiles[0].id * tiles[side - 1].id
            * tiles[len(tiles) - side].id * tiles[-1].id)


if __name__ == '__main__':
    with open('../data/day20.txt') as f:
        strings = f.read().split(sep='\n\n')
    tiles = set(Tile(string.split(sep='\n')) for string in strings)
    tiles = assemble(tiles)
    print(multiply_ids(tiles))
