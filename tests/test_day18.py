from src.day18_1 import tokenize, expression
from src.day18_2 import expression as expression_part2

data1 = (('1 + 2 * 3 + 4 * 5 + 6', 71),
         ('1 + (2 * 3) + (4 * (5 + 6))', 51),
         ('2 * 3 + (4 * 5)', 26),
         ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
         ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
         ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632))

data2 = (('1 + 2 * 3 + 4 * 5 + 6', 231),
         ('1 + (2 * 3) + (4 * (5 + 6))', 51),
         ('2 * 3 + (4 * 5)', 46),
         ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
         ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
         ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340))


def test_part_1():
    for string, result in data1:
        tokens = tokenize(string)
        assert expression(tokens) == result


def test_part_2():
    for string, result in data2:
        tokens = tokenize(string)
        assert expression_part2(tokens) == result
