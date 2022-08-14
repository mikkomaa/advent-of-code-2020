from src.day12_1 import navigate
import src.day12_2 as part2

data = '''F10
N3
F7
R90
F11'''


def test_part_1():
    instructions = [line.strip() for line in data.splitlines()]
    assert navigate(instructions) == 25


def test_part_2():
    instructions = [line.strip() for line in data.splitlines()]
    assert part2.navigate(instructions) == 286
