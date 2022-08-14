import collections


def init_sums(preamble):
    """Given preamble, return initialised sums."""
    sums = collections.defaultdict(int)
    for i, a in enumerate(preamble):
        for b in preamble[i+1:]:
            sums[a + b] += 1
    return sums


def update(n, sums, previous):
    """Given integer n, update sums and previous numbers."""
    remove = previous.popleft()
    for k in previous:
        sums[n + k] += 1
        s = remove + k
        sums[s] -= 1
        if sums[s] == 0:
            del sums[s]
    previous.append(n)


def find(numbers, npreamble):
    """Given numbers and the length of preamble, return the asked number."""
    previous = collections.deque(numbers[:npreamble])
    sums = init_sums(list(previous))

    for n in numbers[npreamble:]:
        if n not in sums:
            return n
        update(n, sums, previous)


if __name__ == '__main__':
    with open('../data/day09.txt') as f:
        numbers = [int(line.strip()) for line in f]
    print(find(numbers, 25))
