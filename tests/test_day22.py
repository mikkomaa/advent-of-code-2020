from src.day22_1 import parse, play, score
from src.day22_2 import play as play2

decks = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''


def test_part1():
    strings = decks.split('\n')
    deck1, deck2 = parse(strings)
    winners_deck = play(deck1, deck2)
    assert score(winners_deck) == 306


def test_part2():
    strings = decks.split('\n')
    deck1, deck2 = parse(strings)
    deck1, deck2 = play2(deck1, deck2)
    assert sorted(score(deck) for deck in (deck1, deck2)) == [0, 291]
