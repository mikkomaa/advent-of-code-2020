from src.day06_1 import sum_yes_anyone
from src.day06_2 import sum_yes_everyone

answers = '''abc

a
b
c

ab
ac

a
a
a
a

b'''


def test_part_1():
    groups = answers.split('\n\n')
    assert sum_yes_anyone(groups) == 11


def test_part_2():
    groups = answers.split('\n\n')
    assert sum_yes_everyone(groups) == 6
