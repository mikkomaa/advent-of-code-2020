from src.day16_1 import parse, error_rate
from src.day16_2 import find_fields, order

data = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''

data_2 = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''


def test_day16_1():
    notes = data.splitlines()
    rules, your, nearby = parse(notes)
    assert rules['seat'] == ((13, 40), (45, 50))
    assert your == (7, 1, 14)
    assert nearby == [(7, 3, 47), (40, 4, 50), (55, 2, 20), (38, 6, 12)]
    assert sum(error_rate(t, rules) for t in nearby) == 71


def test_day16_2():
    notes = data_2.splitlines()
    rules, your, nearby = parse(notes)
    field_names = [find_fields(column, rules) for column in zip(*nearby)]
    assert order(field_names) == ['row', 'class', 'seat']

