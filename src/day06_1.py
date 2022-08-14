def sum_yes_anyone(groups):
    """Given every group as a string, return the sum of yes answers."""
    return sum(len(set(''.join(g.split()))) for g in groups)


if __name__ == '__main__':
    with open('../data/day06.txt') as f:
        groups = f.read().split('\n\n')
    print(sum_yes_anyone(groups))
