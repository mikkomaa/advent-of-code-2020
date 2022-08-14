def product_of_two(entries):
    """Return the product of two entries that sum to 2020."""
    s = set()
    for entry in entries:
        if 2020 - entry in s:
            return (2020 - entry) * entry
        s.add(entry)


if __name__ == '__main__':
    with open('../data/day01.txt') as f:
        entries = [int(line.strip()) for line in f]
    print(product_of_two(entries))
