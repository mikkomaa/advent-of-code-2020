import collections
import itertools


def find_product(ratings):
    """Return the product of 1-jolt and 3-jolt differences."""
    ratings.append(0)  # the charging outlet
    ratings.sort()
    ratings.append(ratings[-1] + 3)  # the device's adapter
    
    diff = collections.defaultdict(int)
    for a, b in itertools.pairwise(ratings):
        diff[b - a] += 1
    return diff[1] * diff[3]


if __name__ == '__main__':
    with open('../data/day10.txt') as f:
        ratings = [int(line.strip()) for line in f]
    print(find_product(ratings))
