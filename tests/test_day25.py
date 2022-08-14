from src.day25_1 import get_loop_size


def test_part1():
    assert get_loop_size(5764801) == 8
    assert get_loop_size(17807724) == 11
