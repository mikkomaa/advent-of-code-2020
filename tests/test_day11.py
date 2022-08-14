from src.day11_1 import init_seats, simulate
import src.day11_2 as part2

lines = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''


def test_part_1():
    data = [line.strip() for line in lines.split()]
    seats = init_seats(data)
    assert simulate(seats) == 37


def test_part_2():
    data = [line.strip() for line in lines.split()]
    seats = part2.init_seats(data)
    assert part2.simulate(seats) == 26
