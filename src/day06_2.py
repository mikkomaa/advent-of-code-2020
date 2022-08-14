def sum_yes_everyone(groups):
    """Given every group as a string, return the sum of yes answers."""
    yes = 0
    for group in groups:
        yes += len(set.intersection(*map(set, group.split())))
    return yes


if __name__ == '__main__':
    with open('../data/day06.txt') as f:
        groups = f.read().split('\n\n')
    print(sum_yes_everyone(groups))
