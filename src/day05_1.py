def convert_partitioning(string):
    """Return the integer converted from space partitioning string."""
    low = 0
    high = 2 ** len(string) - 1
    for c in string:
        if c in 'FL':
            high = (low + high) // 2
        else:  # c in 'BR'
            low = (low + high) // 2 + 1
    return low


def find_seat_id(string):
    """Given space partitioning string, return the seat ID."""
    return (convert_partitioning(string[:7]) * 8
            + convert_partitioning(string[7:]))


if __name__ == '__main__':
    with open('../data/day05.txt') as f:
        decodings = [line.strip() for line in f]
    print(max(find_seat_id(d) for d in decodings))
