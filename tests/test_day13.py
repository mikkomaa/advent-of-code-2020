from src.day13_1 import search
import src.day13_2 as part2

data = '''939
7,13,x,x,59,x,31,19'''


def test_part_1():
    timestamp, ids = data.split()
    timestamp = int(timestamp)
    ids = [int(id) for id in ids.split(',') if id.isdigit()]
    assert search(timestamp, ids) == 295


def test_part_2_a():
    ids = data.split()[1].strip().split(',')
    ids = [(int(id), offset) for offset, id in enumerate(ids) if id.isdigit()]
    assert part2.search(ids) == 1068781


def test_part_2_b():
    ids = [(id, offset) for offset, id in enumerate([17, 'x', 13, 19])
           if id != 'x']
    assert part2.search(ids) == 3417
