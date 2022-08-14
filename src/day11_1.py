def init_seats(data):
    """Return a dictionary of seats with coordinates (x, y) as keys."""
    seats = dict()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == 'L':  # We need only seat coordinates.
                seats[(x, y)] = char
    return seats


def neighbors(x, y, seats):
    """Return the coordinates of adjacent seats of the seat (x, y)."""
    points = ((x - 1, y), (x + 1, y),  # left and right
              (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),  # upper
              (x - 1, y + 1), (x, y + 1), (x + 1, y + 1))  # lower
    return [p for p in points if p in seats]


def update(seats):
    """Return a new dictionary of seats after a round of rules applied."""
    new = dict()
    for seat in seats:
        nseats = neighbors(*seat, seats)
        if seats[seat] == 'L' and not any(seats[n] == '#' for n in nseats):
            new[seat] = '#'
        elif seats[seat] == '#' and sum(seats[n] == '#' for n in nseats) >= 4:
            new[seat] = 'L'
        else:
            new[seat] = seats[seat]
    return new


def simulate(seats):
    """Return the number of occupied seats after no seats change state."""
    while True:
        updated = update(seats)
        if updated == seats:
            return sum(seats[s] == '#' for s in seats)
        seats = updated


if __name__ == '__main__':
    with open('../data/day11.txt') as f:
        data = [line.strip() for line in f]
    seats = init_seats(data)
    print(simulate(seats))
