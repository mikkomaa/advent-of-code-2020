# To make the code fast enough the cups are represented as a list of integers.
# An index i denotes a cup's label and cups[i] the label of the cup
# immediately clockwise. Each move then looks like arranging a linked list.

import itertools


def init_cups(labeling, n=1000000):
    """Return the initial list of cups."""
    cups = [i for i in range(1, n + 2)]
    labeling = [int(c) for c in labeling]
    cups[-1] = labeling[0]
    cups[labeling[-1]] = len(labeling) + 1
    for a, b in itertools.pairwise(labeling):
        cups[a] = b
    return cups


def move(cups, i):
    """Make one move (i is the current index). Return the new current index."""
    three = [cups[i]]
    three.append(cups[three[-1]])
    three.append(cups[three[-1]])

    destination = i - 1 if i > 1 else len(cups) - 1
    while destination in three:
        destination -= 1 if destination > 1 else -(len(cups) - 2)

    cups[i] = cups[three[-1]]
    cups[three[-1]] = cups[destination]
    cups[destination] = three[0]
    return cups[i]


def play(labeling, moves=10000000):
    """Play one game. Return the product of the two labels."""
    cups = init_cups(labeling)
    current_index = int(labeling[0])
    for _ in range(moves):
        current_index = move(cups, current_index)
    return cups[1] * cups[cups[1]]


if __name__ == '__main__':
    print(play('792845136'))
