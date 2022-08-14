from src.day17_1 import initialize, simulate

data = '''.#.
..#
###'''


def test_part_1():
    lines = data.split()
    actives = initialize(lines)
    assert simulate(actives) == 112


def test_part_2():
    lines = data.split()
    actives = initialize(lines, d=4)
    assert simulate(actives) == 848
