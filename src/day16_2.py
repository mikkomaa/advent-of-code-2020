import itertools

from src.day16_1 import parse


def is_valid(ticket, rules):
    """Return True if ticket is valid, else False."""
    limits = tuple(itertools.chain(*rules.values()))
    for value in ticket:
        if not any(a <= value <= b for a, b in limits):
            return False
    return True


def value_fields(value, rules):
    """Return the names of the fields for which given value is valid."""
    names = set()
    for rule in rules:
        if any(a <= value <= b for a, b in rules[rule]):
            names.add(rule)
    return names


def find_fields(values, rules):
    """Return the names of the fields for which all values are valid."""
    names = set(rules.keys())
    for value in values:
        names &= value_fields(value, rules)
    return names


def order(name_sets):
    """Return a list of field names in right order."""
    order = [''] * len(name_sets)
    for _ in range(len(name_sets)):
        for i, nameset in enumerate(name_sets):
            if len(nameset) == 1:
                order[i] = nameset.pop()
                for s in name_sets:
                    s.discard(order[i])
                break
    return order


def find_product(rules, your, nearby):
    """Return the product of departure values on your ticket."""
    nearby = [ticket for ticket in nearby if is_valid(ticket, rules)]
    field_names = [find_fields(column, rules) for column in zip(*nearby)]
    fields_in_order = order(field_names)

    product = 1
    for name, value in zip(fields_in_order, your):
        if name.startswith('departure'):
            product *= value
    return product


if __name__ == '__main__':
    with open('../data/day16.txt') as f:
        notes = [line.strip() for line in f.readlines()]
    rules, your, nearby = parse(notes)
    print(find_product(rules, your, nearby))
