import functools


@functools.cache
def count(seq, prev):
    """Return the number of arrangements of tuple (prev, *seq)."""
    if len(seq) == 1:
        return 1
    if seq[1] - prev <= 3:
        # Use the current first item + skip it.
        return count(seq[1:], seq[0]) + count(seq[1:], prev)
    return count(seq[1:], seq[0])


if __name__ == '__main__':
    with open('../data/day10.txt') as f:
        ratings = [int(line.strip()) for line in f]
    print(count(tuple(sorted(ratings)), 0))
