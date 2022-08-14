def move(cups):
    """Given cups (current first), make one move. Return the new cup order."""
    destination = cups[0] - 1 if cups[0] > 1 else 9
    while destination in cups[1:4]:
        destination -= 1 if destination > 1 else -8
    i = cups.index(destination)
    return cups[4:i] + [cups[i]] + cups[1:4] + cups[i+1:] + [cups[0]]


def play(cups, moves=100):
    """Play one game. Return the labels on the cups after cup 1."""
    cups = [int(c) for c in cups]
    for _ in range(moves):
        cups = move(cups)
    i = cups.index(1)
    return ''.join(str(n) for n in cups[i+1:] + cups[:i])


if __name__ == '__main__':
    print(play('792845136'))
