import itertools
import re


def get_addresses(address, mask):
    """Generate all addresses based on address and mask."""
    address = f'{int(address):036b}'
    template = ''
    for i, c in enumerate(mask):
        template += c if c in '1X' else address[i]
    template = template.replace('X', '{}')
    for bits in itertools.product('01', repeat=template.count('{')):
        yield template.format(*bits)


def execute(instructions):
    """Run the instructions. Return the sum of values left in memory."""
    addresses = dict()

    for i in instructions:
        if i.startswith('mask'):
            mask = i.split()[2]
        else:
            address, value = re.findall(r'[0-9]+', i)
            for a in get_addresses(address, mask):
                addresses[a] = value
    return sum(int(value) for value in addresses.values())


if __name__ == '__main__':
    with open('../data/day14.txt') as f:
        instructions = [line.strip() for line in f.readlines()]
    print(execute(instructions))
