def product_of_three(entries):
    """Return the product of three entries that sum to 2020."""
    for i in range(len(entries)):
        for j in range(i+1, len(entries)):
            for k in range(j+1, len(entries)):
                if entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i] * entries[j] * entries[k]


if __name__ == '__main__':
    with open('../data/day01.txt') as f:
        entries = [int(line.strip()) for line in f]
    print(product_of_three(entries))
