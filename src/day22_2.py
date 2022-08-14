import collections
import itertools

from src.day22_1 import parse, score


def play(deck1, deck2):
    """Play one (recursive) game. Return the decks (loser's deck empty)."""
    seen = set()
    while deck1 and deck2:
        cards = deck1.__str__() + deck2.__str__()
        if cards in seen:
            return deck1, deck2.clear()
        seen.add(cards)

        card1, card2 = deck1.popleft(), deck2.popleft()
        if len(deck1) >= card1 and len(deck2) >= card2:
            subdeck1 = collections.deque(itertools.islice(deck1, card1))
            subdeck2 = collections.deque(itertools.islice(deck2, card2))
            if play(subdeck1, subdeck2)[0]:
                deck1.extend([card1, card2])
            else:
                deck2.extend([card2, card1])
        elif card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    return deck1, deck2


if __name__ == '__main__':
    with open('../data/day22.txt') as f:
        strings = [line.strip() for line in f]
    deck1, deck2 = parse(strings)
    deck1, deck2 = play(deck1, deck2)
    print(max(score(deck) for deck in (deck1, deck2)))
