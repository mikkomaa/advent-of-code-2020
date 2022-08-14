def count_trees(lines, right, down):
    """Given the map as lines, return the number of encountered trees."""
    trees = 0
    for y, line in enumerate(lines[::down]):
        if line[(y * right) % len(line)] == '#':
            trees += 1
    return trees


if __name__ == '__main__':
    with open('../data/day03.txt') as f:
        lines = [line.strip() for line in f]
    print(count_trees(lines, 3, 1))
