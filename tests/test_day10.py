from src.day10_1 import find_product
from src.day10_2 import count

joltages = '16 10 15 5 1 11 7 19 6 12 4'
joltages2 = '28 33 18 42 31 14 46 20 48 47 24 23 49 45 19 38 39 11 1 32 25 35 8 17 7 9 4 2 34 10 3'


def test_part_1():
    ratings = [int(j) for j in joltages.split()]
    assert find_product(ratings) == 35


def test_part_2_a():
    ratings = [int(j) for j in joltages.split()]
    assert count(tuple(sorted(ratings)), 0) == 8


def test_part_2_b():
    ratings = [int(j) for j in joltages2.split()]
    assert count(tuple(sorted(ratings)), 0) == 19208

