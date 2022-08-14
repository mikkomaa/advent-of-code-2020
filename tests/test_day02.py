from src.day02_1 import is_password_valid as is_password_valid_1
from src.day02_2 import is_password_valid as is_password_valid_2

lines = ['1-3 a: abcde\n', '1-3 b: cdefg\n', '2-9 c: ccccccccc']


def test_1():
    assert sum(is_password_valid_1(line) for line in lines) == 2


def test_2():
    assert sum(is_password_valid_2(line) for line in lines) == 1
