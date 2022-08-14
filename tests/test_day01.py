from src.day01_1 import product_of_two
from src.day01_2 import product_of_three

entries = [1721, 979, 366, 299, 675, 1456]


def test_product_of_two():
    assert product_of_two(entries) == 514579


def test_product_of_three():
    assert product_of_three(entries) == 241861950
