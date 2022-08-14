import collections


def parse(strings):
    """Return two decks as deques."""
    for line in strings:
        line = line.strip()
        if line.startswith('Player'):
            deck = collections.deque()
        elif not line:
            deck1 = deck
        else:
            deck.append(int(line))
    return deck1, deck


def play(deck1, deck2):
    """Play one game. Return the winning player's deck."""
    while deck1 and deck2:
        card1, card2 = deck1.popleft(), deck2.popleft()
        if card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    return deck1 if deck1 else deck2


def score(deck):
    """Return the score of deck."""
    return sum(deck.pop() * i for i in range(1, len(deck) + 1))


if __name__ == '__main__':
    with open('../data/day22.txt') as f:
        strings = [line.strip() for line in f]
    deck1, deck2 = parse(strings)
    winners_deck = play(deck1, deck2)
    print(score(winners_deck))
