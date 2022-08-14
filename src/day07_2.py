from src.day07_1 import parse


def count_bags(bag, bags):
    """Return the total (bag + its contents)."""
    return 1 + sum(n * count_bags(b, bags)
                   for b, n in bags[bag].items())


if __name__ == '__main__':
    with open('../data/day07.txt') as f:
        rules = f.readlines()
    bags = parse(rules)
    print(count_bags('shiny gold', bags) - 1)
