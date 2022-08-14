import itertools


def find_list(numbers, n):
    """Return the list of contiguous numbers that sum to n."""
    total = 0
    j = 0  # We search for a slice numbers[i:j].
    for i in itertools.count():
        while total > n:
            j -= 1
            total -= numbers[j]
        while total < n:
            total += numbers[j]
            j += 1
        if total == n and i + 1 < j:
            return numbers[i:j]
        total -= numbers[i]


if __name__ == '__main__':
    with open('../data/day09.txt') as f:
        numbers = [int(line.strip()) for line in f]
    lst = find_list(numbers, 1124361034)
    print(min(lst) + max(lst))
