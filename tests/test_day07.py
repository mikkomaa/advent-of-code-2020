from src.day07_1 import parse, contains
from src.day07_2 import count_bags

rules = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

rules_2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''


def test_part_1():
    bags = parse(rules.splitlines(keepends=True))
    assert sum(contains(bag, bags) for bag in bags) == 4


def test_part_2_a():
    bags = parse(rules.splitlines(keepends=True))
    assert count_bags('shiny gold', bags) - 1 == 32


def test_part_2_b():
    bags = parse(rules_2.splitlines(keepends=True))
    assert count_bags('shiny gold', bags) - 1 == 126
