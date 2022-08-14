import itertools


def search(pairs):
    """Given the list of (id, offset) pairs, return the earliest timestamp."""
    start, step = 0, 1
    for id, offset in pairs:
        for t in itertools.count(start, step):
            if (t + offset) % id == 0:
                start = t
                step *= id
                break
    return t


if __name__ == '__main__':
    with open('../data/day13.txt') as f:
        ids = f.readlines()[1].strip().split(',')
        ids = [(int(id), offset) for offset, id in enumerate(ids)
               if id.isdigit()]
        print(search(ids))

# Notes
# All the bus IDs are prime numbers.
# For example, the (id, offset) pairs for the first 3 buses are (19, 0),
# (37, 13), and (751, 19). For each pair we can increment the start and step
# of the search loop.
