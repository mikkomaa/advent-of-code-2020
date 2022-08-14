import itertools
import re


def parse(notes):
    """Return rules, your ticket and nearby tickets."""
    rules = dict()
    tickets = []
    for line in notes:
        numbers = tuple(map(int, re.findall(r'[0-9]+', line)))
        if numbers:
            if line[:1].isdigit():
                tickets.append(numbers)
            else:
                a, b, c, d = numbers
                rules[line.split(':')[0]] = ((a, b), (c, d))
    return rules, tickets[0], tickets[1:]


def error_rate(ticket, rules):
    """Return the ticket error rate."""
    rate = 0  # 0 does not necessarily imply a valid ticket.
    limits = tuple(itertools.chain(*rules.values()))
    for value in ticket:
        if not any(a <= value <= b for a, b in limits):
            rate += value
    return rate


if __name__ == '__main__':
    with open('../data/day16.txt') as f:
        notes = [line.strip() for line in f.readlines()]
        rules, _, nearby = parse(notes)
        print(sum(error_rate(ticket, rules) for ticket in nearby))
