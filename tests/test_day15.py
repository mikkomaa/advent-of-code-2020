from src.day15_1 import play


def test_day15_part1():
    numbers = [0, 3, 6]
    assert play(numbers, 10) == 0


# def test_day15_part2():
#     numbers = [0, 3, 6]
#     assert play(numbers, end=30000000) == 175594
