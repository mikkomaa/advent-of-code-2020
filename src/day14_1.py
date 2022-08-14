import re


def execute(instructions):
    """Run the instructions. Return the sum of values left in memory."""
    addresses = dict()

    for i in instructions:
        if i.startswith('mask'):
            mask = i.split()[2]
            and_mask = int(mask.replace('X', '1'), 2)
            or_mask = int(mask.replace('X', '0'), 2)
        else:
            address, value = re.findall(r'[0-9]+', i)
            addresses[address] = int(value) & and_mask | or_mask
    return sum(value for value in addresses.values())


if __name__ == '__main__':
    with open('../data/day14.txt') as f:
        instructions = [line.strip() for line in f.readlines()]
    print(execute(instructions))
