class Seats(dict):

    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max

    def neighbors(self, x, y):
        """Return the coordinates of seats visible from the seat (x, y)."""
        deltas = ((-1, 0), (1, 0),  # left and right
                  (-1, -1), (0, -1), (1, -1),  # upper
                  (-1, 1), (0, 1), (1, 1))  # lower
        visible = []
        for dx, dy in deltas:
            a, b = x + dx, y + dy
            while 0 <= a <= self.x_max and 0 <= b <= self.y_max:
                if (a, b) in self:
                    visible.append((a, b))
                    break
                a += dx
                b += dy
        return visible

    def apply_rules(self):
        """Return a new dictionary of seats after a round of rules applied."""
        new = Seats(self.x_max, self.y_max)
        for seat in self:
            nseats = self.neighbors(*seat)
            if self[seat] == 'L' and not any(self[n] == '#' for n in nseats):
                new[seat] = '#'
            elif self[seat] == '#' and sum(self[n] == '#' for n in nseats) >= 5:
                new[seat] = 'L'
            else:
                new[seat] = self[seat]
        return new


def init_seats(data):
    """Return a dictionary of seats with coordinates (x, y) as keys."""
    seats = Seats(len(data[0]), len(data))
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == 'L':  # We need only seat coordinates.
                seats[(x, y)] = char
    return seats


def simulate(seats):
    """Return the number of occupied seats after no seats change state."""
    while True:
        updated = seats.apply_rules()
        if updated == seats:
            return sum(seats[s] == '#' for s in seats)
        seats = updated


if __name__ == '__main__':
    with open('../data/day11.txt') as f:
        data = [line.strip() for line in f]
    seats = init_seats(data)
    print(simulate(seats))
