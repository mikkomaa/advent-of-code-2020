from src.day09_1 import find
from src.day09_2 import find_list

lines = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''


def test_part_1():
    numbers = [int(line.strip()) for line in lines.split()]
    assert find(numbers, 5) == 127


def test_part_2():
    numbers = [int(line.strip()) for line in lines.split()]
    assert find_list(numbers, 127) == [15, 25, 47, 40]
