def parse(lines):
    """Return rules as {outer_bag: {inner_bag: quantity, ...}, ...}."""
    rules = dict()
    for rule in lines:
        outer_bag, contents = rule.split(' bags contain ')
        rules[outer_bag] = dict()
        if contents.startswith('no other bags'):
            continue
        contents = contents.split(',')
        for bag in contents:
            quantity, bag = bag.split(maxsplit=1)
            bag = ' '.join(bag.split()[0:2])
            rules[outer_bag][bag] = int(quantity)
    return rules


def contains(bag, bags):
    """Return True if bag contains at least one shiny gold bag, else False."""
    return ('shiny gold' in bags[bag]
            or any(contains(b, bags) for b in bags[bag]))


if __name__ == '__main__':
    with open('../data/day07.txt') as f:
        rules = f.readlines()
    bags = parse(rules)
    print(sum(contains(bag, bags) for bag in bags))
